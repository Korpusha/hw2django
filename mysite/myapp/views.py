from django.shortcuts import render, HttpResponse
from random import choice
from django.utils.crypto import get_random_string


def main(request):
    res = choice(range(1, 100))
    the_slug = get_random_string(res, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-')
    return render(request, 'main.html', {'ch': res, 'sl': the_slug})


def article(request):
    return render(request, 'article.html')


def article_number(request, article_id):
    return render(request, 'articleNum.html', {'article_id': article_id})


def article_slug(request, article_id, article_sl):
    return render(request, 'articleNum.html', {'article_id': article_id, 'article_sl': article_sl})
