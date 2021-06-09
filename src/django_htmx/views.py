from django.views.generic.edit import FormView
from django_htmx.mixins import HtmxTemplateResponseMixin


class HtmxFormView(HtmxTemplateResponseMixin, FormView):
    """A view for displaying a form and rendering a htmx or regular template response."""
