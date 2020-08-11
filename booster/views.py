from django.shortcuts import render,redirect, get_object_or_404
from booster.models import comment,Post,Blogdes,suscriberr,contact
from .forms import SearchForm,contactForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from booster.templatetags import extras
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.db.models import Count
from booster.templatetags import extras

from django.contrib.postgres.search import SearchVector, SearchQuery,SearchRank






def contct(request):  
        form=contactForm()             
        if request.method=="POST":
                form = contactForm(request.POST)
                if form.is_valid():
                        form.save()                
                        return render(request,'thanks.html')               
                
        else:
                              
                return render(request,'contact.html', {'form':form})  






def suscriber(request):        
        if request.method=="POST":
                email=request.POST.get('emaiil')
                name=request.POST.get('namei')
                oko=suscriberr(email=email, name=name)
                oko.save()                
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) 
        else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) 



       
def post_search(request):
        form = SearchForm()
        query = None
        results = []
        if 'query' in request.GET:
                form = SearchForm(request.GET)
                if form.is_valid():
                        query = form.cleaned_data['query']
                        search_vector = SearchVector('title', weight='A') +  SearchVector('body', weight='B')
                        
                        search_query = SearchQuery(query)
                        results = Post.objects.annotate(search=search_vector, rank=SearchRank(search_vector, search_query) ).filter(rank__gte=0.3).order_by('-rank')
                        
        return render(request,'search.html', {'form': form, 'query': query, 'results': results})
        
         
 
def new(request, tag_slug=None):
        ptr1=Post.objects.all()
        form = SearchForm()
        tag = None
        if tag_slug:
                tag = get_object_or_404(Tag, slug=tag_slug)
                ptr1 = Post.objects.filter(tags__in=[tag])

        paginator = Paginator(ptr1, 1) # 3 posts in each page
        page = request.GET.get('page')
        try:
                posts = paginator.page(page)
        except PageNotAnInteger:
                posts = paginator.page(1)

        except EmptyPage:
                posts = paginator.page(paginator.num_pages)
        return render(request,'home.html' , {'fact': posts, 'form':form ,'page': page,'tag': tag})


     



def detail(request,id,slug):
        form = SearchForm()
        product = get_object_or_404(Post, id=id, slug=slug)
        rec=Post.objects.all()[0:4]
        part = Blogdes.objects.filter(post=id)       
        post_tags_ids = Post.tags.values_list('id', flat=True)
        similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=id)
        similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
        com=comment.objects.filter(postid=id)
        count=comment.objects.filter(postid=id).count()
        return render(request,'detail.html', {'post': product, 'part':part ,'similar_posts': similar_posts ,'rec':rec ,'form':form ,'count':count, 'comment':com })
  
        


def index(request):
        return render(request,'about.html')



      















def addcom(request):                
        
        if request.method =='POST':                         
                body=request.POST.get('body')#comment
                ook=request.POST.get('id')
                name=request.POST.get('name')
                email=request.POST.get('email')               
                commentk=comment(postid=ook, name=name, email=email , body=body)
                if commentk is not None:
                        commentk.save()                
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                
                

        
 