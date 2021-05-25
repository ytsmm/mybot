from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def vectorizer(training_text):
    TfidfVec = TfidfVectorizer()
    tfidf = TfidfVec.fit_transform(training_text)
    sim = cosine_similarity(tfidf[-1], tfidf)
    index = sim.argsort()[0][-2]
    flat = sim.flatten()
    flat.sort()
    max_tfidf = flat[-2]

    a = [max_tfidf, index]
    return a
