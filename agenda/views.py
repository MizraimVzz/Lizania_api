from rest_framework import generics
from .models import Evento
from .serializers import EventoSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta

class EventoLista(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Validar la hora del evento
            hora_evento = serializer.validated_data['horario']
            if not self.validar_horario(hora_evento):
                return Response({"error": "El evento debe estar dentro del horario permitido (6:00 am - 11:00 pm)."}, status=status.HTTP_400_BAD_REQUEST)

            # Validar la diferencia de tiempo entre eventos
            fecha_evento = serializer.validated_data['fecha']
            if not self.validar_diferencia_tiempo(fecha_evento, hora_evento):
                return Response({"error": "Debe haber al menos 3 horas de diferencia entre eventos en el mismo día."},
                                status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def validar_horario(self, hora_evento):
        # Verificar que la hora del evento esté entre las 6:00 am y las 11:00 pm
        hora_inicio = datetime.strptime("06:00", "%H:%M").time()
        hora_fin = datetime.strptime("23:00", "%H:%M").time()
        return hora_inicio <= hora_evento <= hora_fin

    def validar_diferencia_tiempo(self, fecha_evento, hora_evento):
        # Obtener la fecha y hora actual
        ahora = datetime.now()

        # Combinar la fecha y hora del evento
        fecha_hora_evento = datetime.combine(fecha_evento, hora_evento)

        # Obtener todos los eventos para el día seleccionado
        eventos_en_el_dia = Evento.objects.filter(fecha=fecha_evento)

        for evento_existente in eventos_en_el_dia:
            # Combinar la fecha y hora del evento existente
            fecha_hora_existente = datetime.combine(evento_existente.fecha, evento_existente.horario)

            # Calcular la diferencia de tiempo total en minutos
            diferencia_total = abs((fecha_hora_evento - fecha_hora_existente).total_seconds() / 60)

            # Verificar si hay eventos cercanos antes o después del evento que se está creando
            if 0 < diferencia_total < 180:  # Menos de 3 horas de diferencia
                return False

        # Si no hay eventos cercanos antes o después, se cumple la validación
        return True

class EventoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer