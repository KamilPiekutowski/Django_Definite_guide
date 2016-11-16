from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, something):
    something = int(something)
    dt = datetime.datetime.now() + datetime.timedelta(hours=something)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (something, dt)
    return HttpResponse(html)
