
from django.db import models

class Player(models.Model):
	is_admin_player = models.BooleanField(default = False, verbose_name='создатель_игры?')
	player_name = models.CharField(max_length=256, verbose_name='имя_игрока')

	def __str__(self):
		return self.player_name



class Game(models.Model):
	game_name = models.CharField(max_length=256, verbose_name='название_игры')
	falls = models.IntegerField(default = 0, verbose_name='Количество попыток')
	number = models.IntegerField(verbose_name='Загаданное_число')
	is_ready = models.BooleanField(default = False, verbose_name='все игроки?')
	players = models.ManyToManyField(
		Player,
		through = 'PlayerGameInfo',
		related_name='players', 
		verbose_name='Игроки',
		)

	def __str__(self):
		return self.game_name

class PlayerGameInfo(models.Model):
	player = models.ForeignKey(
		Player,
		on_delete=models.CASCADE,
		verbose_name='Игрок'
		)
	game = models.ForeignKey(
		Game,
		on_delete=models.CASCADE,
		verbose_name='Игра'
		)

	def guess_player(self):
		return self.player.is_admin_player

	def __str__(self):
		return self.game.game_name + '__' + self.player.player_name

