import django_tables2 as tables
from django_tables2.utils import A
from . import models


class CompanyTable(tables.Table):
    id = tables.LinkColumn(
        "company-detail",
        args=[A("id")],
        attrs={
            "a": {
                "class": "btn btn-primary btn-sm",
                "up-on-dismissed": "up.reload('.table', { focus: ':main' })",
                "up-layer": "new",
            }
        },
    )

    class Meta:
        model = models.Company
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "name", "address")
