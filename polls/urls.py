from django.conf.urls import url
from .views import index, detail, vote, results
from .views import IndexView, DetailView, ResultView

# The tutorial project has just one app, polls. In real Django projects, there might be five, ten, twenty apps or
# more. How does Django differentiate the URL names between them? For example, the polls app has a detail view,
# and so might an app on the same project that is for a blog. How does one make it so that Django knows which app
# view to create for a url when using the {% url %} template tag?
# The answer is to add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name to set the
#  application namespace:

app_name = 'polls'

urlpatterns = [
    url(r'^$', view=IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', view=DetailView.as_view(), name='detail'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', view=vote, name='vote'),
    url(r'^(?P<pk>[0-9]+)/results/$', view=ResultView.as_view(), name='result'),
]
