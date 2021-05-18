import gensim

w2v_fpath = "all.norm-sz100-w10-cb0-it1-min100.w2v"
w2v = gensim.models.KeyedVectors.load_word2vec_format(w2v_fpath, binary=True, unicode_errors='ignore')
w2v.init_sims(replace=True)


def vectorizer(a):
    vector_text = []
    for i in range(len(a)):
        vector_text.append([])
        for token in a[i]:
            vector_text[i].append(w2v.most_similar(token))
    return vector_text


