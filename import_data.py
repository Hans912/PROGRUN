import csv
# Read the data from the CSV file for our first athlete
csv_file_Enshu = "/Users/hanshelmrichlaura/Desktop/UMICH_CLASSES/SI_339/Deliverable_2/athletes/mens_team/Enshu Kuan23687884.csv"

data = []
with open(csv_file_Enshu, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if row: # only append the row if it isn't empty (csv files had a lot of useless empty rows)
            data.append(row)

print(data[5]) # I checked which row was the one with all the info (In the future I will somehow automate this or delete useless rows)

# Extract the data from the CSV
Athlete_name = data[5][0]  # Column A 
Placement = data[5][1]  # Column B 
Grade = data[5][2]  # Column C 
Time = data[5][3]  # Column D
Date = data[5][4]  # Column E 
Meet = data[5][5] # Column F
Comments = data[5][6] #Column G
Photo = data[5][7] # COlumnn H

# I printed all the var to make sure that i captured the data correctly
print(Athlete_name)
print(Placement)
print(Grade)
print(Time)
print(Date)
print(Meet)
print(Comments)

html_content_friend = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <title>PROGRUN Friends Community</title>
</head>
<body>
    <h1>COMMUNITY</h1>
    <div>
        <button>Your friends</button>
        <button onclick="window.location.href='explore_community.html'">Explore</button>
        <button onclick="window.location.href='index.html'">Home</button>
    </div>
    <div class="Post">
        <p>{Athlete_name}</p>
        <p>{Date} | Placed: {Placement} | Time: {Time} | {Meet}</p>
        <p>Comments: {Comments}</p>
        <img src="" alt="sample picture"/>
    </div>
</body>
</html>
'''

# I create a new html file called frien_community where I will display all our friends we "follow" (This should be a future feature)
output_file = "Deliverable_2/friend_community.html"
with open(output_file, 'w') as file:
    file.write(html_content_friend)


### Now we do it all for the second Athlete again

csv_file_Enshu = "/Users/hanshelmrichlaura/Desktop/UMICH_CLASSES/SI_339/Deliverable_2/athletes/womens_team/Adrienne Stewart21142907.csv"

data = []
with open(csv_file_Enshu, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if row:
            data.append(row)

print(data[5])

# Extract the data from the CSV
Athlete_name = data[6][0]  # Column A 
Placement = data[6][1]  # Column B 
Grade = data[6][2]  # Column C 
Time = data[6][3]  # Column D 
Date = data[6][4]  # Column E 
Meet = data[6][5] # Column F
Comments = data[6][6] #Column G
Photo = data[6][7] # Column H

# print all var again to make sure its all good
print(Athlete_name)
print(Placement)
print(Grade)
print(Time)
print(Date)
print(Meet)
print(Comments)

html_content_explore = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <title>PROGRUN Explore Community</title>
</head>
<body>
    <h1>COMMUNITY</h1>
    <div>
        <button onclick="window.location.href='friend_community.html'">Your friends</button>
        <button>Explore</button>
        <button onclick="window.location.href='index.html'">Home</button>
    </div>
    <div class="Post">
        <p>{Athlete_name}</p>
        <p>{Date} | Placed: {Placement} | Time: {Time} | {Meet}</p>
        <p>Comments: {Comments}</p>
        <img src="" alt="sample picture"/>
    </div>
</body>
</html>
'''

# Output to explore commmunity which will be for people you don't follow
output_file = "Deliverable_2/explore_community.html"
with open(output_file, 'w') as file:
    file.write(html_content_explore)
