from gensim.models import Word2Vec
import re

# 1. Domain-specific corpus (Medical example)
corpus = [
    "The patient was diagnosed with acute hypertension.",
    "Hypertension is often treated with beta-blockers.",
    "Common symptoms of hypertension include headaches and fatigue.",
    "The physician prescribed a low-sodium diet for hypertension.",
    "Chronic hypertension can lead to cardiovascular disease.",
    "The nurse monitored the patient's blood pressure regularly."
]

# 2. Simple preprocessing: lowercase and remove punctuation
tokenized_data = [re.sub(r'[^\w\s]', '', sent).lower().split() for sent in corpus]

# 3. Train Word2Vec model
# vector_size: dimensionality of vectors, window: context distance, min_count: ignore rare words
model = Word2Vec(sentences=tokenized_data, vector_size=50, window=3, min_count=1, workers=1)

# 4. Analyze domain semantics
word = "hypertension"
similar_words = model.wv.most_similar(word, topn=3)

print(f"Words most similar to '{word}':")
for sim_word, score in similar_words:
    print(f" - {sim_word}: {score:.4f}")

# Check similarity between domain-related terms
sim_score = model.wv.similarity("patient", "physician")
print(f"\nSimilarity between 'patient' and 'physician': {sim_score:.4f}")