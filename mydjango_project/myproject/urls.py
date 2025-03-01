"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    # Blog URLs
    path("", views.post_list, name="post_list"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("post/create/", views.create_post, name="create_post"),
    path("post/<slug:slug>/edit/", views.edit_post, name="edit_post"),
    path("post/<slug:slug>/delete/", views.delete_post, name="delete_post"),
    # Comment URLs
    path("post/<slug:slug>/comment/", views.add_comment, name="add_comment"),
    path(
        "comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"
    ),
    # Like/Dislike URLs
    path(
        "post/<int:post_id>/like-dislike/",
        views.toggle_like_dislike,
        name="toggle_like_dislike",
    ),
    # Subscription URLs
    path("subscribe/", views.subscribe, name="subscribe"),
    # Advertisement URLs
    path(
        "ad/<int:ad_id>/click/", views.advertisement_click, name="advertisement_click"
    ),
    # Tag Filtering
    path("tag/<str:tag_name>/", views.tag_posts, name="tag_posts"),
    # Admin Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
]
