from django.views.generic import TemplateView


class APIView(TemplateView):
    template_name = "mip_dr_app_docs/api_docs.html"


class ERDView(TemplateView):
    template_name = "mip_dr_app_docs/erd.html"


class NotesView(TemplateView):
    template_name = "mip_dr_app_docs/notes.html"
