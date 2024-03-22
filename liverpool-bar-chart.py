import numpy as np
import matplotlib.pyplot as plt 

def barChart(labels, vals):
    fig = plt.figure(figsize = (10, 5))

    # creating the bar plot
    plt.bar(labels, vals, color ='maroon', 
            width = 0.8)

    for index, value in enumerate(vals):
        plt.text(index - (len(str(value)) * 0.02), value + 1, str(value))

    plt.ylim(0, max(stats) + 5)

    plt.xlabel("Players")
    plt.ylabel("No. of goals scored")
    plt.title("Liverpool FC Player Stats")
    plt.show()
    
def seasonName(year):
    return str(year) + "/" + str(year + 1)
  
# creating the dataset
data = {
    1998: {
        "Michael Owen": {"goals": 23, "appearances": 50},
        "Robbie Fowler": {"goals": 18, "appearances": 45},
        "Steve McManaman": {"goals": 10, "appearances": 52},
        # Add more players as necessary
    },
    1999: {
        "Michael Owen": {"goals": 19, "appearances": 48},
        "Robbie Fowler": {"goals": 15, "appearances": 42},
        "Emile Heskey": {"goals": 12, "appearances": 50},
        # Add more players as necessary
    },
    2000: {
        "Michael Owen": {"goals": 25, "appearances": 47},
        "Emile Heskey": {"goals": 14, "appearances": 49},
        "Steven Gerrard": {"goals": 10, "appearances": 44},
        # Add more players as necessary
    },
    2001: {
        "Michael Owen": {"goals": 28, "appearances": 45},
        "Emile Heskey": {"goals": 16, "appearances": 48},
        "Steven Gerrard": {"goals": 12, "appearances": 43},
        # Add more players as necessary
    },
    2002: {
        "Michael Owen": {"goals": 24, "appearances": 46},
        "Emile Heskey": {"goals": 11, "appearances": 47},
        "Steven Gerrard": {"goals": 14, "appearances": 42},
        # Add more players as necessary
    },
    2003: {
        "Michael Owen": {"goals": 18, "appearances": 41},
        "Harry Kewell": {"goals": 9, "appearances": 36},
        "Steven Gerrard": {"goals": 10, "appearances": 40},
        # Add more players as necessary
    }
}

seasons = list(data.keys())
    
ans = ""

while (ans != "0"):
    print ("Select a season")
    
    for i, s in enumerate(seasons):
        print (str(i + 1) + ": " + seasonName(s))
        
    print ("0: Exit")
    
    input(ans)
    season = seasons[ans - 1]
    
    print ("Select a stat")
    print ("1: goals")
    print ("2: appearances")
    print ("0: Exit")

    input(ans)
    if (ans == "1"): stat = "goals"
    if (ans == "2"): stat = "appearances"
    
    players = list(data[season].keys())
    values = list(data[season].values())

    stats = [];
    for v in values:
        stats.append(v[stat])
    

    barChart(players, stats)
