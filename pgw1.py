import gensim.downloader as api


model = api.load("glove-wiki-gigaword-50")


words = ["democrats", "congress", "republican"]


for w in words:
    if w in model:
        print(w, model[w])
    else:
        print(w, "not found in vocabulary")


print("Embedding dimension:", model.vector_size)