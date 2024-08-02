from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from blog_app.forms import *
from blog_app.models import Blog

def home(request): 

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Saved")
                return redirect('/show_blog')
            except:
                pass
    else:
        form = BlogForm()
    return render(request,"index_form.html",{'form':form})

def show_blog(request):
    blogs = Blog.objects.all()
    return render(request,"show_blog.html",{'blogs':blogs})

def update(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        # blog = Blog.objects.get(id=id)
        print("Save")
        form = BlogForm(request.POST, instance = blog)
        if form.is_valid():
            print("success")
            form.save()
            return redirect("/show_blog")
    else:
        form = BlogForm(instance = blog)
    return render(request, 'edit_blog.html', {'blog': blog})

def destroy(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("/show_blog")

# def edit_post(request, id):
#     form = Blog.objects.get(id=id)

#     if request.method == "POST":
#         print("Save")
#         context = {'blog' : BlogForm(instance = blog), 'id':id }
#         return render(request, 'edit_blog.html', context)
        
#     elif request.method == 'POST':
#         blog = BlogForm(request.POST, instance=blog)
#         if form.is_valid():
#             form.save()
#             return redirect('show_blog')
#         else:
#             return render(request, 'edit_blog.html', {'blog': form})

    

