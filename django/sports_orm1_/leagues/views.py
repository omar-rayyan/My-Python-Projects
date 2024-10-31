from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		"baseball_leagues": League.objects.filter(sport__icontains="Baseball"),
		"women_leagues": League.objects.filter(name__icontains="Women"),
		"hockey_leagues": League.objects.filter(sport__icontains="Hockey"),
		"football_excluded_leagues": League.objects.exclude(sport__icontains="Football"),
		"conference_leagues": League.objects.filter(name__icontains="Conference"),
		"atlantic_leagues": League.objects.filter(name__icontains="Atlantic"),
		"dallas_teams": Team.objects.filter(location__icontains="Dallas"),
		"raptors_teams": Team.objects.filter(team_name__icontains="Raptors"),
		"city_teams": Team.objects.filter(location__icontains="City"),
		"t_teams": Team.objects.filter(team_name__startswith="T"),
		"location_alphabetically_ordered_teams": Team.objects.all().order_by("location"),
		"name_alphabetically_reversely_ordered_teams": Team.objects.all().order_by("-team_name"),
		"cooper_players": Player.objects.filter(last_name__icontains="Cooper"),
		"joshua_players": Player.objects.filter(first_name__icontains="Joshua"),
		"cooper_joshua_players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"alexander_wyatt_players": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt")),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")