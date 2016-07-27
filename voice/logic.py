from models import Article
import heapq
import json

def rank(title, dict, length, query):
    total_sum = 0
    in_title = False
    all_found = True
    for word in query: #getting query values
        found = False
        for k in dict.keys():
            if word.lower() == k:
                found = True
                total_sum+=dict.get(k)
        if not found:
            all_found = False
        if word.lower() in title.lower():
            in_title = True
    norm = total_sum/float(length)
    if not all_found:
        norm/=10.0
    elif in_title:
        norm*=5
    return norm

def get_k_recent_category(category, k=10):
    return Article.objects.all().order_by('publicationDate')[:k] # obtaining k most recent

def get_k_most_relevant(query, k=10):
    PQ = []
    for article in Article.objects.all():
        dict = json.loads(article.built_dict)
        length = len(json.loads(article.words_only))
        title = article.title
        ranking = rank(title, dict, length, query)
        if ranking>0:
            heapq.heappush(PQ, (ranking, article))
            while len(PQ)>k:
                heapq.heappop(PQ)

    result = []

    while len(PQ):
        ranking, article = heapq.heappop(PQ)
        result.append(article)

    return result[::-1]
    #return list(range(10))
#print get_k_recent_category("Sport")

