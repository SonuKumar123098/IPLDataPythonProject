from collections import defaultdict

# 3b716  today IPIN of Wifi
# IIMT merath ganganagar
from classes import *

matches = read_matches_from_csv('/home/sonu/Downloads/IplProjectData/matches.csv')
deliveries = read_deliveries_from_csv('/home/sonu/Downloads/IplProjectData/deliveries.csv')


def matches_per_year(matches):
    year_match_count = defaultdict(int)
    for match in matches:
        year = match.season  # 'season' represents the year
        year_match_count[year] += 1
    return dict(year_match_count)


print("Matches per year:", matches_per_year(matches))


def matches_won_by_team(matches):
    team_wins = defaultdict(int)
    for match in matches:
        if match.winner:
            team_wins[match.winner] += 1
    return dict(team_wins)


print("Matches won by teams:", matches_won_by_team(matches))


def extra_runs_conceded_per_team_2016(deliveries, matches):
    match_id_2016 = set()
    year = '2016'
    for match in matches:
        if match.season == year:
            match_id_2016.add(match.id)

    extra_runs_per_team = defaultdict(int)
    for delivery in deliveries:
        if delivery.match_id in match_id_2016:
            team = delivery.bowling_team
            extra_runs = int(delivery.extra_runs or 0)
            extra_runs_per_team[team] += extra_runs
    return dict(extra_runs_per_team)


print("Extra runs conceded per team (2016):", extra_runs_conceded_per_team_2016(deliveries, matches))


def top_economical_bowlers_2015(deliveries, matches):
    match_id_2015 = set()
    year = '2015'
    for match in matches:
        if match.season == year:
            match_id_2015.add(match.id)

    bowler_runs = defaultdict(int)
    bowler_overs = defaultdict(int)
    over = '0'
    for delivery in deliveries:
        if delivery.match_id in match_id_2015:
            bowler = delivery.bowler
            runs_conceded = int(delivery.total_runs or 0)
            bowler_runs[bowler] += runs_conceded
            if over != delivery.over:
                over = delivery.over
                bowler_overs[bowler] += 1

    bowler_economy = {bowler: (runs / bowler_overs[bowler]) for bowler, runs in bowler_runs.items() if
                      bowler_overs[bowler] > 0}
    sorted_bowlers = sorted(bowler_economy.items(), key=lambda x: x[1])
    return sorted_bowlers[:10]  # Top 10 economical bowlers


print("Top economical bowlers (2015):", top_economical_bowlers_2015(deliveries, matches))


def top_run_scorers_per_year(deliveries, matches):
    match_id_year = {}
    for match in matches:
        match_id_year[match.id] = match.season

    batsman_runs = defaultdict(lambda: defaultdict(int))  # year -> batsman -> runs
    for delivery in deliveries:
        year = match_id_year[delivery.match_id]
        batsman = delivery.batsman
        runs = int(delivery.batsman_runs or 0)
        batsman_runs[year][batsman] += runs

    top_scorers_per_year = {}
    for year, batsmen in batsman_runs.items():
        sorted_batsmen = sorted(batsmen.items(), key=lambda x: x[1], reverse=True)
        top_scorers_per_year[year] = sorted_batsmen[:5]  # Top 5 run-scorers

    return top_scorers_per_year


print("Top 5 highest run-scorers per year:", top_run_scorers_per_year(deliveries, matches))
