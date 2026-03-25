from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

words = ["computer","software","data","network","ai","robot","chip","server","cloud","code"]
vectors = [model[w] for w in words]

pca = PCA(n_components=2)
reduced = pca.fit_transform(vectors)

plt.scatter(reduced[:,0], reduced[:,1])

for i, w in enumerate(words):
    plt.text(reduced[i,0], reduced[i,1], w)

plt.show()