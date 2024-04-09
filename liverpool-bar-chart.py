import numpy as np
import matplotlib.pyplot as plt 

def barChart(labels, vals, season, stat):
    plt.figure(figsize = (10, 5))

    plt.bar(labels, vals, color = (1, 0.2, 0.2))

    for index, value in enumerate(vals):
        plt.text(index - (len(str(value)) * 0.02), value + 1, str(value))

    plt.ylim(0, max(vals) + 5)
    plt.xticks(rotation=90)
    plt.axhline(y=np.nanmean(vals))

    plt.xlabel("Players")
    plt.ylabel("No. of " + stat)
    plt.title("Liverpool FC Player Stats for " + seasonName(season))
    plt.show()
    
def seasonName(year):
    return str(year) + "/" + str(year + 1)
  
# creating the dataset
data = {
    2017: {
        "Mohamed Salah": {"goals": 44, "appearances": 52},
        "Roberto Firminho": {"goals": 27, "appearances": 54},
        "Sadio Mane": {"goals": 20, "appearances": 44},
        "Alex Oxlade-Chamberlain": {"goals": 5, "appearances": 42}
    },
    2018: {
        "Mohamed Salah": {"goals": 27, "appearances": 52},
        "Roberto Firminho": {"goals": 16, "appearances": 48},
        "Sadio Mane": {"goals": 26, "appearances": 50},
        "Alex Oxlade-Chamberlain": {"goals": 0, "appearances": 2}
    },
    2019: {
        "Mohamed Salah": {"goals": 23, "appearances": 48},
        "Roberto Firminho": {"goals": 12, "appearances": 52},
        "Sadio Mane": {"goals": 22, "appearances": 47},
        "Alex Oxlade-Chamberlain": {"goals": 8, "appearances": 43}
    },
    2020: {
        "Mohamed Salah": {"goals": 31, "appearances": 51},
        "Roberto Firminho": {"goals": 9, "appearances": 48},
        "Sadio Mane": {"goals": 16, "appearances": 48},
        "Alex Oxlade-Chamberlain": {"goals": 1, "appearances": 17},
        "Diogo Jota": {"goals": 13, "appearances": 30}
    },
    2021: {
        "Mohamed Salah": {"goals": 31, "appearances": 51},
        "Roberto Firminho": {"goals": 11, "appearances": 35},
        "Sadio Mane": {"goals": 23, "appearances": 51},
        "Alex Oxlade-Chamberlain": {"goals": 3, "appearances": 29},
        "Diogo Jota": {"goals": 21, "appearances": 55},
        "Luis Diaz": {"goals": 6, "appearances": 26}
    },
    2022: {
        "Mohamed Salah": {"goals": 30, "appearances": 51},
        "Roberto Firminho": {"goals": 13, "appearances": 35},
        "Alex Oxlade-Chamberlain": {"goals": 1, "appearances": 13},
        "Diogo Jota": {"goals": 7, "appearances": 28},
        "Luis Diaz": {"goals": 5, "appearances": 21}
    }
}

seasons = list(data.keys())
    
ans1 = ""
ans2 = ""

while (ans1 != 0 and ans2 != 0):    
    for i, s in enumerate(seasons):
        print (str(i + 1) + ": " + seasonName(s))
        
    print ("0: Exit")

    while True:
        try:
            ans1 = int(input("Select a season"))
            break
        except:
            print("Invalid option. Please try again.")    

    if (ans1 == 0): break
    if (ans1 > len(seasons) + 1 or ans1 < 0): continue  
        
    season = seasons[ans1 - 1]
    
    print ("1: goals")
    print ("2: appearances")
    print ("0: Exit")

    while True:
        try:
            ans2 = int(input("Select a stat"))
            break
        except:
            print("Invalid option. Please try again.")
    
    if (ans2 == 1): stat = "goals"
    if (ans2 == 2): stat = "appearances"
    if (ans2 == 0): break
    if (ans2 > 2 or ans2 < 0): continue
    
    players = list(data[season].keys())
    values = list(data[season].values())

    stats = [];
    for v in values:
        stats.append(v[stat])

    barChart(players, stats, season, stat)
