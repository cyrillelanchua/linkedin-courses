# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use dictionary comprehensions


# define a list of temperature values
ctemps = [0, 12, 34, 100]

# TODO: Use a comprehension to build a dictionary
temp = {"key" + str(t): t**2 for t in ctemps if t < 100}
print(temp)

# TODO: Merge two dictionaries with a comprehension
team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}

print(team1, team2)

new_team = {k: v for team in (team1, team2) for k, v in team.items()}
print(new_team)
