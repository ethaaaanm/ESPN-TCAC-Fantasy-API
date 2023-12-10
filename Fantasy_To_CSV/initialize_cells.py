# Basketball API
import sys
sys.path.insert(0,"C:\\Users\\Tim\\Documents\\projects\\ESPN-TCAC-FANTASY-API")
from TCAC_Fantasy.basketball import League
import cookies
import csv


class InitializeCells(League):

    def initialize_header(teams):
        ''' Creates the header containing each team name'''
        header = []
        for team in teams:
            header.append(team.team_name)
            header.append("Average")
        return header



    ''' Creates a list of rows containing each player and their average from each team'''
    def make_rows(teams):
        rows = []
        # Find the maximum number of players among all teams
        max_players = max(len(team.roster) for team in teams)

        for j in range(max_players):
            row = []
            for i in range(len(teams)):
                # Check if the team has enough players
                if j < len(teams[i].roster):
                    row.append(str(teams[i].roster[j].name))
                    row.append(teams[i].roster[j].avg_points)
                else:
                    # If the team has fewer players, you can append placeholder values or handle it as needed
                    row.append("No Player")
                    row.append(0.0)  # Placeholder for average

            rows.append(row)

        return rows

    def total_average_row(teams):
        row = []
        for i in range(len(teams)):
            total = 0
            for player in teams[i].roster:
                total += player.avg_points
            row.append("Total Average")
            row.append(total/len(teams[i].roster))
        return row
            


if __name__ == "__main__":

    league = League(league_id = 467491942, year= 2024,espn_s2= cookies.espns2, swid = "47177C6B-491A-49B2-AA74-0FB83657947D")

    teams = league.teams
    with open('data.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(initialize_header(teams))
        writer.writerows(make_rows(teams))
        writer.writerow(total_average_row(teams))




