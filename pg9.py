from transformers import pipeline

formalizer = pipeline("text2text-generation", model="google/flan-t5-small")

result = formalizer("Convert this text to a more formal tone: 'Hey, what's up? Let's catch up soon!'")
print(result[0]['generated_text'])

sentence = "Hey bro, whats up? Let's catch up later!"

result = formalizer(
    f"Convert this text to a more formal tone: '{sentence}'",
    max_length=50,
    num_return_sequences=1,
    temperature=1.5
)

print("\nOriginal Sentence:")
print(sentence)

print("\nTransformed Sentence (Formal Style):")
print(result[0]['generated_text'])
