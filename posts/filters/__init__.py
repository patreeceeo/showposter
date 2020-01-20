from django import template
import markdown

register = template.Library()

@register.filter(name='markdown', is_safe=True, needs_autoescape=False)
def markdown_filter(value):
    return markdown.markdown(value, output_format="html5")
