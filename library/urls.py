"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import django
from django import contrib
from django import urls
from django.contrib import admin, auth
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include("django.contrib.auth.urls")),
    path('',views.home,name='home'),
    path('detail',views.detail,name = 'booklist'),
    # path('booklist/',views.BookList,name='booklist'),
    path('book/<int:pk>', views.BookDetail, name='book-detail'),
    path('bookupload/',views.Bookupload,name='bookupload'),
    path('view/',views.simple_upload, name='bookcreate'),
    path('bookupdate/<int:id>/update/',views.BookUpdate,name='bookupdate'),
    path('bookdelete/<int:id>/delete/',views.BookDelete,name='bookdelete'),
    # path('book/<int:pk>/request_issue/', views.student_request_issue, name='request_issue'),
    path('studentcreate/',views.StudentCreate,name='studentcreate'),
    path('studentlist/', views.StudentList, name='studentlist'),
    path('studentdetail/<int:pk>', views.StudentDetail, name='studentdetail'),
    path('studentupdate/<int:id>/update/',views.StudentUpdate,name='studentupdate'),
    path('studentdelete/<int:id>/delete/',views.StudentDelete,name='studentdelete'),
    path('signup/',views.SignUp,name='signup'),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)