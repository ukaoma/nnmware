from django.conf.urls import *
from nnmware.apps.article.views import *

urlpatterns = patterns('',
    url(r'^search/$', ArticleSearch.as_view(), name='articles_search'),
    url(r'^$', ArticleList.as_view(), name="article_index"),
    url(r'^my/$', ArticleMyList.as_view(), name="article_my"),
    url(r'^locked/$', ArticleLockedList.as_view(), name="article_locked"),
    url(r'^new/$', ArticleList.as_view(), name="article_new"),
    url(r'^updated/$', ArticleUpdatedList.as_view(), name="article_updated"),
    url(r'^popular/$', ArticlePopularList.as_view(), name="article_popular"),
    url(r'^moderation/$', ArticleModerationList.as_view(),
        name="article_moderation"),
    url(r'^deleted/$', ArticleDeletedList.as_view(), name="article_deleted"),
    url(r'^add/$', ArticleAdd.as_view(), name="article_add"),
    url(r'^edit/(?P<pk>[0-9]+)/$', ArticleEdit.as_view(), name="article_edit"),
    url(r'^edit_editor/(?P<pk>[0-9]+)/$', ArticleEditEditor.as_view(),
        name="article_edit_editor"),
    url(r'^edit_admin/(?P<pk>[0-9]+)/$', ArticleEditAdmin.as_view(),
        name="article_edit_admin"),
    url(r'^status/(?P<pk>[0-9]+)/$', ArticleStatus.as_view(),
        name="article_status"),
    url(r'^status_editor/(?P<pk>[0-9]+)/$', ArticleStatusEditor.as_view(),
        name="article_status_editor"),
    url(r'^status_admin/(?P<pk>[0-9]+)/$', ArticleStatusAdmin.as_view(),
        name="article_status_admin"),
    url(r'^category/$', ArticleList.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>.*)/$',
        ArticleDetail.as_view(), name='article_detail'),
    url(r'^(?P<year>\d{4})/$', ArticleYearList.as_view(),
        name='article_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', ArticleMonthList.as_view(),
        name='article_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',
        ArticleDayList.as_view(), name='article_day'),
    url(r'^author/(?P<username>.*)/$', ArticleAuthor.as_view(),
        name='articles_by_author'),
    url(r'^category/(?P<parent_slugs>[-\w]+/)*(?P<slug>[-\w]+)/$',
        ArticleCategory.as_view(), name='articles_category'),

)
