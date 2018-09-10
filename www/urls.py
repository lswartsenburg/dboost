from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import app.views



urlpatterns = [
    url(r'^$', app.views.index, name='index'),
    url(r'^db', app.views.db, name='db'),
    path('admin/', admin.site.urls),
]
