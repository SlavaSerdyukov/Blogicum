from datetime import datetime

from blog.models import Post


def queryset_posts():
    return Post.objects.select_related(
        'category', 'author', 'location').filter(
            pub_date__lte=datetime.now(),
            category__is_published=True,
            is_published=True,
    )
