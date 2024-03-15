import numpy as np
import matplotlib.pyplot as plt 
 
  
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

players = list(data[1998].keys())
values = list(data[1998].values())

stats = [];
for v in values:
    stats.append(v['goals'])
  
fig = plt.figure(figsize = (10, 5))
    
# creating the bar plot
plt.bar(players, stats, color ='maroon', 
        width = 0.4)

for index, value in enumerate(stats):
    plt.text(index, value + 1, str(value))
    
plt.ylim(0, max(stats) + 5)
 
plt.xlabel("Players")
plt.ylabel("No. of goals scored")
plt.title("Liverpool FC Player Stats")
plt.show()
