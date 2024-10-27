result = input("Enter a result: ")
teams = result.replace(result.split()[-1], "")
team1 = teams.split("-")[0]
team2 = teams.split("-")[1]
result1 = result.split()[-1].split(":")[0]
result2 = result.split()[-1].split(":")[1]
if result1 == result2:
    print("Ничья!")
elif result1 > result2:
    print(team1)
else:
    print(team2)