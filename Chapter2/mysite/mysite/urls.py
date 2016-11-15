from django.conf.urls import url
from django.contrib import admin
from mysite.views import current_datetime, hours_ahead

urlpatterns = [
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^admin/', admin.site.urls),
]
