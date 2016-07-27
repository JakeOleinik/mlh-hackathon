from django.shortcuts import render
from HTMLParser import HTMLParser

from django.http.response import HttpResponse, HttpResponseRedirect
import logic
import requests
from models import Article
import sys

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

# Create your views here.
def home(request):
    response = render(request, 'webspeechdemo_buggy.html', {})
    return response

def process_words(request):
    query = request.GET['query']
    query_words = query.split()
    result = logic.get_k_most_relevant(query_words, 20)
    response = render(request, 'query_results.html', {'articles': result})
    return response

def get_full_article(request):
    art_id = request.GET['id']
    article = Article.objects.get(id=art_id)
    details = requests.get('http://gva-hackaton-api.twipecloud.net/contentapi/A927F397C5B84435BB01BF10884F4818/contentpackages/' \
                             + str(article.contentPackageID) + '/publications/' + str(article.publicationID) + '/pages/' \
                             + str(article.pageID) + '/articles/' + str(article.articleID) + '.json').json()['details']
    full_text = ''
    for detail in details:
        if detail['ContentType'] == 'text/xml':
            full_text = strip_tags(detail['ArticleText'])



    response = render(request, 'full_article.html', {'article': article, 'full_text': full_text})
    return response

