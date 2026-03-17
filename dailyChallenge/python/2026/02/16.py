# 2026 Winter Games Day 16: Curling

# Given a 5x5 matrix representing the "house" at the end of a curling round, determine which team scores and how many points they score.

# The layout:

#     The center cell (index [2, 2]) is the "button".
#     The 8 cells directly surrounding the button represent ring 1.
#     And the 16 cells on the outer edge of the house represent ring 2.

# In the given matrix:

#     "." represents an empty space.
#     "R" represents a space with a red stone.
#     "Y" represents a space with a yellow stone.

# Scoring rules:

#     Only one team can score per round.
#     The team with the stone closest to the button scores.
#     The scoring team earns 1 point for each of their stones that is closer to the button than the opponent's closest stone.
#     The lower the ring number, the closer to the center the stone is.
#     If both teams' closest stone is the same distance from the center, no team scores.

# Return:

#     A string in the format "team: number_of_points". e.g: "R: 2".
#     or "No points awarded" if neither team scored any points.

# For example, given:

# [
#   [".", ".", "R", ".", "."],
#   [".", "R", ".", ".", "."],
#   ["Y", ".", ".", ".", "."],
#   [".", "R", ".", ".", "."],
#   [".", ".", ".", ".", "."]
# ]

# Return "R: 2". The two red stones in ring 1 are tied for the closest and are the only two stones closer than yellows closest.
# Tests:

# 1. score_curling([[".", ".", "R", ".", "."], [".", "R", ".", ".", "."], ["Y", ".", ".", ".", "."], [".", "R", ".", ".", "."], [".", ".", ".", ".", "."]]) should return "R:2".
# 2. score_curling([[".", ".", "R", ".", "."], [".", ".", ".", ".", "."], [".", ".", "Y", ".", "R"], [".", ".", "Y", "Y", "."], [".", "Y", "R", "R", "."]]) should return "Y: 3".
# 3. score_curling([[".", "R", "Y", ".", "."], ["Y", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", "Y", "R", "Y", "."], [".", ".", "R", "R", "."]]) should return "No points awarded".
# 4. score_curling([[".", "Y", "Y", ".", "."], ["Y", ".", ".", "R", "."], [".", ".", "R", ".", "."], [".", ".", "R", "R", "."], [".", "Y", "R", "Y", "."]]) should return "R: 4".
# 5. score_curling([["Y", "Y", "Y", "Y", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "R", "Y", "R", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "Y", "Y", "Y", "Y"]]) should return "Y: 1".
# 6. score_curling([["Y", "R", "Y", "R", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", ".", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", "R", "Y"]]) should return "No points awarded".


def score_curling(house):
    ring2 = ["0,0", "0,1", "0,2", "0,3", "0,4", "1,0", "1,4", "2,0", "2,4", "3,0", "3,4", "4,0", "4,1", "4,2", "4,3", "4,4",]
    ring1 = ["1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3",]
    
    scores = {}
    ring1_scores = {}
    ring2_scores = {}

    for index_l, l in enumerate(house):
        for index_c, c in enumerate(l):
            if str(index_l) + "," + str(index_c) in ring1:
                if c not in ["."]:
                    scores[c + "ring1"] = scores.get(c + "ring1", 0) + 1
                    ring1_scores[c] = ring1_scores.get(c, 0) + 1 
            if str(index_l) + "," + str(index_c) in ring2:
                if c not in ["."]:
                    scores[c + "ring2"] = scores.get(c + "ring2", 0) + 1
                    ring2_scores[c] = ring2_scores.get(c, 0) + 1 
    if house[2][2] not in ["."]:
        return f"{house[2][2]}: {scores[house[2][2] + "ring1"]}"
    sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))

    if len(ring1_scores) > 1:
        return "No points awarded"

    if len(ring1_scores) == 0  and len(ring2_scores) > 1:
        return "No points awarded"

    return f"{list(sorted_scores.items())[0][0][:1]}: {list(sorted_scores.items())[0][1]}"



print(
    score_curling(
        [
            [".", ".", "R", ".", "."],
            [".", "R", ".", ".", "."],
            ["Y", ".", ".", ".", "."],
            [".", "R", ".", ".", "."],
            [".", ".", ".", ".", "."],
        ]
    )
)
print(
    score_curling(
        [
            [".", ".", "R", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", "Y", ".", "R"],
            [".", ".", "Y", "Y", "."],
            [".", "Y", "R", "R", "."],
        ]
    )
)
print(
    score_curling(
        [
            [".", "R", "Y", ".", "."],
            ["Y", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", "Y", "R", "Y", "."],
            [".", ".", "R", "R", "."],
        ]
    )
)
print(
    score_curling(
        [
            [".", "Y", "Y", ".", "."],
            ["Y", ".", ".", "R", "."],
            [".", ".", "R", ".", "."],
            [".", ".", "R", "R", "."],
            [".", "Y", "R", "Y", "."],
        ]
    )
)
print(
    score_curling(
        [
            ["Y", "Y", "Y", "Y", "Y"],
            ["Y", "R", "R", "R", "Y"],
            ["Y", "R", "Y", "R", "Y"],
            ["Y", "R", "R", "R", "Y"],
            ["Y", "Y", "Y", "Y", "Y"],
        ]
    )
)
print(
    score_curling(
        [
            ["Y", "R", "Y", "R", "Y"],
            ["R", ".", ".", ".", "R"],
            ["Y", ".", ".", ".", "Y"],
            ["R", ".", ".", ".", "R"],
            ["Y", ".", ".", "R", "Y"],
        ]
    )
)
