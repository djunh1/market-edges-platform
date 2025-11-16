from django.urls import path
from . import views


urlpatterns = [
    path('', views.portfolios, name="portfolios"),
    path('portfolio/<str:pk>/', views.portfolio, name="portfolio"),
    path('create-portfolio/', views.createPortfolio, name="create-portfolio"),
    path('add-stock/<str:pk>/', views.addStock, name="add-stock"),
    path('remove-stock/', views.deleteStock, name="remove-stock"),
    path('update-portfolio/<str:pk>/', views.updatePortfolio, name='update-portfolio'),
    path('delete-portfolio/<str:pk>/', views.deletePortfolio, name="delete-portfolio"),
    path('delete-stock/<str:pk>/', views.deleteStock, name="delete-stock"),
]
