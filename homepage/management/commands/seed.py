
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from homepage.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.init_superuser()
        


    def init_superuser(self):
        try:
            User.objects.all().delete()

            User.objects.create_superuser("rshci_wallet", "support@rshci.com", "password")
            User.objects.create_superuser("yoshida", "yoshidadaisuke0420@gmail.com", "password")
            
            
            print("Superuser created successfully.")
        except Exception as error:
            print(str(error))

   

    