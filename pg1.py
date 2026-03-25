import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
result = model.most_similar(positive = ["king","woman"],negative = ["man"],topn = 1)
print(result)
