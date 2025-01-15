from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, LikeDislike, Tag, Subscriber, Advertisement, PageView
from .forms import PostForm, CommentForm, SubscriptionForm
from .utils.timezone import now

# Blog Views
def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')

    # Track Page View
    if request.META.get('REMOTE_ADDR'):
        PageView.objects.create(post=post, visitor_ip=request.META['REMOTE_ADDR'])

    comments = post.comments.filter(moderation_status='approved')
    comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # Save tags
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    post.delete()
    return redirect('post_list')

# Comment Views
@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
    return redirect('post_detail', slug=post.slug)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    post_slug = comment.post.slug
    comment.delete()
    return redirect('post_detail', slug=post_slug)

# Like/Dislike Views
@login_required
def toggle_like_dislike(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    interaction_type = request.POST.get('interaction_type')
    if interaction_type not in ['like', 'dislike']:
        return JsonResponse({'error': 'Invalid interaction type'}, status=400)

    like_dislike, created = LikeDislike.objects.get_or_create(user=request.user, post=post)
    if not created and like_dislike.interaction_type == interaction_type:
        like_dislike.delete()  # Toggle off
    else:
        like_dislike.interaction_type = interaction_type
        like_dislike.save()

    return JsonResponse({'status': 'success'})

# Subscription Views
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

# Advertisement Views
def advertisement_click(request, ad_id):
    ad = get_object_or_404(Advertisement, id=ad_id)
    ad.clicks += 1
    ad.save()
    return JsonResponse({'status': 'success'})

# Utility Views
def tag_posts(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = tag.posts.filter(status='published')
    return render(request, 'blog/tag_posts.html', {'tag': tag, 'posts': posts})

# Dashboard (Admin Panel)
@login_required
def dashboard(request):
    if not request.user.is_staff:
        return redirect('post_list')
    return render(request, 'blog/dashboard.html', {
        'post_count': Post.objects.count(),
        'comment_count': Comment.objects.count(),
        'subscriber_count': Subscriber.objects.count(),
        'page_view_count': PageView.objects.count(),
    })
