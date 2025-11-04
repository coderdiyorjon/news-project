from django.urls import path
from .views import (news_list, ContactPageView, page_not_found, single_page, news_detail, IndexView,
                    LocalNewsView, SportNewsView, AbroadNewsView, TechnoNewsView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'), path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('local-news/', LocalNewsView.as_view(), name='local_news_page'),
    path('sport-news/', SportNewsView.as_view(), name='sport_news_page'),
    path('abroad-news/', AbroadNewsView.as_view(), name='abroad_news_page'),
    path('techno-news/', TechnoNewsView.as_view(), name='techno_news_page'),
    path('not_found/', page_not_found, name='not_found'),
    path('single_page/', single_page, name='single_page'),
]
