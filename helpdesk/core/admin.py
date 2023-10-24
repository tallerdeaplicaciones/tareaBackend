from django.contrib import admin
from .models import Speciality, Tech, Ticket, TicketHistory, Criticy, Status
# Register your models here.


admin.site.register(Speciality)

admin.site.register(Tech)

admin.site.register(Ticket)

admin.site.register(TicketHistory)

admin.site.register(Criticy)

admin.site.register(Status)