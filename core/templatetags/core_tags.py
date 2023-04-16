from django import template
from django.utils.html import strip_tags

register = template.Library()


@register.simple_tag(takes_context=True)
def fragment_explainer(context):
    view = context["view"]
    template_name = view.get_template_names()[0]
    return {
        "view": view.__class__.__name__,
        "view_code": "https://github.com/spapas/django-unpoly-demo/blob/master/core/views.py",
        "template": template_name,
        "template_code": "https://github.com/spapas/django-unpoly-demo/tree/master/core/templates/{}".format(
            template_name
        ),
    }


@register.tag("tourdot")
def do_tourdot(parser, token):
    nodelist = parser.parse(("endtourdot",))
    parser.delete_first_token()
    return TourDotNode(nodelist)


class TourDotNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        rendered = self.nodelist.render(context).strip()
        size = "medium"
        if len(strip_tags(rendered)) > 400:
            size = "large"
        if not rendered.startswith("<p"):
            rendered = "<p>{}</p>".format(rendered)

        rendered += """
        <p>
            <a href="#" up-dismiss class="btn btn-success btn-sm">OK</a>
        </p>
        """
        from django.utils.html import escape

        output = escape(rendered)
        return """
        <a 
            href="#" 
            class="tour-dot"
            up-layer="new popup"
            up-content="{}"
            up-position="right"
            up-align="top"
            up-class="tour-hint"
            up-size="{}"
            >
        </a>
        """.format(
            output, size
        )


@register.simple_tag
def urlid(path, arg):
    from django.urls import reverse
    if arg == "$id":
        arg = 999
    
    url = reverse(path, args=[arg])
    return url.replace("999", "$id")