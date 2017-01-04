from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^Users/', include('Users.urls')),
	
	#url(r'^$', 'django_Pro.views.home', name='home'),
	
	url(r'^$', 'Users.views.index'),
	
	
)
