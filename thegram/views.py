from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostCreateForm
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)

from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  
    context_object_name = 'posts'
    
# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['image', 'description']
#     template_name = 'blog/post_form.html'

#     def form_valid(self, form):
#         form.instance.description = self.request.user
#         super().form_valid(form)
#         return form.save()
    
def post_save(request):
    if request.method =='POST':
    # u_form = UserUpdateForm(request.POST, instance=request.user)
        a_form = PostCreateForm(request.POST, request.FILES)
        if a_form.is_valid():
            image = a_form.save(commit=False)
            image.author = request.user
            # u_form.save()
            image.save()
            return redirect('thegram-home')
    else:
        a_form = PostCreateForm()
    return render(request,'blog/post_form.html',{'form':a_form})
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['image', 'description']
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.image:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def search_results(request):
    
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_description(search_term)
        message = f"{search_term}"

        return render(request, 'blog/search.html',{"message":message,"post": searched_posts})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})