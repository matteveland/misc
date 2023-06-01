import statsapi
import sys
import datetime

"""
Baseball standings
"""

teams = {
    "NLW": ["Dodgers", "Padres", "Diamondbacks", "Giants", "Rockies"],
    "NLC": ["Cubs", "Reds", "Brewers", "Pirates", "Cardinals"],
    "NLE": ["Braves", "Marlins", "Mets", "Phillies", "nationals"],  # good
    "ALW": ["Astros", "Angels", "Athletics", "Mariners", "Rangers"],  # good
    "ALC": ["White Sox", "Gaurdians", "tigers", "Royals", "Twins"],  # no
    "ALE": ["Orioles", "Red Sox", "Yankees", "Blue Jays", "Rays", "Devil Rays"],
}

today = datetime.date.today()
year = today.year


def find_top_performers_for_year(team):
    find_year = team[0]
    find_team = team[1]
    team_id = team[2]
    categories = ["walks", "hits", "homeruns", "runs"]
    for category in categories:
        print(
            find_team.title() + " leader for " + category.title() + " in " + find_year
        )
        print(statsapi.team_leaders(team_id, category, limit=5, season=find_year))


def find_team_standings(team):
    find_year = team[0]
    find_team = team[1]
    for division, team in teams.items():
        if find_team in team:
            return statsapi.standings(
                division=division, season=find_year, include_wildcard="False"
            )


def team_look_up():
    find_team = input("Team: ").title().strip()

    team_look = statsapi.lookup_team(find_team)
    find_year = input("Year: ")

    while True:
        for division, team in teams.items():
            if find_team in team:
                # need to determine if the team was an actual team for the year entered. do not want to have years before or after a team
                try:
                    if team_look != []:
                        team_name = team_look[0]["teamName"]
                        team_id = team_look[0]["id"]
                        team_start = statsapi.get(
                            "team", {"teamId": team_id}, {"startSeason"}
                        )
                        team_start = team_start["teams"][0]["firstYearOfPlay"]
                        if int(find_year) >= 1993:
                            if int(find_year) <= year - 1:
                                return find_year, team_name, team_id, division
                            else:
                                find_year = input(
                                    "Standings begin with the expansion 1994. Enter a year less than "
                                    + str(year - 1)
                                    + ": "
                                )
                        else:
                            find_year = input(
                                "Standings begin with the expansion 1994. Enter a year from 1994 through "
                                + str(year - 1)
                                + ": "
                            )
                except:
                    sys.exit("error occurred")

        find_team = input(f"Please enter a valid team:\n from {list(teams.values())} ")


def main():
    standings = team_look_up()
    results = find_team_standings(standings)
    print(results)
    find_top_performers_for_year(standings)


if __name__ == "__main__":
    main()

