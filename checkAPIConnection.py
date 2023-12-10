# Basketball API
from TCAC_Fantasy.basketball import League, Team
from TCAC_Fantasy.utils import cookies
# import pandas as pd

# Initiate League Info
league = League(league_id=467491942, year=2024, swid=cookies.swid, espn_s2=cookies.espns2)
allTeams = league.teams
numberOfTeams = len(allTeams)

print("Testing Successful")
print(league.league_id, league.year)
print(allTeams)

print(numberOfTeams)
for x in range(0, numberOfTeams):
    teamX = league.teams[x]
    print(teamX.team_name)
    teamSize = len(teamX.roster)
    for y in range(teamSize):
        player = teamX.roster[y].avg_points
        print(player)



# TODO: Clean ReadMe and MetaData
