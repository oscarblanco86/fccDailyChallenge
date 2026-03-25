# 2026 Winter Games Day 17: Closing Day

# Given a 2D array of medal winners, return a medal count for each country as a CSV string.

#     In the given array, each sub-array represents a single event: [gold_winner, silver_winner, bronze_winner]

#     The returned CSV string should have the following format, with the first line being headers:

# Country,Gold,Silver,Bronze,Total
# country_name,gold_count,silver_count,bronze_count,total_medals

#     Separate new lines with the new line character ("\n").
#     Do not include spaces around commas or at the end of lines.
#     Sort the returned CSV by gold medal count, highest first. If two countries have the same gold medal count, sort the tied ones alphabetically.

# For example, given:

# [
#   ["USA", "CAN", "NOR"],
#   ["NOR", "USA", "CAN"],
#   ["USA", "NOR", "SWE"]
# ]

# Return:

# "Country,Gold,Silver,Bronze,Total\nUSA,2,1,0,3\nNOR,1,1,1,3\nCAN,0,1,1,2\nSWE,0,0,1,1"

# Which looks like this when printed:

# Country,Gold,Silver,Bronze,Total
# USA,2,1,0,3
# NOR,1,1,1,3
# CAN,0,1,1,2
# SWE,0,0,1,1

# Tests:

#     Waiting: 1. count_medals([["USA", "CAN", "NOR"], ["NOR", "USA", "CAN"], ["USA", "NOR", "SWE"]]) 
# should return "Country,Gold,Silver,Bronze,Total
# \nUSA,2,1,0,3
# \nNOR,1,1,1,3
# \nCAN,0,1,1,2
# \nSWE,0,0,1,1".
#     Waiting: 2. count_medals([["NOR","SWE","FIN"]]) 
# should return "Country,Gold,Silver,Bronze,Total
# \nNOR,1,0,0,1
# \nFIN,0,0,1,1
# \nSWE,0,1,0,1".
#     Waiting: 3. count_medals([["ITA", "CHN", "CHN"], ["JPN", "ITA", "JPN"]]) 
# should return "Country,Gold,Silver,Bronze,Total
# \nITA,1,1,0,2
# \nJPN,1,0,1,2
# \nCHN,0,1,1,2".
#     Waiting: 4. count_medals([["USA","CAN","NOR"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["SWE","FIN","NOR"], ["CAN","USA","SWE"], ["FRA","GER","ITA"]]) 
# should return "Country,Gold,Silver,Bronze,Total
# \nCAN,1,1,0,2
# \nFRA,1,1,0,2
# \nGER,1,1,0,2
# \nJPN,1,0,0,1
# \nSWE,1,0,1,2
# \nUSA,1,1,0,2
# \nCHN,0,0,1,1
# \nFIN,0,1,0,1
# \nITA,0,0,2,2
# \nKOR,0,1,0,1
# \nNOR,0,0,2,2".
#     Waiting: 5. count_medals([["ESP","ITA","FRA"], ["ITA","ESP","GER"], ["NOR","SWE","FIN"], ["FIN","NOR","SWE"], ["USA","CAN","MEX"], ["CAN","USA","MEX"], ["JPN","KOR","CHN"], ["CHN","JPN","KOR"]]) 
# should return "Country,Gold,Silver,Bronze,Total
# \nCAN,1,1,0,2
# \nCHN,1,0,1,2
# \nESP,1,1,0,2
# \nFIN,1,0,1,2
# \nITA,1,1,0,2
# \nJPN,1,1,0,2
# \nNOR,1,1,0,2
# \nUSA,1,1,0,2
# \nFRA,0,0,1,1
# \nGER,0,0,1,1
# \nKOR,0,1,1,2
# \nMEX,0,0,2,2
# \nSWE,0,1,1,2".
#     Waiting: 6. count_medals([["USA","CAN","GER"], ["NOR","SWE","FIN"], ["USA","NOR","SWE"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["USA","GER","CAN"], ["SWE","NOR","FIN"], ["CAN","USA","NOR"], ["FRA","GER","ITA"], ["JPN","CHN","KOR"], ["SWE","FIN","NOR"], ["GER","ITA","FRA"]]) 
# should return "Country,Gold,Silver,Bronze,Total
# \nUSA,3,1,0,4
# \nGER,2,2,1,5
# \nJPN,2,0,0,2
# \nSWE,2,1,1,4
# \nCAN,1,1,1,3
# \nFRA,1,1,1,3\nNOR,1,2,2,5\nCHN,0,1,1,2\nFIN,0,1,2,3\nITA,0,1,2,3\nKOR,0,1,1,2".

# def count_medals(winners):
#     country_medals = {}

#     def country_default(ctry):
#         if ctry not in country_medals:
#             country_medals[ctry] = {'Gold': 0, 'Silver': 0, 'Bronze': 0, 'Total': 0}
    
#     def get_gold(cntr_dict, cntry):
#         return cntr_dict[cntry]['Gold']

#     def swap_countries(cntry_dict, ctry1, ctry2):
#         items = list(cntry_dict.items())
#         items[ctry1], items[ctry2] = items[ctry2], items[ctry1] 
#         return dict(items)
        
#     for [gold, silver, bronze] in winners:
#         country_default(gold)
#         country_default(silver)
#         country_default(bronze)
#         country_medals[gold]['Gold'] += 1
#         country_medals[gold]['Total'] += 1

#         country_medals[silver]['Silver'] += 1
#         country_medals[silver]['Total'] += 1

#         country_medals[bronze]['Bronze'] += 1
#         country_medals[bronze]['Total'] += 1
    
#     country_medals_sorted = dict(sorted(country_medals.items()))

#     country_list = list(country_medals_sorted.keys())

#     n = len(country_list)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if get_gold(country_medals_sorted, country_list[j]) < get_gold(country_medals_sorted, country_list[j + 1]):
#                 country_medals_sorted = swap_countries(country_medals_sorted, j, j + 1)
#                 country_list[j], country_list[j + 1] = country_list[j + 1], country_list[j]
#                 swapped = True
#         if not swapped:
#             break
#     table = ['Country,Gold,Silver,Bronze,Total\n']
#     for country, medals in country_medals_sorted.items():
#         table.append(country)
#         for count in medals:
#             table.append(f',{str(medals[count])}')
#         table.append('\n')
#     return "".join(table)

# Copilot solution
def count_medals(winners):
    # Step 1: Count medals
    medals = {}

    for gold, silver, bronze in winners:
        for country, medal in [(gold, "Gold"), (silver, "Silver"), (bronze, "Bronze")]:
            if country not in medals:
                medals[country] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            medals[country][medal] += 1

    # Step 2: Compute totals
    for country in medals:
        m = medals[country]
        medals[country]["Total"] = m["Gold"] + m["Silver"] + m["Bronze"]

    # Step 3: Sort by gold DESC, then alphabetically ASC
    sorted_countries = sorted(
        medals.items(),
        key=lambda item: (-item[1]["Gold"], item[0])
    )

    # Step 4: Build CSV output
    lines = ["Country,Gold,Silver,Bronze,Total"]
    for country, m in sorted_countries:
        line = f"{country},{m['Gold']},{m['Silver']},{m['Bronze']},{m['Total']}"
        lines.append(line)

    return "\n".join(lines)



print(count_medals([["USA", "CAN", "NOR"], ["NOR", "USA", "CAN"], ["USA", "NOR", "SWE"]]))
print(count_medals([["NOR","SWE","FIN"]]))
print(count_medals([["ITA", "CHN", "CHN"], ["JPN", "ITA", "JPN"]]))
print(count_medals([["USA","CAN","NOR"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["SWE","FIN","NOR"], ["CAN","USA","SWE"], ["FRA","GER","ITA"]]))
print(count_medals([["ESP","ITA","FRA"], ["ITA","ESP","GER"], ["NOR","SWE","FIN"], ["FIN","NOR","SWE"], ["USA","CAN","MEX"], ["CAN","USA","MEX"], ["JPN","KOR","CHN"], ["CHN","JPN","KOR"]]))
print(count_medals([["USA","CAN","GER"], ["NOR","SWE","FIN"], ["USA","NOR","SWE"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["USA","GER","CAN"], ["SWE","NOR","FIN"], ["CAN","USA","NOR"], ["FRA","GER","ITA"], ["JPN","CHN","KOR"], ["SWE","FIN","NOR"], ["GER","ITA","FRA"]]))