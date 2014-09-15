from django.conf.urls import patterns, url
from click_app.views import ProductNaProdaje
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('click_app.views',
                       url(r'^$', ProductNaProdaje.as_view()),

)
urlpatterns += staticfiles_urlpatterns()
