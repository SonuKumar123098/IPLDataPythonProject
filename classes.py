import csv


class Match:
    def __init__(self, id=None, season=None, city=None, date=None, team1=None, team2=None,
                 toss_winner=None, toss_decision=None, result=None, dl_applied=None,
                 winner=None, win_by_runs=None, win_by_wickets=None, player_of_match=None,
                 venue=None, umpire1=None, umpire2=None, umpire3=None):
        self.id = id
        self.season = season
        self.city = city
        self.date = date
        self.team1 = team1
        self.team2 = team2
        self.toss_winner = toss_winner
        self.toss_decision = toss_decision
        self.result = result
        self.dl_applied = dl_applied
        self.winner = winner
        self.win_by_runs = win_by_runs
        self.win_by_wickets = win_by_wickets
        self.player_of_match = player_of_match
        self.venue = venue
        self.umpire1 = umpire1
        self.umpire2 = umpire2
        self.umpire3 = umpire3

    def __str__(self):
        return (f"Match(id={self.id!r}, season={self.season!r}, city={self.city!r}, "
                f"date={self.date!r}, team1={self.team1!r}, team2={self.team2!r}, "
                f"toss_winner={self.toss_winner!r}, toss_decision={self.toss_decision!r}, "
                f"result={self.result!r}, dl_applied={self.dl_applied!r}, winner={self.winner!r}, "
                f"win_by_runs={self.win_by_runs!r}, win_by_wickets={self.win_by_wickets!r}, "
                f"player_of_match={self.player_of_match!r}, venue={self.venue!r}, "
                f"umpire1={self.umpire1!r}, umpire2={self.umpire2!r}, umpire3={self.umpire3!r})")


def read_matches_from_csv(file_path):
    matches = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            match = Match(
                id=row.get('id'),
                season=row.get('season'),
                city=row.get('city'),
                date=row.get('date'),
                team1=row.get('team1'),
                team2=row.get('team2'),
                toss_winner=row.get('toss_winner'),
                toss_decision=row.get('toss_decision'),
                result=row.get('result'),
                dl_applied=row.get('dl_applied'),
                winner=row.get('winner'),
                win_by_runs=row.get('win_by_runs'),
                win_by_wickets=row.get('win_by_wickets'),
                player_of_match=row.get('player_of_match'),
                venue=row.get('venue'),
                umpire1=row.get('umpire1'),
                umpire2=row.get('umpire2'),
                umpire3=row.get('umpire3')
            )
            matches.append(match)
    return matches


class Delivery:
    def __init__(self, match_id=None, inning=None, batting_team=None, bowling_team=None,
                 over=None, ball=None, batsman=None, non_striker=None, bowler=None,
                 is_super_over=None, wide_runs=None, bye_runs=None, legbye_runs=None,
                 noball_runs=None, penalty_runs=None, batsman_runs=None, extra_runs=None,
                 total_runs=None, player_dismissed=None, dismissal_kind=None, fielder=None):
        self.match_id = match_id
        self.inning = inning
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.over = over
        self.ball = ball
        self.batsman = batsman
        self.non_striker = non_striker
        self.bowler = bowler
        self.is_super_over = is_super_over
        self.wide_runs = wide_runs
        self.bye_runs = bye_runs
        self.legbye_runs = legbye_runs
        self.noball_runs = noball_runs
        self.penalty_runs = penalty_runs
        self.batsman_runs = batsman_runs
        self.extra_runs = extra_runs
        self.total_runs = total_runs
        self.player_dismissed = player_dismissed
        self.dismissal_kind = dismissal_kind
        self.fielder = fielder

    def __str__(self):
        return (f"Delivery(match_id={self.match_id!r}, inning={self.inning!r}, "
                f"batting_team={self.batting_team!r}, bowling_team={self.bowling_team!r}, "
                f"over={self.over!r}, ball={self.ball!r}, batsman={self.batsman!r}, "
                f"non_striker={self.non_striker!r}, bowler={self.bowler!r}, "
                f"is_super_over={self.is_super_over!r}, wide_runs={self.wide_runs!r}, "
                f"bye_runs={self.bye_runs!r}, legbye_runs={self.legbye_runs!r}, "
                f"noball_runs={self.noball_runs!r}, penalty_runs={self.penalty_runs!r}, "
                f"batsman_runs={self.batsman_runs!r}, extra_runs={self.extra_runs!r}, "
                f"total_runs={self.total_runs!r}, player_dismissed={self.player_dismissed!r}, "
                f"dismissal_kind={self.dismissal_kind!r}, fielder={self.fielder!r})")


def read_deliveries_from_csv(file_path):
    deliveries = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            delivery = Delivery(
                match_id=row.get('match_id'),
                inning=row.get('inning'),
                batting_team=row.get('batting_team'),
                bowling_team=row.get('bowling_team'),
                over=row.get('over'),
                ball=row.get('ball'),
                batsman=row.get('batsman'),
                non_striker=row.get('non_striker'),
                bowler=row.get('bowler'),
                is_super_over=row.get('is_super_over'),
                wide_runs=row.get('wide_runs'),
                bye_runs=row.get('bye_runs'),
                legbye_runs=row.get('legbye_runs'),
                noball_runs=row.get('noball_runs'),
                penalty_runs=row.get('penalty_runs'),
                batsman_runs=row.get('batsman_runs'),
                extra_runs=row.get('extra_runs'),
                total_runs=row.get('total_runs'),
                player_dismissed=row.get('player_dismissed'),
                dismissal_kind=row.get('dismissal_kind'),
                fielder=row.get('fielder')
            )
            deliveries.append(delivery)
    return deliveries
