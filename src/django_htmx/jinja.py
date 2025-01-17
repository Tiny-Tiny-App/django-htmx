from django.conf import settings
from django.templatetags.static import static
from django.utils.html import format_html


def django_htmx_script():
    # Optimization: whilst the script has no behaviour outside of debug mode,
    # don't include it.
    if not settings.DEBUG:
        return format_html("")
    return format_html(
        '<script type="text/javascript" src="{}" data-debug="{}" async defer></script>',
        static("django-htmx.js"),
        str(bool(settings.DEBUG)),
    )
