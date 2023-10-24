from django.contrib import admin
from django.urls import path
from core.views import Home, TicketCreateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(), name='home'),
    path('crearTicket/', TicketCreateView.as_view(), name='add_ticket'),
]
