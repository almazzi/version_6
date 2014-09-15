from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from click_app.models import Product

from django.contrib import admin
admin.autodiscover()
admin.site.register(Product)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flip_v6.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('click_app.urls'))
)
#urlpatterns += staticfiles_urlpatterns()