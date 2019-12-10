from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Game, Player, PlayerGameInfo

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ('id', 'game_name', 'number', 'falls', 'is_ready')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	list_display = ('id', 'player_name', 'is_admin_player')

@admin.register(PlayerGameInfo)
class PlayerGameInfoAdmin(admin.ModelAdmin):
	pass
