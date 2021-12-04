print("Hello World")


my_list = []

print(my_list)
 
# Creating a List of numbers
counties = ["Arapahoe","Denver","Jefferson"]
print("\nLcounties_names ")
print(counties)
print(counties[0])
len(counties)
print ("Number of items in the list = ", len(counties))
print ("Position of the counties", counties[0:2])
counties.append("El Paso")
print(counties)
counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties[2]="Broward"
print(counties)
counties_tuple = ("Arapahoe","Denver","Jefferson")
print(counties_tuple)
print ("Number of items in A TUPLE",len(counties_tuple))
counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
len(counties_dict)
print("Number of items in the dictionary",len(counties_dict))
counties_dict.items()
print ("All items in the dictionary",counties_dict.items())
counties_dict.keys()
print ("All the keys in the dictionary",counties_dict.keys())
counties_dict.values()
print ("All the values in the dictionary",counties_dict.values())
counties_dict.get("Denver")
print("Get a specific value from a dictionary",counties_dict.get("Denver"))
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

x = 0
while x <= 5:
    print(x)
    x = x + 1

