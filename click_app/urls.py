from django.conf.urls import patterns, url
from click_app.views import ProductNaProdaje

urlpatterns = patterns('click_app.views',
                       url(r'^$',ProductNaProdaje.as_view()),

)
