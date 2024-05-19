from django import forms

class ClientLoginForm(forms.Form):
    username = forms.CharField(label="Wallet Address")
    password = forms.CharField(label="Secret Code")

class ClientWalletForm(forms.Form):
    send_coins = forms.CharField(label="send_coins")
    recieve_address = forms.CharField(label="recieve_address")
    
