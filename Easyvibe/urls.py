from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from Api import views

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Easyvibe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/',views.UserRestView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
