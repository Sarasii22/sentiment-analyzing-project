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
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative

    logging.info('========== Open home page ============')
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