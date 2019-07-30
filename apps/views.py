from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
class Map(TemplateView):
    template_name = 'map.html'

# Create your views here.
