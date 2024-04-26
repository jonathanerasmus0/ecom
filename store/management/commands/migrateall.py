from typing import Any
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help ='Runs makemigrations and migrate in one command'




    def handle(self, *args: Any, **options: Any) -> str | None:
        
        call_command('makemigrations')

        call_command('migrate')


