from django.shortcuts import render, get_object_or_404
from .models import Character, Battle

def character_list(request):
    characters = Character.objects.all()
    return render(request, 'battle/character_list.html', {'characters': characters})

def battle_view(request, attacker_id, defender_id):
    attacker = get_object_or_404(Character, id=attacker_id)
    defender = get_object_or_404(Character, id=defender_id)

    if attacker.attack_power >= defender.health:
        winner = attacker
    else:
        winner = defender

    battle = Battle.objects.create(attacker=attacker, defender=defender, winner=winner)
    return render(request, 'battle/battle_result.html', {'battle': battle})