
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from homepage.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.init_superuser()
        self.init_coin()
        


    def init_superuser(self):
        try:
            User.objects.all().delete()

            user = User.objects.create_superuser("rshci_wallet", "support@rshci.com", "password")
           
            User.objects.create_superuser("yoshida", "yoshidadaisuke0420@gmail.com", "password")
            
            
            print("Superuser created successfully.")
        except Exception as error:
            print(str(error))
    def init_coin(self):
        try:
            CoinPrice.objects.all().delete()

            CoinPrice.objects.create(coinprice=2.22)
            print("CoinPrice created successfully.")
        except Exception as error:
            print(str(error))
   

    