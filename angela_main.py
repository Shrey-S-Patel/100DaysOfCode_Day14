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

# Angela's version of the code.
# Start with defining the goals of ur code AKA problems to solve.

def format_data(account):
    """
    This function formats the account data into a printable statement.
    It returns a formatted string.
    """
    acc_name = account["name"]
    acc_desc = account["description"]
    acc_country = account["country"]

    return f"{acc_name}, a {acc_desc}, from {acc_country}"

def check_answer(user_guess, a_followers, b_followers):
    """"
    Checks a user's guess against the account with the highest followers.
    Returns either a True or False
    """
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

# Display Art
print(art.logo)
score = 0
game_should_continue = True
account_b = random.choice(game_data.data)

while game_should_continue:
    # Generate a random account that doesn't clash with the other one.
    # In case of a win, make the account at Position B the next account at position B.
    account_a = account_b
    account_b = random.choice(game_data.data)

    if account_a == account_b:
        account_b = random.choice(game_data.data)

    # Format account data into a more printable format.
    print(f"Compare A: {format_data(account_a)}")
    print(art.vs)
    print(f"Compare B: {format_data(account_b)}")

    # Ask the user for a guess.
    guess = input("Who has more followers? Type A or B:\n").lower()

    # Check if user is correct
    # - Get follower's count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # - Use an if statement to check if the user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # Keep user score
    # Make the game repeatable
    if is_correct:
        score += 1
        print(f"You're right! Current score is {score}")
    else:
        print(f"Sorry, That's wrong! Final score is {score}")
        game_should_continue = False


