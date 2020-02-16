from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from ER_test_app.models import User, UserProfile, DataAboutSending
from ER_test_app.forms import UserForm, UserProfileForm, DataAboutSendingForm, NumberPacketForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
import time
import csv
import os


app_name = "ER_test_app"

def csv_reader(file_obj):
	reader = csv.reader(file_obj)
	output = ""
	for row in reader:
		output = output + row + "\n"
	return output

def index(request):
	if request.user.is_authenticated:
		name = request.user
		try:
			current_user = UserProfile.objects.get(user=name)
		except:
			current_user = "admin"
		if request.method == 'POST':
			sending_form = DataAboutSendingForm(request.POST, request.FILES)
			packet_form = NumberPacketForm(request.POST, request.FILES)
			if sending_form.is_valid() and packet_form.is_valid():
				sending_model = sending_form.save(commit=False)
				# проверка - сообщение отправлено файлом или текстом
				if 'message_file' in request.FILES:
					message_file = request.FILES['message_file']
					# обработка mp3
				else:
					sending_model.message = sending_form.cleaned_data['message_text']

				numbers_model = packet_form.save(commit=False)
				# проверка - база контактов отправлена файлом или текстом 
				if 'numbers_file' in request.FILES:
					csv_file = request.FILES['numbers_file']
					if csv_file.name.endswith('.csv'):
						#csv_path = os.path(csv_path)
						# обработка csv
						file_data = csv_file.read().decode("utf-8")
						lines = file_data.split("\n")

						#with open(csv_path, "r") as f_obj:
						#	numbers_model.packet_content = csv_reader(f_obj)
						numbers_model.packet_name = csv_file.name
						numbers_model.packet_content = lines
					else:
						result = "файл должен иметь расширение csv"
						context_dict = {'app_name': app_name, 'sending_form': DataAboutSendingForm(), 'packet_form': NumberPacketForm(), "result": result}
						return render(request, app_name + "/index.html", context_dict)
				else:
					numbers_model.packet_content = packet_form.cleaned_data['numbers_text']
				numbers_model.user_id = request.user.id
				numbers_model.packet_name = packet_form.cleaned_data['packet_name']
				numbers_model.save()
				sending_model.user_id = request.user.id
				sending_model.packet_id = numbers_model
				sending_model.save()
				result = "Рассылка запущена/сохранена"
			else:
				result = packet_form.errors, sending_form.errors
		else:
			result = ""
	else:
		return HttpResponseRedirect('/login')
	context_dict = {'app_name': app_name, 'sending_form': DataAboutSendingForm(), 'packet_form': NumberPacketForm(), "result": result}
	return render(request, app_name + "/index.html", context_dict)


def registration(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			if user_form.cleaned_data['password'] == user_form.cleaned_data['repeat_password']:
				user = user_form.save()
				user.set_password(user.password)
				user.save()
				profile = profile_form.save(commit=False)
				profile.user = user
				if 'avatar' in request.FILES:
					profile.avatar = request.FILES['avatar']
				profile.save()
				registered = True
				result = "Пользователь создан успешно."
			else:
				result = "Пароли не совпадают"
		else:
			result = user_form.errors, profile_form.errors, user_form.is_valid(), profile_form.is_valid()
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
		result = ""
	context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'result': result,
	'user_pic': 'user_pic.jpg'}
	return render(request, app_name + '/register.html', context_dict)


def login(request):
	context_dict = {}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				return HttpResponseRedirect('/')
			else:
				context_dict = {'result': 'пользователь отключен'}
		else:
			context_dict = {'result': 'неправильно введены данные'}
	return render(request, app_name + '/login.html', context_dict)


@login_required
def logout_request(request):
	logout(request)
	return HttpResponseRedirect('/')