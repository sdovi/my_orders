from django import forms


class PhoneForm(forms.Form):
    phone = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    send_type = forms.CharField(max_length=20)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone = phone.strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        return phone
