#from django.conf.urls import url
from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # re_path('^$',views.welcome,name = 'welcome'),
    re_path(r'^$', views.art_of_day, name = 'artToday'),
    re_path(r'^search/', views.search_results, name = 'search_results'),
    re_path(r'^location/(\d+)', views.location, name = 'location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
