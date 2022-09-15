from django import template

register = template.Library()


@register.filter(name='plurals_comments')
def plural_comments(comments_numbers):
    try:
        comments_numbers = int(comments_numbers)
        if comments_numbers == 0:
            return f'Nenhum Comentário'
        elif comments_numbers == 1:
            return f'{comments_numbers} Comentário'
        else:
            return f'{comments_numbers} Comentários'
    except:
        return f'{comments_numbers} Comentário(s)'


@register.filter(name='hasuser')
def hasuser(user):
    if not user:
        return f'Anônimo'
    else:
        return f'{user}'.capitalize()
