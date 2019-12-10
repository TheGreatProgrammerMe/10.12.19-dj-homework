from django import forms
from .models import Player, Game

class NameForm(forms.Form):
	data = forms.CharField(label='Ник  ')

	def clean_name(self):
		data = self.cleaned_data['data']
		if data != '1':
			raise forms.ValidationError("имя уже используется")
		return data
		# try:
		# 	obj = Player.objects.get(player_name=data)
		# 	raise forms.ValidationError('имя уже используется')
		# 	return None
		# except:
		# 	return data

	class Meta(object):
		model = Player
		fields = ('player_name')


class Is_NewGameForm(forms.Form):
	data = forms.ChoiceField(widget=forms.RadioSelect, choices=((1, True), (2, False)), label='Создатель игры? ')

	class Meta(object):
		model = Player
		fields = ('is_admin_player')

class GameNameForm(forms.Form):
	data = forms.CharField(label='Название игры  ')

	class Meta(object):
		model = Game
		fields = ('game_name')