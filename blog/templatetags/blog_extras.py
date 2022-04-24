from django.contrib.auth import get_user_model
user_model = get_user_model()


def author_details(author):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)

@register.simple_tag
def row():
  return format_html('<div class="row">')
  
@register.simple_tag
def endrow():
  return format_html("</div>")
