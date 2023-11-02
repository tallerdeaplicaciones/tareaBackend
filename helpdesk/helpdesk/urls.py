from django.contrib import admin
from django.urls import path
from core.views import Home, TicketCreateView, TechCreateView, TicketUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(), name='home'),
    path('crearTicket/', TicketCreateView.as_view(), name='add_ticket'),
    path('editarTicket/<int:id>', TicketUpdateView.as_view(), name='update_ticket'),
    path('crearTecnico/', TechCreateView.as_view(), name='add_tech')
]
