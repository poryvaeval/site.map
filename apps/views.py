from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
class Map(TemplateView):
    template_name = 'map.html'
class Str1762(TemplateView):
    template_name = 'revision1762.html'
class Str1801(TemplateView):
    template_name = 'metric1801.html'
class Str1802(TemplateView):
    template_name = 'metric1802.html'
class Str1710R(TemplateView):
    template_name = 'rev1710Re.html'
class Str1710Sk(TemplateView):
    template_name = 'rev1710Sk.html'
class Str1710Si(TemplateView):
    template_name = 'rev1710Si.html'
class Str1710Me(TemplateView):
    template_name = 'rev1710Me.html'
class Str1710Os(TemplateView):
    template_name = 'rev1710Os.html'

# Create your views here.
