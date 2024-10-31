from django.db.models import Count
from django.shortcuts import render, redirect
from .models import League, Team, Player
from . import team_maker

def index(request):
    context = {
        "atlantic_soccer_conference_teams": Team.objects.filter(league__name="Atlantic Soccer Conference"),
        "boston_penguins_players": Player.objects.filter(curr_team__team_name="Penguins", curr_team__location="Boston"),
        "international_collegiate_baseball_conference_players": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
        "american_conference_of_amateur_football_lopez_players": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football", last_name="Lopez"),
        "football_players": Player.objects.filter(curr_team__league__sport="Football"),
        "sophia_teams": Team.objects.filter(curr_players__first_name="Sophia"),
        "sophia_leagues": League.objects.filter(teams__curr_players__first_name="Sophia").distinct(),
        "flores_players": Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders", curr_team__location="Washington"),
        "samuel_evans_teams": Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
        "manitoba_tiger_cats_players": Player.objects.filter(curr_team__team_name="Tiger-Cats", curr_team__location="Manitoba"),
        "former_wichita_vikings_players": Player.objects.filter(all_teams__team_name="Vikings", all_teams__location="Wichita").exclude(curr_team__team_name="Vikings", curr_team__location="Wichita"),
        "jacob_gray_teams": Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(team_name="Colts",location="Oregon"),
        "joshua_atlantic_federation_of_amateur_baseball_players": Player.objects.filter(curr_team__league__name="Atlantic Federation of Amateur Baseball Players", first_name="Joshua"),
        "12_or_more_players_teams": Team.objects.annotate(player_count=Count('all_players')).filter(player_count__gte=12),
        "all_players_sorted_by_count_of_teams_played_for": Player.objects.annotate(team_count=Count('all_teams')).order_by('-team_count'),
    }
    return render(request, "leagues/index.html", context)

def make_data(request):
    team_maker.gen_leagues(10)
    team_maker.gen_teams(50)
    team_maker.gen_players(200)
    return redirect("index")
