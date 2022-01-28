from pyexpat import model
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic.edit import UpdateView




def index(request):
    post = Post.objects.all().order_by('-date')
    paginator = Paginator(post, 25)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {'posts': posts}
    return render(request, 'index.html', context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post':post,
        'title':post.title,
        'img':post.image,
        'description':post.body[0:55]
    }
    return render(request, 'post.html', context)


def createPost(request):
    form = CreatePostForm(request.POST)
    if request.method == "POST":
        form = CreatePostForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('create_post')
    context = {'form':form}
    return render(request, 'create-post.html', context)




class UpdatePost(UpdateView):
    template_name = 'update-post.html'
    model = Post
    fields = ['title','image','body','tags']
    success_url = reverse_lazy('home')


def privecy(request):
    return render(request, 'privecy.html',{'title':'GoolBool - Privecy Poslicy'})


def contact(request):
    return render(request, 'contact.html',{'title':'GoolBool - Contact Form'})


def about(request):
    return render(request, 'about.html',{'title':'GoolBool - About Us'})


def dashboard(request):
    return render(request, 'dashboard.html',{'title':'GoolBool - Dashboard'})
