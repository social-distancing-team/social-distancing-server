from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class TestQueryViews(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user="Zydn9ZG77ydUeNorHRBllmdFlf73")

    def test_query_chats(self):
        response = self.client.get("/api/query/chats/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_query_lists(self):
        response = self.client.get("/api/query/lists/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_query_users(self):
        response = self.client.get("/api/query/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
