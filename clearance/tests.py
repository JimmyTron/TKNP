from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class RequestTest(TestCase):
    def test_request(self):
        response = self.client.post(reverse('request'), {'title': 'title', 'description': 'description', 'departments': [1, 2]})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('request'))
        self.assertEqual(Request.objects.count(), 1)
        self.assertEqual(Notification.objects.count(), 2)