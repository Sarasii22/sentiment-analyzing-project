# Sentiment Feedback Analyzer

A Machine Learning web application that analyzes customer reviews and classifies them as **Positive** or **Negative** in real time.

This project demonstrates the **complete machine learning workflow** from data preprocessing to model deployment using Flask.

---

# Problem Statement

Businesses receive a large number of customer reviews daily.  
Manually analyzing each review to understand customer sentiment is inefficient.

This project aims to build a system that can:

- Automatically classify reviews as **Positive or Negative**
- Provide a **confidence score**
- Show the **overall sentiment trend**

---

# Project Workflow

## 1. Dataset Collection

A sentiment analysis dataset containing labeled customer reviews was used.

Each review has:
- **Text**
- **Sentiment Label (Positive / Negative)**

---

## 2. Data Preprocessing

Text preprocessing steps include:

- Convert text to lowercase
- Remove URLs
- Remove punctuation
- Remove numbers
- Remove stopwords
- Stemming using **Snowball Stemmer**


---

## 3. Feature Engineering

Machine learning models cannot understand raw text, so the text is converted into numerical features.

Technique used:

**TF-IDF Vectorization**

Parameters:

- `max_features = 18000`
- `ngram_range = (1,2)`
- `min_df = 2`

This converts text into weighted numerical vectors.

---

## 4. Model Building

Several models were tested:

- Logistic Regression
- Multinomial Naive Bayes
- Decision Tree
- Random Forest
- Support Vector Machine

Final selected model:

**Logistic Regression**

Reason:
- Best balance between accuracy and generalization
- Works well for text classification

---

## 5. Model Evaluation

Evaluation Metrics Used:

- Accuracy
- Precision
- Recall
- F1 Score

Results:

Training Scores:
	Accuracy = 0.926
	Precision = 0.793
	Recall = 0.963
	F1=Score = 0.87
	
Testing Scores:
	Accuracy = 0.878
	Precision = 0.715
	Recall = 0.87
	F1=Score = 0.785

---

## 6. Prediction Pipeline

The prediction pipeline includes:

1. User inputs review text
2. Text is preprocessed
3. TF-IDF vectorizer transforms text
4. Trained model predicts sentiment
5. Confidence score is calculated
6. Result displayed on the website

---

## 7. Web Application

A web interface was built using **Flask**.

Features:

- Enter customer feedback
- Real-time sentiment prediction
- Confidence score display
- Progress bar showing sentiment distribution
- Display recent feedback

---

# Tech Stack

Backend
- Python
- Flask

Machine Learning
- Scikit-learn
- NLTK
- Pandas
- NumPy

Frontend
- HTML
- CSS
- Bootstrap

