from django.conf.urls import url
from django.contrib import admin
from mysite.views import current_datetime

urlpatterns = [
    url(r'^time/$', current_datetime),
    url(r'^admin/', admin.site.urls),
]
