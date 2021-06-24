import uuid

from django.db import models
from django.contrib.auth.models import User
from .constants import SEX_CHOICES, SEX_UNKNOWN


class Facility(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField('Telefon', max_length=25)
    email = models.CharField('Email', max_length=100)
    city = models.CharField('Miasto', max_length=100)
    street = models.CharField('Ulica', max_length=100)
    country = models.CharField('Kraj', max_length=100)
    postal_code = models.CharField('Kod pocztowy', max_length=10)


class Patient(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    name = models.CharField('imię', max_length=100)
    second_name = models.CharField('drugie imię', max_length=100, default='', blank=True)
    surname = models.CharField('nazwisko', max_length=100)
    sex = models.CharField('Płeć', choices=SEX_CHOICES, default=SEX_UNKNOWN, max_length=100)
    telephone = models.CharField('Telefon', max_length=25)
    email = models.CharField('Email', max_length=100, blank=True)
    city = models.CharField('Miasto', max_length=100)
    street = models.CharField('Ulica', max_length=100)
    country = models.CharField('Kraj', max_length=100)
    postal_code = models.CharField('Kod pocztowy', max_length=10)
    pesel = models.CharField('pesel', max_length=11)

    def __str__(self):
        return self.name + ' ' + self.surname + ' (' + self.pesel + ')'


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    name = models.CharField('imię', max_length=100)
    second_name = models.CharField('drugie imię', max_length=100, default='', blank=True)
    surname = models.CharField('nazwisko', max_length=100)
    telephone = models.CharField('Telefon', max_length=25, blank=True)
    pwz = models.CharField('PWZ', max_length=20)
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)

    def __str__(self):
        return self.name + ' ' + self.surname + ' (' + self.pwz + ')'


class Visit(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.date) + ' (' + str(self.start_time) + ':' + str(self.end_time) + ')'


class Tooth(models.Model):
    class Horizontally(models.TextChoices):
        top = "top", "Górny"
        bottom = "bottom", "Dolny"

    class Vertically(models.TextChoices):
        left = "left", "Lewy"
        right = "right", "Prawy"

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="teeth")
    number = models.PositiveIntegerField()
    horizontally = models.CharField(max_length=16, choices=Horizontally.choices)
    vertically = models.CharField(max_length=16, choices=Vertically.choices)
    note = models.TextField(blank=True)


class PatientNote(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="notes")
    title = models.TextField()
    note = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
