from django.views.generic.base import RedirectView


class HomeView(RedirectView):
    pattern_name = "vocab:index"
