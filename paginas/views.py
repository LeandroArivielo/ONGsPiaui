from django.views.generic import TemplateView

# Create your views here.
class TrabalhoPageView(TemplateView):
    template_name = 'trabalho.html'

class ListadeEventosPageView(TemplateView):
    template_name = 'ListadeEventos.html'

class ONGsDeAnimaisPageView(TemplateView):
    template_name = 'ONGsDeAnimais.html'

class ONGsDeAnimaisPedroIIPageView(TemplateView):
    template_name = 'ONGsDeAnimaisPedroII.html'

class oqEPageView(TemplateView):
    template_name = 'oqE.html'

class voluntariadoPageView(TemplateView):
    template_name = 'voluntariado.html'