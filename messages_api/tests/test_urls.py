from django.test import SimpleTestCase
from django.urls import resolve, reverse
from messages_api.views import list_messages

class TestUrls(SimpleTestCase):
    def test_messages_list_url(self):
        url = reverse("api-messages-list")
        self.assertEquals(resolve(url).func, list_messages)
