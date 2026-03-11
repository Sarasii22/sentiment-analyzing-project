from flask import Flask, render_template
app = Flask(__name__)

data = dict()
reviews = ['Great product!', 'Not bad, could be better.', 'I love it!', 'Bad quality, do not recommend.', 'Not worth the price.']
positive = 3
negative = 2

@app.route('/')
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)