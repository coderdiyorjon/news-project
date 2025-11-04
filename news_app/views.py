from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, get_object_or_404
from .models import News, Category
from .forms import ContactForm
# Create your views here.0


def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)
    context = {
        'news_list': news_list,
    }
    return render(request, "news/news_list.html", context=context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news,
    }

    return render(request, 'news/news_detail.html', context)

# def homePageView(request):
#     categories = Category.objects.all()
#     news_list = News.objects.filter(status=News.Status.Published).order_by('-publish_time')[:5]
#     local_new = News.objects.filter(status=News.Status.Published).filter(status=News.Status.Published).order_by('-publish_time')[0]
#     local_news = News.objects.filter(category__name='Mahalliy', status=News.Status.Published).order_by('-publish_time')[1:6]
#     context = {
#         'news_list': news_list,
#         'categories': categories,
#         'local_new': local_new,
#         'local_news': local_news,
#     }
#
#     return render(request, 'news/index.html', context)


class IndexView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.objects.filter(status=News.Status.Published).order_by('-publish_time')[:5]
        local_news_qs = News.objects.filter(status=News.Status.Published, category__name='Mahalliy').order_by(
            '-publish_time')
        context['local_news'] = local_news_qs[0:6]
        abroad_news_qs = News.objects.filter(status=News.Status.Published, category__name='Xorij').order_by(
            '-publish_time')
        context['abroad_news'] = abroad_news_qs[0:6]
        techno_news_qs = News.objects.filter(status=News.Status.Published, category__name='Texnologiya').order_by(
            '-publish_time')
        context['techno_news'] = techno_news_qs[0:6]
        sport_news_qs = News.objects.filter(status=News.Status.Published, category__name='Sport').order_by(
            '-publish_time')
        context['sport_news'] = sport_news_qs[0:6]
        return context


# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2>Biz bilan bog'langaningiz uchun raxmat!</h2>")
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'news/contact.html', context)


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("Thank you for contacting us.")
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


def page_not_found(request):
    context = {}

    return render(request, 'news/404.html', context)

def single_page(request):
    context = {}

    return render(request, 'news/single_page.html', context)


class LocalNewsView(ListView):
    model = News
    template_name = 'news/local.html'
    context_object_name = 'local_news'

    def get_queryset(self):
        news = self.model.objects.filter(status=News.Status.Published, category__name='Mahalliy').order_by('-publish_time')
        return news


class AbroadNewsView(ListView):
    model = News
    template_name = 'news/abroad.html'
    context_object_name = 'abroad_news'

    def get_queryset(self):
        news = self.model.objects.filter(status=News.Status.Published, category__name='Xorij').order_by('-publish_time')
        return news


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.objects.filter(status=News.Status.Published, category__name='Sport').order_by('-publish_time')
        return news


class TechnoNewsView(ListView):
    model = News
    template_name = 'news/techno.html'
    context_object_name = 'techno_news'

    def get_queryset(self):
        news = self.model.objects.filter(status=News.Status.Published, category__name='Texnologiya').order_by('-publish_time')
        return news
