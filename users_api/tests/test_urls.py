from django.test import SimpleTestCase
from django.urls import resolve, reverse
from users_api.views import list_users

class TestUrls(SimpleTestCase):
    def test_users_list_url(self):
        url = reverse("api-users-list")
        self.assertEquals(resolve(url).func, list_users)
