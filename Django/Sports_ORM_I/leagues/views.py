from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		'baseball_leagues':League.objects.filter(sport='Baseball'), # all baseball leagues
		'women_leagues':League.objects.filter(name__contains='Womens'), # all womens' leagues
		'hockey_leagues':League.objects.filter(sport__contains="hockey"), # all leagues where sport is any type of hockey
		'leagues_are_not_football':League.objects.exclude(sport="Football"), # all leagues where sport is something OTHER THAN football
		'conferences_leagues':League.objects.filter(name__contains="Conference"), # all leagues that call themselves "conferences"
		'atlantic_leagues':League.objects.filter(name__contains="Atlantic"), # all leagues in the Atlantic region
		'dallas_teams':Team.objects.filter(location="Dallas"), # all teams based in Dallas
		'raptors':Team.objects.filter(team_name="Raptors"), # all teams named the Raptors
		'cities_teams':Team.objects.filter(location__contains="City"), # all teams whose location includes "City"
		'teams_start_with_t':Team.objects.filter(team_name__startswith="T"), # all teams whose names begin with "T"
		'ordered_teams_by_location':Team.objects.all().order_by("location"), # all teams, ordered alphabetically by location
		'ordered_teams_by_name_reverse':Team.objects.all().order_by("-team_name"), # all teams, ordered by team name in reverse alphabetical order
		'players_with_lname_cooper':Player.objects.filter(last_name="Cooper"), # every player with last name "Cooper"
		'players_with_fname_joshua':Player.objects.filter(first_name="Joshua"), # every player with first name "Joshua"
		'players_with_lname_cooper_without_joshua':Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"), # every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
		'alexander_or_wyatt':Player.objects.filter(first_name__in=["Alexander","Wyatt"]), # all players with first name "Alexander" OR first name "Wyatt"
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")