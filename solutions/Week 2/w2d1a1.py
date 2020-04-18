# Solution


def minion_game(string):

    vowels = 'AEIOU'

    kevinScore = 0
    stuartScore = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevinScore += (len(string)-i)
        else:
            stuartScore += (len(string)-i)

    if kevinScore > stuartScore:
        print("Kevin", kevinScore)
    elif kevinScore < stuartScore:
        print("Stuart", stuartScore)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)


# -------------------------------------------------------------------------------------------------------------------------

# Explanation :

# string[0] = B

# BANANA
# BANAN
# BANA
# BAN
# BA
# B

# stuartScore = 6

# string[1] = A

# ANANA
# ANAN
# ANA
# AN
# A

# kevinScore = 5

# string[2] = N

# NANA
# NAN
# NA
# N

# stuartScore = 6 + 4

# string[3] = A

# ANA
# AN
# A

# kevinScore = 5 + 3

# string[4] = N

# NA
# N

# stuartScore = 6 + 4 + 2

# string[5] = A

# A

# kevinScore = 5 + 3 + 1

# stuartScore = 6 + 4 + 2 = 12
# kevinScore = 5 + 3 + 1 = 9

# -------------------------------------------------------------------------------------------------------------------------

# Input :
# BANANA

# Output :
# Stuart 12
