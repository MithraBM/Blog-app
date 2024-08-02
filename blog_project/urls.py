
from django.contrib import admin
from django.urls import path
from blog_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('show_blog', views.show_blog),
    path('home/', views.home),
    # path('edit/<int:id>/', views.edit),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.destroy),
]
