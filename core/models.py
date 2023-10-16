import uuid
from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Gear'),
        ('lni-stats-up', 'Graph'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )

    service = models.CharField('Service', max_length=100)
    description = models.TextField('Description', max_length=250)
    icon = models.CharField('Icon', max_length=20, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self) -> str:
        return self.service


class Role(Base):
    role = models.CharField('Role', max_length=100)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self) -> str:
        return self.role
         

class Employee(Base):
    name = models.CharField('Name', max_length=100)
    role = models.ForeignKey('core.Role', verbose_name='Role', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=450)
    image = StdImageField('Image', upload_to=get_file_path, variations={ 'thumbnail': { 'width': 400, 'height': 480 } }) # type: ignore
    facebook = models.CharField('Facebook', max_length=150, default='#')
    twitter = models.CharField('Twitter', max_length=150, default='#')
    Instagram = models.CharField('Instagram', max_length=150, default='#')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self) -> str:
        return self.name