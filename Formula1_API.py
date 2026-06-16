import requests
from tabulate import tabulate
from rich import print
def getFinalStandings(location):
    driver_list = {
        43: "Franco Colapinto",
        10: "Pierre Gasly",
        14: "Fernando Alonso",
        18: "Lance Stroll",
        16: "Charles Leclerc",
        44: "Lewis Hamilton",
        31: "Esteban Ocon",
        87: "Oliver Bearman",
        5: "Gabriel Bortoleto",
        27: "Nico Hulkenberg",
        4: "Lando Norris",
        81: "Oscar Piastri",
        12: "Kimi Antonelli",
        63: "George Russell",
        6: "Isack Hadjar",
        7: "Jack Doohan",
        30: "Liam Lawson",
        23: "Alexander Albon",
        55: "Carlos Sainz",
        1: "Max Verstappen",
        22: "Yuki Tsunoda"
    }

    # country = input("What location: ")

    url = f'https://api.openf1.org/v1/sessions?circuit_short_name={location}&session_name=Race&session_type=Race&year=2025'
    response = requests.get(url)
    data = response.json()
    sessionKey = data[0]["session_key"]
    url = f'https://api.openf1.org/v1/session_result?session_key={sessionKey}&position<=25'
    response = requests.get(url)
    data = response.json()
    tabulateTable = []

    for i in data:
        placeholderList = []
        driverNumber = i["driver_number"]
        driverPosition = i["position"]
        gapToLeader = i["gap_to_leader"]
        points = i["points"]
        if driverNumber in driver_list:
            driverName = driver_list[driverNumber]
        # print(f'Driver: {driverName}, Position: {str(driverPosition)}, Gap to Leader (seconds): {str(gapToLeader)}, Points Gained: {points}')
        placeholderList.append(driverName)
        placeholderList.append(driverPosition)
        placeholderList.append(f"{gapToLeader} ")
        placeholderList.append(points)
        tabulateTable.append(placeholderList)
    return tabulateTable


    # print(tabulate(
    #     tabulateTable,
    #     headers=["Driver", "Position", "Gap To Leader", "Points"], 
    #     tablefmt="fancy_grid",
    #     numalign="center",
    #     stralign="center",
    # ))
    # print("\n[bold red]No Gap Time Indicates DNF.[/bold red]")
    # print("[bold red]Some drivers may not appear if they didn't start the race or encountered an accident.[/bold red]")

