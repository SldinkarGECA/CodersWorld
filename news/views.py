from django.shortcuts import render

# Create your views here.
import requests


def news(request):
    url = "https://newsapi.org/v2/everything?q=technology&sortBy=popularity&apiKey=3a84486c8e814609a943c709c7f93453"
    open_bbc_page = requests.get(url).json()
    article = open_bbc_page["articles"]
    return render(request, 'news/news.html', {'categories': article})
