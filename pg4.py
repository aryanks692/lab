import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

word = "education"
similar = [w for w,_ in model.most_similar(word, topn=5)]

print("Original Prompt: Explain education")
print("Enriched Prompt: Explain education using", similar)