from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import app.views



urlpatterns = [
    url(r'^$', app.views.index, name='index'),
    path('admin/', admin.site.urls),
]
