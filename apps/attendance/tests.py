from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from apps.employees.models import Empleado
from .models import Asistencia


class AsistenciaModelTest(TestCase):
    def test_str_representation(self):
        empleado = Empleado.objects.create(
            nombre="Pedro",
            apellidos="Méndez",
            edad=32,
            puesto="Operario",
            salario="900",
            fecha_contratacion="2023-05-20"
        )
        asistencia = Asistencia.objects.create(
            empleado=empleado,
            fecha="2024-05-01",
            hora_entrada="08:00:00",
            hora_salida="17:00:00"
        )
        self.assertEqual(str(asistencia), f"{empleado}-{asistencia.fecha}")


class AsistenciaAPITest(APITestCase):
    def setUp(self):
        self.empleado = Empleado.objects.create(
            nombre="Carlos",
            apellidos="Suárez",
            edad=29,
            puesto="Secretario",
            salario="1100",
            fecha_contratacion="2024-01-20"
        )

    def test_create_asistencia(self):
        url = "/api/v1/asistencia/"
        payload = {
            "empleado": self.empleado.id,
            "fecha": "2024-05-12",
            "hora_entrada": "09:00:00",
            "hora_salida": "18:00:00"
        }

        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["empleado"], self.empleado.id)

    def test_list_asistencia(self):
        Asistencia.objects.create(
            empleado=self.empleado,
            fecha="2024-05-01",
            hora_entrada="08:30:00",
            hora_salida="17:30:00"
        )

        response = self.client.get("/api/v1/asistencia/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
