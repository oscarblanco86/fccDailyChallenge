# 2026 Winter Games Day 14: Ski Mountaineering

# Given the snow depth and slope of a mountain, determine if there's an avalanche risk.

#     The snow depth values are "Shallow", "Moderate", or "Deep".
#     Slope values are "Gentle", "Steep", or "Very Steep".

# Return "Safe" or "Risky" based on this table:
# 	"Shallow" 	"Moderate" 	"Deep"
# "Gentle" 	"Safe" 	"Safe" 	"Safe"
# "Steep" 	"Safe" 	"Risky" 	"Risky"
# "Very Steep" 	"Safe" 	"Risky" 	"Risky"
# Tests:

#     Waiting: 1. avalanche_risk("Shallow", "Gentle") should return "Safe".
#     Waiting: 2. avalanche_risk("Shallow", "Steep") should return "Safe".
#     Waiting: 3. avalanche_risk("Shallow", "Very Steep") should return "Safe".
#     Waiting: 4. avalanche_risk("Moderate", "Gentle") should return "Safe".
#     Waiting: 5. avalanche_risk("Moderate", "Steep") should return "Risky".
#     Waiting: 6. avalanche_risk("Moderate", "Very Steep") should return "Risky".
#     Waiting: 7. avalanche_risk("Deep", "Gentle") should return "Safe".
#     Waiting: 8. avalanche_risk("Deep", "Steep") should return "Risky".
#     Waiting: 9. avalanche_risk("Deep", "Very Steep") should return "Risky".


def avalanche_risk(snow_depth, slope):
    safe_risky_table = {
        "Shallow_Gentle": "Safe",
        "Moderate_Gentle": "Safe",
        "Deep_Gentle": "Safe",
        "Shallow_Steep": "Safe",
        "Moderate_Steep": "Risky",
        "Deep_Steep": "Risky",
        "Shallow_Very Steep": "Safe",
        "Moderate_Very Steep": "Risky",
        "Deep_Very Steep": "Risky",
    }
    return safe_risky_table[snow_depth + "_" + slope]


print(avalanche_risk("Shallow", "Gentle"))
print(avalanche_risk("Shallow", "Steep"))
print(avalanche_risk("Shallow", "Very Steep"))
print(avalanche_risk("Moderate", "Gentle"))
print(avalanche_risk("Moderate", "Steep"))
print(avalanche_risk("Moderate", "Very Steep"))
print(avalanche_risk("Deep", "Gentle"))
print(avalanche_risk("Deep", "Steep"))
print(avalanche_risk("Deep", "Very Steep"))

