import random
import art
import game_data
"""
# Shrey's version of the code.

wins = 0


def random_entity_gen():
    # Let's start by retrieving the data of two players randomly from our data list.
    return random.choice(game_data.data)


def compare(person1, person2):
    # Set the highest followers variable.
    if person1['follower_count'] > person2['follower_count']:
        return 'A'
    else:
        return 'B'

def higher_lower(entity1=random_entity_gen(), entity2=random_entity_gen()):
    global wins
    # Let's start by showing a cool little logo
    print(art.logo)

    p1 = entity1
    p2 = entity2

    if p1 == p2:
        p2 = random_entity_gen()

    print(f"Compare A: {p1['name']}, {p1['description']}, from {p1['country']}.")
    print(art.vs)
    print(f"Compare B: {p2['name']}, {p2['description']}, from {p2['country']}.")

    highest_followers = compare(p1, p2)
    # Get the user's guess from an input stmnt.
    choice = input("Who has more followers? Type A or B:\n")

    if choice == highest_followers:
        wins += 1
        print(f"That's correct! You Win! Current wins: {wins}")
        if highest_followers == 'A':
            return higher_lower(p1, random_entity_gen())
        else:
            return higher_lower(p2, random_entity_gen())
    else:
        print(f"Womp Womp! Final Score: {wins}")
        wins = 0


higher_lower()
"""


