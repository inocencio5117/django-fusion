from django.test import TestCase

from core.forms import ContactForm


class ContactFormTestCase(TestCase):
    
    def setUp(self) -> None:
        self.name = 'John Jones'
        self.email = 'jones@gmail.com'
        self.subject = 'A random subject'
        self.message = 'Any message'

        self.data = {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message
        }

        self.form = ContactForm(data=self.data)

        return super().setUp()

    def test_send_mail(self):
        form1 = ContactForm(data=self.data)
        form1.is_valid()
        result1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        result2 = form2.send_mail()

        self.assertEquals(result1, result2)