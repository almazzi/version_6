from django.conf.urls import patterns, url
from click_app.views import ProductNaProdaje
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('click_app.views',
                       url(r'^$', ProductNaProdaje.as_view()),
                       url(r'^products/$', 'product_list'),
                       url(r'^bid/$', 'flipDetail'),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns = format_suffix_patterns(urlpatterns)
