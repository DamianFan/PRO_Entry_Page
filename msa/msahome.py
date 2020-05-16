from django.views.generic.base import TemplateView


class MsaHomeView(TemplateView):
    template_name = 'msa/index.html'