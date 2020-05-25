from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class TestViews(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user="Zydn9ZG77ydUeNorHRBllmdFlf73")

    def test_messages_list(self):
        response = self.client.get("/api/messages/list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
