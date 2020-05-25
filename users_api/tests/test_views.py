from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class TestUsersViews(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user="Zydn9ZG77ydUeNorHRBllmdFlf73")

    def test_users_list(self):
        response = self.client.get("/api/users/list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_get_user(self):
        pass
