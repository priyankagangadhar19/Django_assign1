from django.conf.urls import patterns, include, url
from django.contrib import admin
from posts.views import ArticleListView, ArticleDetailView
from users.views import UserProfileDetailView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'news.views.home', name='home'),
    url(r'^$', ArticleListView.as_view(), name='home'),
    url(r'^login/', 'users.views.login', name='login'),
    url(r'^logout/', 'users.views.logout', name='logout'),
    url(r'^register/$', 'users.views.register', name='register'),
    url(r'^submit/$', 'posts.views.create_new', name='submit'),
    url(r"^profile/(?P<slug>\w+)/$", UserProfileDetailView.as_view(),
        name="profile"),
    url(r'^article/(?P<slug>[\w-]+)/$', ArticleDetailView.as_view(),
    name='article_detail'),

    url(r'^admin/', include(admin.site.urls)),
)