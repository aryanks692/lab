from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")

texts = ["I love chocalates", "I hate peoples", "This is a dog"]

for t in texts:
    print(sentiment_analysis(t))