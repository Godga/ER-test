from django import forms
from ER_test_app.models import UserProfile, DataAboutSending, NumberPacket
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control'}), required=True, max_length=128, min_length=5, help_text="", label="")
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control'}), required=True, max_length=128, min_length=5, label="")
	username = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control'}), min_length=3, required=True, help_text="", label="")
	email = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control'}), min_length=3, help_text="", label="")
	class Meta:
		model = User
		fields = {"username", "email", "password"}


class UserProfileForm(forms.ModelForm):
	website = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control'}), help_text="", label="", required=False)
	avatar = forms.FileField(widget=forms.FileInput(), required=False, help_text="", label="")
	class Meta:
		model = UserProfile
		fields = {'website', 'avatar'}


class DataAboutSendingForm(forms.ModelForm):
	message_text = forms.CharField(widget=forms.Textarea(\
		attrs={"class": "tabs_textarea", "rows": "7", "placeholder": "Сообщение для рассылки"}),\
		help_text="", label="",	required=False
		)
	message_file = forms.FileField(widget=forms.FileInput(\
		attrs={"class": "file_input", "placeholder": "mp3 файл с записью рассылки"}),\
		required=False, help_text="", label=""\
		)

	def clean(self):
		cleaned_data = super().clean()
		message_text = cleaned_data.get("message_text")
		message_file = cleaned_data.get("message_file")
		if not(message_file or message_text):
			raise forms.ValidationError("Введите или загрузите сообщение")

	class Meta:
		model = DataAboutSending
		fields = {}


class NumberPacketForm(forms.ModelForm):
	packet_name = forms.CharField(widget=forms.TextInput(\
		attrs={"class": 'tabs_input', "placeholder": "Название базы"}),\
		help_text="", label="", required=False)
	numbers_text = forms.CharField(widget=forms.Textarea(\
		attrs={"class": "tabs_textarea", "rows": "7", "placeholder": "Номера для рассылки (каждый в отдельной строке)"}),\
		help_text="", label="",	required=False
		)
	numbers_file = forms.FileField(\
		widget=forms.FileInput(attrs={"class": "file_input", "placeholder": "csv файл с базой для рассылки"}),\
		required=False, help_text="", label=""\
		)

	def clean(self):
		cleaned_data = super().clean()
		numbers_text = cleaned_data.get("numbers_text")
		numbers_file = cleaned_data.get("numbers_file")
		packet_name = cleaned_data.get("packet_name")

	class Meta:
		model = NumberPacket
		fields = {}


