from suit.apps import DjangoSuitConfig
from django.apps import AppConfig


class CollegeAppConfig(AppConfig):
    name = 'collegeApp'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
