import random 

def guess_number_game():
  print("=" * 50)
  print("        WELCOME TO RANDOM NUMBER GUESSING!        ")
  print("=" * 50)
  print("I have selected a random number between 1 and 20.")
  print("Can you guess what it is?\n")

  # Generate a random number between 1 and 20
  secret_number = random.randint(1, 20)
  attempts = 0

  while True:
    try:
      # Get user input
      guess = int(input("Enter your guess (1-20): "))
      attempts += 1

      # Validate range
      if guess < 1 or guess > 20:
        print("⚠️ Please enter a number strictly between 1 and 20.\n")
        continue

      # Check guess against the secret number
      if guess < secret_number:
        print("📉 Too low! Try again.\n")
      elif guess > secret_number:
        print("📈 Too high! Try again.\n")
      else:
        print("*" * 50)
        print(
            f"🎉 Congratulations! You guessed the number"
            f" **{secret_number}** in **{attempts}** attempts!"
        )
        print("*" * 50)
        break

    except ValueError:
      print(
          "❌ Invalid input! Please enter a valid whole number (e.g., 42).\n"
      )


if __name__ == "__main__":

  while True:
    guess_number_game()

    # Prompt to replay
    play_again = (
        input("\nWould you like to play again? (yes/no): ").strip().lower()
    )
    if play_again not in ("y", "yes"):
      print("\nThanks for playing! Goodbye!")
      break
    print("\n" + "=" * 50 + "\nStarting a new game...\n" + "=" * 50)