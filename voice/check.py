import pickle

with open("sample.pkl", 'rb') as f:
    data = pickle.load(f)
    
query = ['route','check']

def rank(dict, length, query):
    freq_occurence = []
    for i in range(len(query)): #getting query values
        for k in dict.keys():
            if query[i] == k:
                #print "match",t[k]
                freq_occurence.append(dict.get(k))
                #print "freq_occ",freq_occurence
            elif((query[i] != k)):
                freq_occurence.append(0)
                #print "How",freq_occurence

    freq = (sum(freq_occurence))
    print freq
    norm = freq/float(length)
    return norm




