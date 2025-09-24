from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import NewsItem

# Create your views here.
def news_list(request: HttpRequest):
    news_objects = NewsItem.objects.all().order_by('-date')
    paginator = Paginator(news_objects, 4)

    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = {'news': news}
    return render(request, "news/news.html", context)
