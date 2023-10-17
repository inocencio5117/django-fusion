import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):
    
    def setUp(self) -> None:
        self.filename = f'{uuid.uuid4()}.png'
        return super().setUp()

    def test_get_file_path(self):
        archive = get_file_path(None, 'test.png')
        self.assertTrue(len(archive), len(self.filename))


class ServiceTestCase(TestCase):
    
    def setUp(self) -> None:
        self.service = mommy.make('Service')
        return super().setUp()
    
    def test_str(self):
        self.assertEquals(str(self.service), self.service.service) # type: ignore


class RoleTestCase(TestCase):
    
    def setUp(self) -> None:
        self.role = mommy.make('Role')
        return super().setUp()
    
    def test_str(self):
        self.assertEquals(str(self.role), self.role.role) # type: ignore

        
class EmployeeTestCase(TestCase):
    
    def setUp(self) -> None:
        self.employee = mommy.make('Employee')
        return super().setUp()
    
    def test_str(self):
        self.assertEquals(str(self.employee), self.employee.name) # type: ignore