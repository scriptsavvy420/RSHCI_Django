from django.db import models



class Wallet(models.Model):
    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallet'

    # owner = models.ForeignKey(CoinUsers,related_name='wallet_username',default='', on_delete=models.CASCADE)
    owner = models.CharField(max_length=100,verbose_name='Owner')
    address = models.CharField(max_length=255,verbose_name='Address', default='')
    secretcode = models.CharField(max_length=255,verbose_name='SecretCode', default='')
    coinamount = models.CharField(max_length=255,verbose_name='CoinAmount', default='')

    def __str__(self):
        return self.owner
    
class CoinUsers(models.Model):
    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    name = models.CharField(max_length=100,verbose_name='Name',default='')
    email = models.CharField(max_length=100,verbose_name='Email', default='')
    phone = models.CharField(max_length=100,verbose_name='Phone Number', default='')
    wallet_info = models.ManyToManyField(Wallet,related_name='owners', default='')


    def __str__(self):
        return self.name




    

