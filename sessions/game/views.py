from django.shortcuts import render, HttpResponse, redirect

from game.models import Player, Game, PlayerGameInfo

from .forms import NameForm, Is_NewGameForm, GameNameForm

def show_home(request):
	template = 'home.html'
	print(request)

	if request.method == 'POST':
		name = NameForm(request.POST)
		request.session['no_name'] = False
		print('работает_имя')

		if name.is_valid():
			data = name.clean_name()
			if data is None:
				print('data_is_None')
			else:
				print(data)
			try:
				print('все не ок')
			except:
				return redirect('is_admin/')
		else:
			data = 'проблема с валидацией name'

	else:
		name = NameForm()
		data = 'no'
		print('error')

	context = {
		'name': name,

	}

	return render(request, template, context)

def is_admin(request):
	template = 'is_admin.html'

	if request.method == 'POST':
		new_game = Is_NewGameForm(request.POST)
		request.session['new_game'] = False
		print('работает_new_game')

		if new_game.is_valid():
			data = new_game.cleaned_data['data']
			print(data)
			return HttpResponse('is_admin/')
		else:
			data = 'проблема с валидацией new_game'

	else:
		new_game = Is_NewGameForm()
		data = 'no'
		print('error')

	context = {
		'new_game': new_game,

	}

	return render(request, template, context)

def sucess(request, ):
	pass