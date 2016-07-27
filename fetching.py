from HTMLParser import HTMLParser
import re, string, os
import json
import pickle

with open("hackathon/downloaded1.pkl", 'rb') as f:
    list_articles = pickle.load(f)

with open("hackathon/dummyWords.txt", 'rb') as f:
    dummyWords = set(f.read().split())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackathon.settings")
import django
django.setup()

from datetime import datetime as dt
from voice.models import Article

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


def clean_string(str):
    raw_list = re.findall(r"[\w']+|[.,!?:;]", str)
    raw_list = [w.lower() for w in raw_list if w.isalnum() and not w.lower() in dummyWords]
    return raw_list


def get_or_empty(dictionary, field, f=None):
    if field in dictionary.keys():
        if not f:
            return dictionary[field]
        return f(dictionary[field])
    return None

def build_dict(words_only):
    dict = {}
    for word in words_only:
        if word in dict.keys():
            dict[word]+=1
        else:
            dict[word] = 1
    return dict

"""
class Article:
    def __init__(self):
        self.publicationID = ""
        self.category = ""
        self.contentPackageID = ""
        self.title = ""
        self.author = ""
        self.articleText = ""
        self.articleID = ""
        self.introduction = ""
        self.publicationName = ""
        self.publicationDate = ""
        self.words_only = ""

    def __repr__(self):
        return 'Article #{}, "{}" by {}'.format(self.articleID, self.title, self.author)

    def update(self, art):
        self.publicationID = get_or_empty(art, 'PublicationId')
        self.category = get_or_empty(art, 'Category')
        self.contentPackageID = get_or_empty(art, 'ContentPackageId')
        self.title = strip_tags(get_or_empty(art, 'Title'))
        self.author = get_or_empty(art, 'Author')
        self.articleText = strip_tags(get_or_empty(art, 'ArticleText'))
        self.articleID = get_or_empty(art, 'ArticleId')
        self.introduction = strip_tags(get_or_empty(art,'Introduction'))
        self.publicationName = get_or_empty(art, 'PublicationName')
        self.publicationDate = get_or_empty(art, 'PublicationDate')
        self.words_only = clean_string(self.articleText)
        return self # to allow stacking

    def build_dict(self):
        dict = {}
        for word in self.words_only:
            if word in dict.keys():
                dict[word]+=1
            else:
                dict[word] = 1
        return dict

    #def get_rank(self):


DB = []
dictionaries = []
for art in list_articles:
    new_art = Article().update(art)
    new_dict = new_art.build_dict()
    dictionaries.append((new_dict, len(new_art.words_only)))
    DB.append(new_art)
"""
"""
with open('sample.pkl', 'wb') as f:
    pickle.dump(dictionaries, f)
"""

Article.objects.all().delete()

def populate(list_articles):

    def include(art):
        title = get_or_empty(art, 'Title')
        has_image = get_or_empty(art, 'hasImage')
        if not title or not has_image:
            return
        words_only = get_or_empty(art, 'ArticleText', clean_string)
        defaults={
                'publicationID': get_or_empty(art, 'PublicationId', int),
                'contentPackageID': get_or_empty(art, 'ContentPackageId', int),
                'pageID': get_or_empty(art, 'PageId', int),
                'category': get_or_empty(art, 'Category'),
                'title': get_or_empty(art, 'Title', strip_tags),
                'author': get_or_empty(art, 'Author'),
                'articleText': get_or_empty(art, 'ArticleText', strip_tags),
                'hasImage': get_or_empty(art, 'hasImage'),
                'image': get_or_empty(art, 'image'),
                'introduction': get_or_empty(art, 'Introduction', strip_tags),
                'publicationName': get_or_empty(art, 'PublicationName'),
                'publicationDate': None,
                'words_only': None,
                'built_dict': None
            }

        new_art = Article.objects.get_or_create( articleID = get_or_empty(art, 'ArticleId', int),
                                                 defaults=defaults )[0]


        if words_only:
            new_art.words_only = json.dumps(words_only)
            new_art.built_dict = json.dumps(build_dict(words_only))

        if 'PublicationDate' in art.keys():
            date_str = art['PublicationDate']
            date_str =  date_str.strip('"')
            date = dt.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
            new_art.publicationDate = date
            new_art.save()

    for art in list_articles:
        include(art)

populate(list_articles.values()[:])