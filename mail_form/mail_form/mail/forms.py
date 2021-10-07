from django import forms


class Credentials(forms.Form):
    name = forms.CharField(
        label='Введите ваше имя',
        max_length=35,
        )
    email = forms.EmailField(
        empty_value='example@mail.com',
        )
    message_text = forms.CharField(
        max_length=10000,
        label='Текст сообщения'
        )
    personal_data = forms.BooleanField(label='Согласие на обработку ПД')



