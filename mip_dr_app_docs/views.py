from django.views.generic import TemplateView


class NotesView(TemplateView):
    template_name = "mip_dr_app_docs/notes.html"


class APIView(TemplateView):
    template_name = "mip_dr_app_docs/api_docs.html"
