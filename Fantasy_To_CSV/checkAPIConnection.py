# Basketball API
from TCAC_Fantasy.basketball import League
from TCAC_Fantasy.utils import personal_details
import csv


header = []

# Initiate League Info
league = League(league_id=personal_details.league_id, year=personal_details.year, espn_s2=personal_details.espn_s2,
                swid=personal_details.swid)

teams = league.teams

# team _ team _ team _
for team in teams:
    header.append(team)
    header.append("Average")



def make_row(teams):
    rows = []
    
    # Find the maximum number of players among all teams
    max_players = max(len(team.roster) for team in teams)

    for j in range(max_players):
        row = []
        for i in range(len(teams)):
            # Check if the team has enough players
            if j < len(teams[i].roster):
                row.append(str(teams[i].roster[j]))
                row.append(teams[i].roster[j].avg_points)
            else:
                # If the team has fewer players, you can append placeholder values or handle it as needed
                row.append("No Player")
                row.append(0.0)  # Placeholder for average

        rows.append(row)

    return rows


def get_average(players):
    total = 0
    for player in players:
        total += player.avg_points
    return total / len(players)

with open('data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(make_row(teams))




