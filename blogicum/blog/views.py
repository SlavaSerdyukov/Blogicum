from django.shortcuts import get_object_or_404, render

from blog.constants import POSTS_ON_PAGE
from blog.models import Category
from blog.utils import queryset_posts


def index(request):
    template = 'blog/index.html'
    published_posts = queryset_posts()[:POSTS_ON_PAGE]
    context = {'post_list': published_posts}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        queryset_posts(), pk=post_id)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects,
        is_published=True,
        slug=category_slug
    )
    context = {'category': category, 'post_list': queryset_posts().filter(
        category=category)}
    return render(request, template, context)
