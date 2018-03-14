from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
import posts.models as models
from django.contrib.auth.decorators import login_required
from posts.forms import *
from django.http import HttpResponseRedirect, HttpResponse



class ArticleListView(ListView):
    """ generic list view to render list of articles
    """ 
    model = models.Article
    queryset = models.Article.objects.all()
    paginate_by = 10


@login_required(login_url='/login/')
def create_new(request):
    """ Method to create new article manually
    """
    if request.method == 'GET':
        form = ArticleForm()
    else:
        
        form = ArticleForm(request.POST)
        
        if form.is_valid():
        	title = form.cleaned_data['title']
        	description = form.cleaned_data['description']
        	posted_by = request.user #requested user (loggedin)
        	posted_on = timezone.now() #current time
        	article = models.Article.objects.create(title=title,
        				posted_on=posted_on, posted_by=posted_by,
        				description=description)
        	return HttpResponseRedirect('/')
 
    return render(request, 'posts/new.html', {
        'form': form,
    })


class ArticleDetailView(DetailView):
    model = models.Article
    slug_field = "slug"
    template_name = "posts/article_detail.html"