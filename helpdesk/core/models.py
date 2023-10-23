from django.db import models
import uuid
# Create your models here.

class Speciality(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID Especialidad")
    name = models.CharField(max_length=255, verbose_name="Nombre Especialidad")

    def __str__(self) -> str:
        return self.name

    def create(self, name):
        self.name = name
        self.save()

    def update(self, id, name):
        self.id = id
        self.name = name
        self.save()

    def delete(self, id):
        self.id = id
        self.delete()

class Tech(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID Tech")
    name = models.CharField(max_length=255, verbose_name="Nombre Tech")
    last_name = models.CharField(max_length=255)
    speciality = models.ManyToManyField(
        Speciality, related_name="techs" 
    ) ###############

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def assign_ticket(self, ticket):
        ticket.tech = self
        ticket.save()

    def resolve_ticket(self):
        pass

    def create(self, name, last_name, speciality):
        self.name = name
        self.last_name = last_name
        self.speciality.add(*speciality) ######################
        self.save()


class Criticy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID Criticy")
    level = models.CharField(max_length=255, verbose_name="Level Criticy")

    def __str__(self):
        return self.level

    def create(self, level):
        self.level = level
        self.save()

from django.db import models


class TicketHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID Ticket History")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro en el historial")
    description = models.TextField(default="", verbose_name="Descripción del cambio")

    def __str__(self):
        return self.description

    def add_entry(self, description):
        self.description = description
        self.save()


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID Ticket")
    title = models.CharField(max_length=255, verbose_name="Titulo Ticket")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    criticy = models.ForeignKey(
        Criticy, on_delete=models.CASCADE, related_name="tickets"
    )
    tech = models.ForeignKey(
        Tech, on_delete=models.SET_NULL, related_name="tickets", null=True
    )
    history = models.OneToOneField(
        TicketHistory, on_delete=models.CASCADE, related_name="ticket"
    )
    status = models.CharField(max_length=255, default="open")

    def __str__(self):
        return self.title

    def create(self, title, description, criticy, tech):
        self.title = title
        self.description = description
        self.criticy = criticy
        self.tech = tech
        self.status = "open"
        self.save()

    def close_ticket(self):
        self.status = "closed"
        self.save()




