from django import template

register = template.Library()

@register.filter
def is_favorited_by(post, user):
    if user.is_authenticated:
        return post.favorites.filter(id=user.id).exists()
    return False