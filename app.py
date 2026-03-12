from flask import Flask, render_template, request, redirect
from helper import preprocessing, get_prediction   
from logger import logging

app = Flask(__name__)

logging.info('Flask server started')

data = dict()
reviews = []
positive = 0
negative = 0

@app.route("/")
def index():
    global reviews, positive, negative

    # Calculate average rating (0–5 stars)
    if reviews:
        total_reviews = len(reviews)
        total_confidence = 0
        
        for r in reviews:
            conf = r['confidence'] / 100.0  # 0.0 to 1.0
            if r['sentiment'] == 'positive':
                total_confidence += conf
            else:
                total_confidence -= conf  # negative reduces score

        avg_score = (total_confidence / total_reviews + 1) / 2  # normalize -1..1 → 0..1
        avg_rating = round(avg_score * 5, 1)  # 0.0 to 5.0
        rating_percentage = round(avg_score * 100, 1)
    else:
        avg_rating = 0.0
        rating_percentage = 0.0

    data['avg_rating'] = avg_rating
    data['rating_percentage'] = rating_percentage
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative

    logging.info(f'========== Open home page ============ (Rating: {avg_rating}/5)')
    return render_template('index.html', data=data)

@app.route("/", methods=['POST'])
def my_post():
    text = request.form.get('text', '').strip()
    
    if not text:
        logging.warning("Empty feedback submitted")
        return redirect(request.url)

    logging.info(f'Text : {text}')

    try:
        prediction, confidence = get_prediction(text)   # ← now tuple
        logging.info(f'Prediction : {prediction} | Confidence: {confidence}%')

        if prediction == 'negative':
            global negative
            negative += 1
        else:
            global positive
            positive += 1

        # Store review as dictionary with confidence
        reviews.insert(0, {
            "text": text,
            "sentiment": prediction,
            "confidence": confidence
        })

    except Exception as e:
        logging.error(f"Error processing feedback: {str(e)}")

    return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)  # debug=True is helpful during development