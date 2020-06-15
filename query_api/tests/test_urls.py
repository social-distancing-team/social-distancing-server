from django.test import SimpleTestCase
from django.urls import resolve, reverse
from query_api import views

class TestUrls(SimpleTestCase):
    def test_query_chats_url(self):
        url = reverse("api-query-chats")
        self.assertEquals(resolve(url).func, views.query_chats)

    def test_query_lists_url(self):
        url = reverse("api-query-lists")
        self.assertEquals(resolve(url).func, views.query_lists)

    def test_query_users_url(self):
        url = reverse("api-query-users")
        self.assertEquals(resolve(url).func, views.query_users)
