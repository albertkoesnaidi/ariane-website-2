from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePage(TemplateView):
    template_name = 'web/index.html'

class AboutPage(TemplateView):
    template_name = 'web/about.html'

class ProjectPage(TemplateView):
    template_name = "web/project.html"

class ProductPage(TemplateView):
    template_name = 'web/product.html'

class SwhPage(TemplateView):
    template_name = "web/swh.html"

class HeatpumpPage(TemplateView):
    template_name = "web/heatpump.html"

class PumpPage(TemplateView):
    template_name = 'web/pump.html'

class PartnerPage(TemplateView):
    template_name = 'web/partner.html'

class ArtikelPage(TemplateView):
    template_name = 'web/artikel-swh.html'

class ArtikelPageSwh1(TemplateView):
    template_name = 'web/artikel-swh-1.html'

    

