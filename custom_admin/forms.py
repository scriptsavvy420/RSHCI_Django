from django import forms

class AdminLoginForm(forms.Form):
    username = forms.CharField(label="Wallet Address")
    password = forms.CharField(label="Secret Code")


class CreateWalletForm(forms.Form):
    name = forms.CharField(label="username")
    email = forms.CharField(label="useremail")


class UpdateWalletForm(forms.Form):
    name = forms.CharField(label="username")
    email = forms.CharField(label="useremail")
    coins = forms.DecimalField(label="coins")
    username = forms.CharField(label="walletaddress")
    secretcode = forms.CharField(label="secretcode")

class SetPriceForm(forms.Form):
    coinprice = forms.DecimalField(label="coin_price")