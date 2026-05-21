from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from apps.employees.models import Empleado
from .models import Departamento


class DepartamentoModelTest(TestCase):
    def test_str_representation(self):
        departamento = Departamento.objects.create(
            nombre="Recursos Humanos",
            descripcion="Gestión del personal"
        )
        self.assertEqual(str(departamento), "Recursos Humanos")


class DepartamentoAPITest(APITestCase):
    def setUp(self):
        self.gerente = Empleado.objects.create(
            nombre="María",
            apellidos="López",
            edad=40,
            puesto="Gerente",
            salario="3000",
            fecha_contratacion="2022-01-10"
        )

    def test_create_departamento_with_gerente(self):
        url = "/api/v1/departamentos/"
        payload = {
            "nombre": "Finanzas",
            "descripcion": "Departamento de contabilidad",
            "gerente": self.gerente.id
        }

        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nombre"], payload["nombre"])
        self.assertEqual(response.data["gerente"], self.gerente.id)

    def test_list_departamentos(self):
        Departamento.objects.create(nombre="Ventas", descripcion="Equipo de ventas")

        response = self.client.get("/api/v1/departamentos/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
