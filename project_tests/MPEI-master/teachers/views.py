from django.shortcuts import render

def news_add(request):
    return render(request, 'news-add.html')
