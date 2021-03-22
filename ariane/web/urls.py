from django.urls import path, include
from web import views

app_name='web'

urlpatterns=[
    path('',views.HomePage.as_view(), name='home'),
    path('about/',views.AboutPage.as_view(), name='about'),
    path('project/', views.ProjectPage.as_view(),name='project'),
    path('products/', views.ProductPage.as_view(),name='product'),
    path('products/solar-series/', views.SwhPage.as_view(), name="swh"),
    path('products/heatpump-series/', views.HeatpumpPage.as_view(), name="heatpump"),
    path('products/pump-filter/', views.PumpPage.as_view(), name="pump"),
    path('our-partners/', views.PartnerPage.as_view(), name="partner"),
    path('artikel/', views.ArtikelPage.as_view(), name="artikel-swh"),
    path('artikel/swh-1/', views.ArtikelPageSwh1.as_view(), name="artikel-swh-1"),
]