"""
Return the winning team.
Team gets 3 points on win, 0 on lose.
Competitions formatted as [[home_team, away_team], ...]
Results formatted as [0, 0, 1,...] where 0 is an away team win and 1 is a home team win
"""


def tournamentWinner(competitions, results):
    """
    Time: O(n) where n is the number of matches
    Space: O(k) where k is the number of teams
    """
    scores = {}
    leading_team = ""

    for index in range(len(results)):
        result = results[index]
        match_winner = competitions[index][1 - result]

        if not (leading_team):
            leading_team = match_winner

        if match_winner in scores:
            current_score = scores[match_winner]
            scores[match_winner] = current_score + 3
        else:
            scores[match_winner] = 3

        if scores[match_winner] > scores[leading_team]:
            leading_team = match_winner

    return leading_team
