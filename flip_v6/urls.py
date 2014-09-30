from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from click_app.models import Product


from django.contrib import admin
from flip_v6 import settings
from django.conf.urls.static import  static

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flip_v6.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^click/', include('click_app.urls')),
    url(r'^api-auth/login', include('rest_framework.urls', namespace='rest_framework'), name='login'),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()