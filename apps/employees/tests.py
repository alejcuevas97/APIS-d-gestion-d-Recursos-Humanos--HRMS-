from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Empleado


class EmpleadoModelTest(TestCase):
    def test_str_representation(self):
        empleado = Empleado.objects.create(
            nombre="Juan",
            apellidos="Pérez",
            edad=30,
            puesto="Developer",
            salario="1200",
            fecha_contratacion="2024-01-01"
        )
        self.assertEqual(str(empleado), "Juan Pérez")


class EmpleadoAPITest(APITestCase):
    def test_create_and_retrieve_empleado(self):
        url = "/api/v1/empleados/"
        payload = {
            "nombre": "Ana",
            "apellidos": "Gómez",
            "edad": 28,
            "puesto": "Analista",
            "salario": "1500",
            "fecha_contratacion": "2024-04-01"
        }

        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        empleado_id = response.data["id"]

        response = self.client.get(f"{url}{empleado_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nombre"], payload["nombre"])
        self.assertEqual(response.data["apellidos"], payload["apellidos"])

    def test_list_empleados(self):
        Empleado.objects.create(
            nombre="Luis",
            apellidos="Ramírez",
            edad=35,
            puesto="Jefe",
            salario="2500",
            fecha_contratacion="2023-08-15"
        )

        response = self.client.get("/api/v1/empleados/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
