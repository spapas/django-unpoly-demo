from django import template

register = template.Library()


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
        if not rendered.startswith("<p"):
            rendered = "<p>{}</p>".format(rendered)
        
        rendered +="""
        <p>
            <a href="#" up-dismiss class="btn btn-success btn-sm">OK</a>
        </p>
        """
        from django.utils.html import escape

        output = escape(rendered)
        # a+=1
        return """
        <a 
            href="#" 
            class="tour-dot"
            up-layer="new popup"
            up-content="{}"
            up-position="right"
            up-align="top"
            up-class="tour-hint"
            up-size="medium"
            >
        </a>
        """.format(output)
