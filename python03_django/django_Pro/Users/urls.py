from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
	
	#url(r'^Users/', include(Users.urls)),
	
	url(r'^$', 'Users.views.home', name='home'),
	
	url(r'^random_number/$', 'Users.views.random_number', name='random_number'),
	
)
