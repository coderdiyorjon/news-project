from .models import News, Category

def latest_news(request):
    l_news = News.objects.filter(status=News.Status.Published).order_by('-publish_time')[:5]
    categories = Category.objects.all()
    context = {
        'latest_news': l_news,
        'categories': categories,
    }

    return context