from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    
    def setUp(self) -> None:
        self.data = {
            'name': 'John Jones',
            'email': 'jones@gmail.com',
            'subject': 'A random subject',
            'message': 'Any message'
        }

        self.client = Client()

        return super().setUp()

    def test_form_valid(self):
        req = self.client.post(reverse_lazy('index'), data=self.data)
        self.assertEquals(req.status_code, 302)

    def test_form_invalid(self):
        invalid_data = {
            'name': 'John Jones',
            'subject': 'A random subject',
        }

        req = self.client.post(reverse_lazy('index'), data=invalid_data)
        self.assertEquals(req.status_code, 200)
        