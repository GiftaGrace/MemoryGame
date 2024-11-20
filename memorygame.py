import random

def display_board(board):
    """Display the current board with face-down cards represented as X."""
    for row in board:
        print(" ".join(row))
    print()

def get_card(board, row, col):
    """Return the card value at the specified position."""
    return board[row][col]

def memory_game():
    print("Welcome to the Memory Game!")
    
    # Create a list of card pairs (using numbers for simplicity)
    cards = ['1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6']
    
    # Shuffle the cards
    random.shuffle(cards)
    
    # Set up the board (4x3 grid for 12 cards)
    board = [['X' for _ in range(4)] for _ in range(3)]
    
    # Convert the shuffled list into a 3x4 board
    card_board = [cards[i:i+4] for i in range(0, len(cards), 4)]
    
    # Track the number of moves
    moves = 0
    matched_pairs = 0
    
    # Game loop
    while matched_pairs < 6:  # 6 pairs to match
        display_board(board)
        print(f"Matched pairs: {matched_pairs}/6")
        
        try:
            # Get the player's choice (coordinates to flip two cards)
            row1, col1 = map(int, input("Enter coordinates of first card to flip (row col): ").split())
            row2, col2 = map(int, input("Enter coordinates of second card to flip (row col): ").split())
            
            # Check if the coordinates are valid
            if (row1 < 0 or row1 > 2 or col1 < 0 or col1 > 3 or
                row2 < 0 or row2 > 2 or col2 < 0 or col2 > 3 or (row1 == row2 and col1 == col2)):
                print("Invalid coordinates. Please try again.")
                continue
            
            # Show the chosen cards
            card1 = card_board[row1][col1]
            card2 = card_board[row2][col2]
            
            # If the cards match
            if card1 == card2:
                print(f"Match found: {card1}!")
                board[row1][col1] = card1
                board[row2][col2] = card2
                matched_pairs += 1
            else:
                print(f"No match. Cards were {card1} and {card2}.")
                
            moves += 1
        except ValueError:
            print("Invalid input. Please enter two numbers for row and column.")
    
    # Display the final board and number of moves
    display_board(board)
    print(f"Congratulations! You completed the game in {moves} moves.")

if __name__ == "__main__":
    memory_game()
