# 2026 Winter Games Day 11: Ice Hockey

# Given an array of 6 ice hockey teams and their records after the round robin games, determine the match-ups for the semi-final round.

#     Each array item will have a team and their record in the format "TEAM: W-OTW-OTL-L". Where:
#         "W" is the number of wins in regulation, worth 3 points each
#         "OTW" is the number of overtime wins, worth 2 points each
#         "OTL" is the number of overtime losses, worth 1 point each
#         "L" is the number of losses, worth 0 points each

# For example, "FIN: 2-2-1-0" would have 11 points after adding up their record.

# Find the total number of points for each team and return "The semi-final games will be (1st) vs (4th) and (2nd) vs (3rd).". For example, "The semi-final games will be FIN vs SWE and CAN vs USA."
# Tests:

#     Waiting: 1. get_semifinal_matchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"]) should return "The semi-final games will be FIN vs SWE and CAN vs USA.".
#     Waiting: 2. get_semifinal_matchups(["CAN: 2-1-1-1", "CZE: 1-1-1-2", "FIN: 1-2-1-1", "NOR: 0-1-1-3", "SLO: 1-0-1-3", "USA: 5-0-0-0"]) should return "The semi-final games will be USA vs CZE and CAN vs FIN.".
#     Waiting: 3. get_semifinal_matchups(["CAN: 3-2-0-0", "CZE: 2-1-2-0", "LAT: 0-0-1-4", "ITA: 1-1-1-2", "DEN: 1-0-0-4", "USA: 3-1-1-0"]) should return "The semi-final games will be CAN vs ITA and USA vs CZE.".
#     Waiting: 4. get_semifinal_matchups(["AUT: 2-2-1-0", "DEN: 1-0-0-4", "ITA: 1-1-1-2", "JPN: 3-2-0-0", "KOR: 2-1-2-0", "LAT: 0-0-1-4"]) should return "The semi-final games will be JPN vs ITA and AUT vs KOR.".


def get_semifinal_matchups(teams):
    team_scores = {}
    sorted_team = []
    for team in teams:
        ctry, scores = team.split(": ")
        score = scores.split("-")
        points = 0
        value = 3
        for sc in score:
            points += value * int(sc)
            value -= 1

        team_scores[ctry] = points
    sort_team_scores = dict(sorted(team_scores.items(), key=lambda item: item[1], reverse=True))
    for k, s in sort_team_scores.items():
        sorted_team.append(k)



    return f"The semi-final games will be {sorted_team[0]} vs {sorted_team[3]} and {sorted_team[1]} vs {sorted_team[2]}."

## copilot version
# def get_semifinal_matchups(teams):
#     team_scores = {}

#     for entry in teams:
#         team, record = entry.split(": ")
#         W, OTW, OTL, L = map(int, record.split("-"))
#         points = 3*W + 2*OTW + 1*OTL
#         team_scores[team] = points

#     sorted_teams = sorted(team_scores, key=lambda t: team_scores[t], reverse=True)

#     return f"The semi-final games will be {sorted_teams[0]} vs {sorted_teams[3]} and {sorted_teams[1]} vs {sorted_teams[2]}."



print(get_semifinal_matchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"]))
print(get_semifinal_matchups(["CAN: 2-1-1-1", "CZE: 1-1-1-2", "FIN: 1-2-1-1", "NOR: 0-1-1-3", "SLO: 1-0-1-3", "USA: 5-0-0-0"]))
print(get_semifinal_matchups(["CAN: 3-2-0-0", "CZE: 2-1-2-0", "LAT: 0-0-1-4", "ITA: 1-1-1-2", "DEN: 1-0-0-4", "USA: 3-1-1-0"]))
print(get_semifinal_matchups(["AUT: 2-2-1-0", "DEN: 1-0-0-4", "ITA: 1-1-1-2", "JPN: 3-2-0-0", "KOR: 2-1-2-0", "LAT: 0-0-1-4"]))