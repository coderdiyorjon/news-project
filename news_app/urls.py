from django.urls import path
from .views import (
    news_list, ContactPageView, page_not_found, single_page, news_detail, IndexView,
    LocalNewsView, SportNewsView, AbroadNewsView, TechnoNewsView,
    NewsUpdateView, NewsDeleteView, NewsCreateView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('news/', news_list, name='all_news_list'),

    # ⚠️ Static URL'lar oldin turadi:
    path('news/create/', NewsCreateView.as_view(), name='news_create_page'),
    path('news/<slug:slug>/edit/', NewsUpdateView.as_view(), name='news_update_page'),
    path('news/<slug:slug>/delete/', NewsDeleteView.as_view(), name='news_delete_page'),

    # 🔽 Keyin dinamik slug yo‘li:
    path('news/<slug:news>/', news_detail, name='news_detail_page'),

    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('local-news/', LocalNewsView.as_view(), name='local_news_page'),
    path('sport-news/', SportNewsView.as_view(), name='sport_news_page'),
    path('abroad-news/', AbroadNewsView.as_view(), name='abroad_news_page'),
    path('techno-news/', TechnoNewsView.as_view(), name='techno_news_page'),
    path('not_found/', page_not_found, name='not_found'),
    path('single_page/', single_page, name='single_page'),
]
