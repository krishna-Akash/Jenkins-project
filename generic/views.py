from django.shortcuts import render

# Create your views here.

def article_archive(request):
    return render(request, 'article_archive.html')
