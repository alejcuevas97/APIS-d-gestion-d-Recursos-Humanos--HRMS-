from decimal import Decimal

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from apps.employees.models import Empleado
from .models import Nomina


class NominaModelTest(TestCase):
    def test_salario_neto_property(self):
        empleado = Empleado.objects.create(
            nombre="Laura",
            apellidos="Fernández",
            edad=38,
            puesto="Contador",
            salario="2200",
            fecha_contratacion="2022-11-12"
        )
        nomina = Nomina.objects.create(
            empleado=empleado,
            periodo_inicio="2024-04-01",
            periodo_fin="2024-04-30",
            salario_base=Decimal("2000.00"),
            deducciones=Decimal("200.00"),
            bonificaciones=Decimal("150.00"),
            fecha_pago="2024-05-05"
        )
        self.assertEqual(
            nomina.salario_neto,
            nomina.salario_base - nomina.deducciones + nomina.bonificaciones
        )


class NominaAPITest(APITestCase):
    def setUp(self):
        self.empleado = Empleado.objects.create(
            nombre="Diego",
            apellidos="Ortiz",
            edad=33,
            puesto="Auxiliar",
            salario="1200",
            fecha_contratacion="2024-02-01"
        )

    def test_create_nomina(self):
        url = "/api/v1/nomina/"
        payload = {
            "empleado": self.empleado.id,
            "periodo_inicio": "2024-04-01",
            "periodo_fin": "2024-04-30",
            "salario_base": "1800.00",
            "deducciones": "100.00",
            "bonificaciones": "120.00",
            "fecha_pago": "2024-05-05"
        }

        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["empleado"], self.empleado.id)
        self.assertEqual(Decimal(response.data["salario_neto"]), Decimal("1820.00"))

    def test_list_nomina(self):
        Nomina.objects.create(
            empleado=self.empleado,
            periodo_inicio="2024-04-01",
            periodo_fin="2024-04-30",
            salario_base="1800.00",
            deducciones="100.00",
            bonificaciones="120.00",
            fecha_pago="2024-05-05"
        )

        response = self.client.get("/api/v1/nomina/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
