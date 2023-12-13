from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    horario = models.TimeField()
    calle = models.CharField(max_length=255, default=' ')
    numero = models.CharField(max_length=255, default=' ')
    colonia = models.CharField(max_length=255, default=' ')
    municipio = models.CharField(max_length=255, default=' ')
    estado = models.CharField(max_length=255, default=' ')
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        super().clean()
        self.validar_eventos_cercanos()
        self.validar_horario()

    def validar_eventos_cercanos(self):
        limite_tiempo = timezone.datetime.combine(self.fecha, self.horario) + timezone.timedelta(hours=3)
        eventos_cercanos = Evento.objects.filter(
            fecha__gte=self.fecha,
            horario__gte=self.horario,
            fecha__lte=limite_tiempo.date(),
            horario__lte=limite_tiempo.time(),
        ).exclude(pk=self.pk)
        if eventos_cercanos.exists():
            raise ValidationError("Ya hay un evento cercano en ese horario.")

    def validar_horario(self):
        hora_limite_inferior = timezone.make_aware(timezone.datetime.combine(self.fecha, timezone.datetime.min.time()) + timezone.timedelta(hours=6))
        hora_limite_superior = timezone.make_aware(timezone.datetime.combine(self.fecha, timezone.datetime.min.time()) + timezone.timedelta(hours=23))

        if not hora_limite_inferior <= timezone.make_aware(timezone.datetime.combine(self.fecha, self.horario)) <= hora_limite_superior:
            raise ValidationError("El evento debe estar programado entre las 6:00 am y las 11:00 pm.")