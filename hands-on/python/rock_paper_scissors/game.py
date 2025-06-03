# Rock Paper Scissors Game

# Class that represents the scorer of the game
class Scorer:

    # initialize the scorer with two player scores
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0

    # method to calculate points for the winning move
    def calculate_points(self, move):
        if move == "rock":
            return 1
        elif move == "paper":
            return 2
        elif move == "scissors":
            return 3
        else:
            print("Invalid move")
            return 0
        
    # Method to update the score based on the winner and the move
    def update_score(self, winner, move):
        points = self.calculate_points(move)
        if winner == "player1":
            self.player1_score += points
        elif winner == "player2":
            self.player2_score += points
        else:
            print("Invalid winner")

    def get_final_scores(self):
        return self.player1_score, self.player2_score
    
    def get_winner(self):
        if self.player1_score > self.player2_score:
            return "Player 1 wins!"
        elif self.player2_score > self.player1_score:
            return "Player 2 wins!"
        else:
            return "It's a tie!"

# Function to determine the winner of a rock paper scissors round
def determine_winner(player1_move, player2_move):
    if player1_move == player2_move:
        return "tie"
    elif (player1_move == "rock" and player2_move == "scissors") or \
         (player1_move == "paper" and player2_move == "rock") or \
         (player1_move == "scissors" and player2_move == "paper"):
        return "player1"
    else:
        return "player2"
    
# Main function to simulate a 5-round match between Player 1 and Player 2 with predefined moves and score tracking
# Print out detailed texts, results of each round and the final scores
# predifned moves for Player 1 and Player 2:
# player1_moves = ['scissors', 'paper', 'scissors', 'rock', 'rock']
# player2_moves = ['rock', 'rock', 'paper', 'scissors', 'paper']
def main():
    player1_moves = ['scissors', 'paper', 'scissors', 'rock', 'rock']
    player2_moves = ['rock', 'rock', 'paper', 'scissors', 'paper']
    
    scorer = Scorer()
    
    for i in range(5):
        player1_move = player1_moves[i]
        player2_move = player2_moves[i]
        
        print(f"Round {i + 1}:")
        print(f"Player 1 plays: {player1_move}")
        print(f"Player 2 plays: {player2_move}")
        
        winner = determine_winner(player1_move, player2_move)
        
        if winner == "tie":
            print("It's a tie!")
        else:
            print(f"{winner} wins this round!")
            scorer.update_score(winner, player1_move if winner == "player1" else player2_move)
            initial_scores = scorer.get_final_scores()
            print(f"Initial Scores: Player 1: {initial_scores[0]}, Player 2: {initial_scores[1]}")
        
        print("-" * 30)
    
    final_scores = scorer.get_final_scores()
    print(f"Final Scores: Player 1: {final_scores[0]}, Player 2: {final_scores[1]}")
    print(scorer.get_winner())


if __name__ == "__main__":
    main()