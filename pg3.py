from gensim.models import Word2Vec

sentences = [["law", "court"], ["doctor", "hospital", "patient"]]

model = Word2Vec(sentences, vector_size=50, window=2, min_count=1)

print(model.wv["doctor"])