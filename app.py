from flask import Flask, render_template, request, redirect
from helper import preprocessing, get_prediction   # only need these
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
        # Only pass raw text — let get_prediction handle preprocessing & vectorization
        prediction = get_prediction(text)
        logging.info(f'Prediction : {prediction}')

        if prediction == 'negative':
            global negative
            negative += 1
        else:
            global positive
            positive += 1

        reviews.insert(0, text)

    except Exception as e:
        logging.error(f"Error processing feedback: {str(e)}")
        # Optional: show error to user, but for now just log and continue
        pass

    return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)  # debug=True is helpful during development