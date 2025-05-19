# Rock Paper Scissors: Game Simulation 🏆

In this hands-on lab, you'll build a Python implementation of a classic Rock Paper Scissors game between two players with the help of GitHub Copilot! This lab demonstrates how GitHub Copilot can assist with creating game logic, scoring systems, and user interfaces.

## Lab Overview 📋

**Duration**: 45-60 Minutes  
**Difficulty**: Beginner to Intermediate  
**Prerequisites**:

- Basic knowledge of Python and console applications
- Python 3.8+: [Download Python](https://www.python.org/downloads/)
- pip package manager (included with Python)

## What You'll Build 🏗️

A Python console application that simulates a Rock Paper Scissors match with the following components:

- Game logic for rock, paper, scissors
- Scoring system based on the winning move
- Round-by-round simulation of the match
- Optional advanced features like hints and player move selection

## Getting Started 🚀

### Step 1: Set Up the Project Structure

We'll start by setting up a basic Python project structure. GitHub Copilot will help us create the necessary files and configurations.

!!! tip "Copilot Tip"
     You can ask Github Copilot Chat to provide you with the steps to create a Python based project with a prompt like: ``How can I create a Python based project, where I need one file for the game and another file for the testing?``

     You can use ``@workspace`` agent to 

Let's set up our project directory. Create an empty folder and navigate to it via terminal.

```powershell
mkdir rock_paper_scissors
cd rock_paper_scissors
```

Create a virtual environment and activate it:

```powershell
python -m venv venv
# For Windows
venv\Scripts\activate
# For macOS/Linux
# source venv/bin/activate
```

A sample project structure could look like this:
```
rock_paper_scissors/
├── game.py
└── tests/
    └── test_game.py
```

### Step 2: Create the Game File - Step by Step

Let's start by creating a single file that contains all the game logic, scoring system, and main application. We'll build this incrementally, introducing GitHub Copilot features along the way.

First, create a new file called `game.py` in your project directory:

```powershell
# Create an empty game.py file
New-Item -Path "game.py" -ItemType "file"
```

#### Step 2.1: Setting Up the Basic Structure

Open `game.py` in your editor and let's first create the basic structure for our game:

!!! tip "Copilot Tip"
     Start with a comment describing what you want to build, and GitHub Copilot will suggest code based on your description. Try typing the following comment at the top of your file:
     ```python
     # Rock Paper Scissors game implementation
     ```

After typing the comment, press Enter, and Copilot may suggest some initial code. Let's start by implementing the `Scorer` class:

```python
# Rock Paper Scissors game implementation

class Scorer:
    """
    Class to handle scoring for the Rock Paper Scissors game.
    """
```

#### Step 2.2: Implementing the Scorer Class

Now let's implement the constructor for our `Scorer` class:

!!! tip "Copilot Tip"
     Start typing the `__init__` method and press Tab to accept Copilot's suggestion. If Copilot doesn't immediately suggest what you want, try adding a comment describing what you need.

```python
class Scorer:
    """
    Class to handle scoring for the Rock Paper Scissors game.
    """
    
    def __init__(self):
        """Initialize scores for both players."""
        self.player1_score = 0
        self.player2_score = 0
```

Now let's implement a method to update scores. This time, use comments to guide Copilot:

!!! tip "Copilot Tip"
     Add a comment describing what the method should do, and Copilot will suggest an implementation. Try typing:
     ```python
     # Method to update the score based on the winner and the move
     ```

Try implementing the `update_score` method that takes two parameters (`winner` and `move`):

```python
def update_score(self, winner, move):
    """
    Update the score based on the winner and the move.
    
    Args:
        winner (int): 1 if player 1 wins, 2 if player 2 wins, 0 if it's a draw
        move (str): The winning move ('rock', 'paper', or 'scissors')
    """
```

After typing this, Copilot should suggest the method body. Accept the suggestion by pressing Tab. You should end up with something like:

```python
def update_score(self, winner, move):
    """
    Update the score based on the winner and the move.
    
    Args:
        winner (int): 1 if player 1 wins, 2 if player 2 wins, 0 if it's a draw
        move (str): The winning move ('rock', 'paper', or 'scissors')
    """
    points = self.calculate_points(move)
    
    if winner == 1:
        self.player1_score += points
    elif winner == 2:
        self.player2_score += points
```

#### Step 2.3: Using Copilot Edit Mode for the Calculate Points Method

Now let's implement the `calculate_points` method using Copilot's Edit Mode:

!!! tip "Copilot Tip"
     Select the code area where you want to add the new method, press Ctrl+I to open inline chat, and enter a prompt like:
     "/edit Add a method called calculate_points that determines points based on the move (rock=1, paper=2, scissors=3)"

After receiving Copilot's suggestion, your code should now include:

```python
def calculate_points(self, move):
    """
    Calculate points for a winning move.
    
    Args:
        move (str): The winning move ('rock', 'paper', or 'scissors')
        
    Returns:
        int: Points for the move (rock=1, paper=2, scissors=3)
    """
    points = {
        'rock': 1,
        'paper': 2,
        'scissors': 3
    }
    return points.get(move, 0)
```

#### Step 2.4: Using Copilot to Generate Helper Methods

Let's add methods to get the final scores and determine the winner. For this, we'll use Copilot's ability to generate code based on function names.

!!! tip "Copilot Tip"
     Simply type the method name and signature, and Copilot will suggest the implementation. Try typing:
     ```python
     def get_final_scores(self):
     ```

Add the remaining methods to complete the `Scorer` class:

```python
def get_final_scores(self):
    """
    Get the final scores for both players.
    
    Returns:
        tuple: (player1_score, player2_score)
    """
    return (self.player1_score, self.player2_score)

def get_winner(self):
    """
    Determine the overall winner based on scores.
    
    Returns:
        int: 1 if player 1 wins, 2 if player 2 wins, 0 if it's a draw
    """
```

Copilot should suggest the implementation of the `get_winner` method. Accept the suggestion to get:

```python
def get_winner(self):
    """
    Determine the overall winner based on scores.
    
    Returns:
        int: 1 if player 1 wins, 2 if player 2 wins, 0 if it's a draw
    """
    if self.player1_score > self.player2_score:
        return 1
    elif self.player2_score > self.player1_score:
        return 2
    else:
        return 0
```

#### Step 2.5: Adding the Game Logic Function

Now let's implement the core game logic with a function to determine the winner of a round:

!!! tip "Copilot Tip"
     Add a comment describing the function before implementing it. Try typing:
     ```python
     # Function to determine the winner of a rock paper scissors round
     ```

Add the `determine_winner` function after the `Scorer` class:

```python
# Function to determine the winner of a rock paper scissors round
def determine_winner(player1_move, player2_move):
    """
    Determine the winner of a rock paper scissors round.
    
    Args:
        player1_move (str): Move chosen by player 1 ('rock', 'paper', or 'scissors')
        player2_move (str): Move chosen by player 2 ('rock', 'paper', or 'scissors')
        
    Returns:
        int: 1 if player 1 wins, 2 if player 2 wins, 0 if it's a draw
    """
```

Accept Copilot's suggestion for the function implementation:

```python
def determine_winner(player1_move, player2_move):
    """
    Determine the winner of a rock paper scissors round.
    
    Args:
        player1_move (str): Move chosen by player 1 ('rock', 'paper', or 'scissors')
        player2_move (str): Move chosen by player 2 ('rock', 'paper', or 'scissors')
        
    Returns:
        int: 1 if player 1 wins, 2 if player 2 wins, 0 if it's a draw
    """
    if player1_move == player2_move:
        return 0  # Draw
        
    if (player1_move == 'rock' and player2_move == 'scissors') or \
       (player1_move == 'paper' and player2_move == 'rock') or \
       (player1_move == 'scissors' and player2_move == 'paper'):
        return 1  # Player 1 wins
    else:
        return 2  # Player 2 wins
```

#### Step 2.6: Implementing the Main Game Loop

Finally, let's implement the main game loop that simulates the match:

!!! tip "Copilot Tip"
     For longer functions like the main game loop, you can give Copilot more detailed instructions using comments. Try typing:
     ```python
     # Main function to simulate a 5-round match between Player 1 and Player 2
     # with predefined moves and score tracking
     ```

Start implementing the `main` function:

```python
# Main function to simulate a 5-round match between Player 1 and Player 2
# with predefined moves and score tracking
def main():
    """Main function to run the Rock Paper Scissors match simulation."""
```

Accept Copilot's suggestion for the implementation. It should provide something like:

```python
def main():
    """Main function to run the Rock Paper Scissors match simulation."""
    print("=== Rock Paper Scissors: Classic Match ===")
    print("Two players compete in a 5-round match.")
    print("Each move carries weight and consequences.")
    print("\n")
    
    # Initialize scorer
    scorer = Scorer()
    
    # Predefined moves for Player 1
    player1_moves = ['scissors', 'paper', 'scissors', 'rock', 'rock']
    
    # Predefined moves for Player 2
    player2_moves = ['rock', 'rock', 'paper', 'scissors', 'paper']
    
    # Simulate 5 rounds
    for round_num in range(5):
        print(f"=== Round {round_num + 1} ===")
        
        player1_move = player1_moves[round_num]
        player2_move = player2_moves[round_num]
        
        print(f"Player 1 chooses: {player1_move.upper()}")
        print(f"Player 2 chooses: {player2_move.upper()}")
        
        winner = determine_winner(player1_move, player2_move)
        winning_move = player1_move if winner == 1 else player2_move if winner == 2 else None
        
        if winner == 0:
            print("It's a DRAW! No points awarded.")
        else:
            winner_name = "Player 1" if winner == 1 else "Player 2"
            points = scorer.calculate_points(winning_move)
            print(f"{winner_name} WINS with {winning_move.upper()}! {points} points awarded.")
            scorer.update_score(winner, winning_move)
        
        print(f"Current scores: Player 1 {scorer.player1_score}, Player 2 {scorer.player2_score}")
        print("\n")
    
    # Determine overall winner
    print("=== Final Results ===")
    final_scores = scorer.get_final_scores()
    print(f"Final scores: Player 1 {final_scores[0]}, Player 2 {final_scores[1]}")
    
    overall_winner = scorer.get_winner()
    if overall_winner == 0:
        print("The match ends in a DRAW!")
    else:
        winner_name = "Player 1" if overall_winner == 1 else "Player 2"
        print(f"{winner_name} is the WINNER of the Rock Paper Scissors match!")
```

#### Step 2.7: Adding the Entry Point

Finally, let's add the entry point to our script:

!!! tip "Copilot Tip"
     For standard Python idioms like the entry point, Copilot often needs minimal prompting. Try typing:
     ```python
     if __name__ == "__main__":
     ```

Complete the file with:

```python
if __name__ == "__main__":
    main()
```

At this point, your complete `game.py` should look like this:

??? abstract "Complete `game.py`"
    ```python
    # Rock Paper Scissors game implementation

    class Scorer:
        """
        Class to handle scoring for the Rock Paper Scissors game.
        """
        
        def __init__(self):
            """Initialize scores for both players."""
            self.player1_score = 0
            self.player2_score = 0
        
        def update_score(self, winner, move):
            """
            Update the score based on the winner and the move.
            
            Args:
                winner (int): 1 if player 1 wins, 2 if player 2 wins, 0 if it's a draw
                move (str): The winning move ('rock', 'paper', or 'scissors')
            """
            points = self.calculate_points(move)
            
            if winner == 1:
                self.player1_score += points
            elif winner == 2:
                self.player2_score += points
        
        def calculate_points(self, move):
            """
            Calculate points for a winning move.
            
            Args:
                move (str): The winning move ('rock', 'paper', or 'scissors')
                
            Returns:
                int: Points for the move (rock=1, paper=2, scissors=3)
            """
            points = {
                'rock': 1,
                'paper': 2,
                'scissors': 3
            }
            return points.get(move, 0)
        
        def get_final_scores(self):
            """
            Get the final scores for both players.
            
            Returns:
                tuple: (player1_score, player2_score)
            """
            return (self.player1_score, self.player2_score)
        
        def get_winner(self):
            """
            Determine the overall winner based on scores.
            
            Returns:
                int: 1 if player 1 wins, 2 if player 2 wins, 0 if it's a draw
            """
            if self.player1_score > self.player2_score:
                return 1
            elif self.player2_score > self.player1_score:
                return 2
            else:
                return 0


    # Function to determine the winner of a rock paper scissors round
    def determine_winner(player1_move, player2_move):
        """
        Determine the winner of a rock paper scissors round.
        
        Args:
            player1_move (str): Move chosen by player 1 ('rock', 'paper', or 'scissors')
            player2_move (str): Move chosen by player 2 ('rock', 'paper', or 'scissors')
            
        Returns:
            int: 1 if player 1 wins, 2 if player 2 wins, 0 if it's a draw
        """
        if player1_move == player2_move:
            return 0  # Draw
            
        if (player1_move == 'rock' and player2_move == 'scissors') or \
           (player1_move == 'paper' and player2_move == 'rock') or \
           (player1_move == 'scissors' and player2_move == 'paper'):
            return 1  # Player 1 wins
        else:
            return 2  # Player 2 wins


    # Main function to simulate a 5-round match between Player 1 and Player 2
    # with predefined moves and score tracking
    def main():
        """Main function to run the Rock Paper Scissors match simulation."""
        print("=== Rock Paper Scissors: Classic Match ===")
        print("Two players compete in a 5-round match.")
        print("Each move carries weight and consequences.")
        print("\n")
        
        # Initialize scorer
        scorer = Scorer()
        
        # Predefined moves for Player 1
        player1_moves = ['scissors', 'paper', 'scissors', 'rock', 'rock']
        
        # Predefined moves for Player 2
        player2_moves = ['rock', 'rock', 'paper', 'scissors', 'paper']
        
        # Simulate 5 rounds
        for round_num in range(5):
            print(f"=== Round {round_num + 1} ===")
            
            player1_move = player1_moves[round_num]
            player2_move = player2_moves[round_num]
            
            print(f"Player 1 chooses: {player1_move.upper()}")
            print(f"Player 2 chooses: {player2_move.upper()}")
            
            winner = determine_winner(player1_move, player2_move)
            winning_move = player1_move if winner == 1 else player2_move if winner == 2 else None
            
            if winner == 0:
                print("It's a DRAW! No points awarded.")
            else:
                winner_name = "Player 1" if winner == 1 else "Player 2"
                points = scorer.calculate_points(winning_move)
                print(f"{winner_name} WINS with {winning_move.upper()}! {points} points awarded.")
                scorer.update_score(winner, winning_move)
            
            print(f"Current scores: Player 1 {scorer.player1_score}, Player 2 {scorer.player2_score}")
            print("\n")
        
        # Determine overall winner
        print("=== Final Results ===")
        final_scores = scorer.get_final_scores()
        print(f"Final scores: Player 1 {final_scores[0]}, Player 2 {final_scores[1]}")
        
        overall_winner = scorer.get_winner()
        if overall_winner == 0:
            print("The match ends in a DRAW!")
        else:
            winner_name = "Player 1" if overall_winner == 1 else "Player 2"
            print(f"{winner_name} is the WINNER of the Rock Paper Scissors match!")


    if __name__ == "__main__":
        main()
    ```

### Step 3: Create a Test File - Step by Step

Now let's create a test file to verify our game logic. We'll build this incrementally as well.

First, create a tests directory and a test file:

```powershell
# Create tests directory
mkdir -p tests

# Create an empty test file
New-Item -Path "tests/test_game.py" -ItemType "file"
```

#### Step 3.1: Setting Up the Test Structure

Open `tests/test_game.py` in your editor and let's start by setting up the test structure:

!!! tip "Copilot Tip"
     Start by importing the required modules and setting up the test class. Try typing:
     ```python
     # Tests for the Rock Paper Scissors game
     
     import unittest
     ```

Copilot should suggest importing your game module. However, we need to make sure our test file can import from the parent directory. Add the following code:

```python
# Tests for the Rock Paper Scissors game

import unittest
import sys
import os

# Add the parent directory to the path so we can import game
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import determine_winner, Scorer
```

#### Step 3.2: Creating the Test Class

Now let's create a test class structure:

!!! tip "Copilot Tip"
     Type the class definition and Copilot will suggest the docstring and methods. Try typing:
     ```python
     class TestGame(unittest.TestCase):
     ```

```python
class TestGame(unittest.TestCase):
    """Test cases for the Rock Paper Scissors game."""
```

#### Step 3.3: Testing the determine_winner Function

Let's add our first test method to test the `determine_winner` function:

!!! tip "Copilot Tip"
     Use Copilot to generate test cases by typing the method name and docstring. For example:
     ```python
     def test_determine_winner(self):
         """Test the determine_winner function."""
     ```

Accept Copilot's suggestions for the test cases or add them yourself:

```python
def test_determine_winner(self):
    """Test the determine_winner function."""
    # Test draws
    self.assertEqual(determine_winner('rock', 'rock'), 0)
    self.assertEqual(determine_winner('paper', 'paper'), 0)
    self.assertEqual(determine_winner('scissors', 'scissors'), 0)
    
    # Test player 1 wins
    self.assertEqual(determine_winner('rock', 'scissors'), 1)
    self.assertEqual(determine_winner('paper', 'rock'), 1)
    self.assertEqual(determine_winner('scissors', 'paper'), 1)
    
    # Test player 2 wins
    self.assertEqual(determine_winner('scissors', 'rock'), 2)
    self.assertEqual(determine_winner('rock', 'paper'), 2)
    self.assertEqual(determine_winner('paper', 'scissors'), 2)
```

#### Step 3.4: Using Copilot to Generate Tests for the Scorer Class

Now let's add a test method for the `Scorer` class:

!!! tip "Copilot Tip"
     For more complex test cases, you can use Copilot's `/tests` command. In the editor, press Ctrl+I to open the inline chat and type:
     `/tests Write test cases for the Scorer class to verify point calculation and score updates`

After receiving Copilot's suggestions, you can adapt them to your code. Your test method should look like:

```python
def test_scorer(self):
    """Test the Scorer class."""
    scorer = Scorer()
    
    # Initial scores should be 0
    self.assertEqual(scorer.player1_score, 0)
    self.assertEqual(scorer.player2_score, 0)
    
    # Test point calculation
    self.assertEqual(scorer.calculate_points('rock'), 1)
    self.assertEqual(scorer.calculate_points('paper'), 2)
    self.assertEqual(scorer.calculate_points('scissors'), 3)
    
    # Test score updates
    scorer.update_score(1, 'rock')
    self.assertEqual(scorer.player1_score, 1)
    self.assertEqual(scorer.player2_score, 0)
    
    scorer.update_score(2, 'scissors')
    self.assertEqual(scorer.player1_score, 1)
    self.assertEqual(scorer.player2_score, 3)
    
    # Test get_winner
    self.assertEqual(scorer.get_winner(), 2)  # Player 2 has more points
    
    # Update Player 1's score to test tie
    scorer.update_score(1, 'scissors')
    self.assertEqual(scorer.player1_score, 4)
    self.assertEqual(scorer.player2_score, 3)
    
    # Now Player 1 should be winning
    self.assertEqual(scorer.get_winner(), 1)
```

#### Step 3.5: Adding the Test Runner

Finally, let's add the code to run the tests:

!!! tip "Copilot Tip"
     For standard test runners, Copilot can generate the code with minimal prompting. Try typing:
     ```python
     if __name__ == '__main__':
     ```

Complete the file with:

```python
if __name__ == '__main__':
    unittest.main()
```

At this point, your complete `test_game.py` should look like this:

??? abstract "Complete `test_game.py`"
    ```python
    # Tests for the Rock Paper Scissors game
    
    import unittest
    import sys
    import os
    
    # Add the parent directory to the path so we can import game
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from game import determine_winner, Scorer
    
    class TestGame(unittest.TestCase):
        """Test cases for the Rock Paper Scissors game."""
        
        def test_determine_winner(self):
            """Test the determine_winner function."""
            # Test draws
            self.assertEqual(determine_winner('rock', 'rock'), 0)
            self.assertEqual(determine_winner('paper', 'paper'), 0)
            self.assertEqual(determine_winner('scissors', 'scissors'), 0)
            
            # Test player 1 wins
            self.assertEqual(determine_winner('rock', 'scissors'), 1)
            self.assertEqual(determine_winner('paper', 'rock'), 1)
            self.assertEqual(determine_winner('scissors', 'paper'), 1)
            
            # Test player 2 wins
            self.assertEqual(determine_winner('scissors', 'rock'), 2)
            self.assertEqual(determine_winner('rock', 'paper'), 2)
            self.assertEqual(determine_winner('paper', 'scissors'), 2)
        
        def test_scorer(self):
            """Test the Scorer class."""
            scorer = Scorer()
            
            # Initial scores should be 0
            self.assertEqual(scorer.player1_score, 0)
            self.assertEqual(scorer.player2_score, 0)
            
            # Test point calculation
            self.assertEqual(scorer.calculate_points('rock'), 1)
            self.assertEqual(scorer.calculate_points('paper'), 2)
            self.assertEqual(scorer.calculate_points('scissors'), 3)
            
            # Test score updates
            scorer.update_score(1, 'rock')
            self.assertEqual(scorer.player1_score, 1)
            self.assertEqual(scorer.player2_score, 0)
            
            scorer.update_score(2, 'scissors')
            self.assertEqual(scorer.player1_score, 1)
            self.assertEqual(scorer.player2_score, 3)
            
            # Test get_winner
            self.assertEqual(scorer.get_winner(), 2)  # Player 2 has more points
            
            # Update Player 1's score to test tie
            scorer.update_score(1, 'scissors')
            self.assertEqual(scorer.player1_score, 4)
            self.assertEqual(scorer.player2_score, 3)
            
            # Now Player 1 should be winning
            self.assertEqual(scorer.get_winner(), 1)
    
    if __name__ == '__main__':
        unittest.main()
    ```

#### Step 3.6: Running the Tests

Now let's run the tests to verify that our game logic is working correctly:

```powershell
cd rock_paper_scissors
python -m unittest discover tests
```

If all tests pass, you should see output similar to:

```
.....
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

### Step 4: Run the Game

Now, let's run the game to see the simulation in action:

```powershell
python game.py
```

### Step 5: Advanced Features (Optional)

If you have time, try implementing these advanced features:

!!! tip "Copilot Tip"
     Ask Github Copilot to help you implement these advanced features by describing what you want to achieve.

1. **Hint System**: Add a hint system that suggests a move to the player

2. **Player Input**: Allow players to select their moves for each round

3. **GUI Interface**: Create a simple graphical interface using a library like Pygame or Tkinter

Here's an example of how you might add player input to the game:

??? abstract "Adding Player Input to `game.py`"
    ```python
    def get_player_move():
        """
        Get a move from the player.
        
        Returns:
            str: The player's move ('rock', 'paper', or 'scissors')
        """
        valid_moves = ['rock', 'paper', 'scissors']
        
        while True:
            move = input("Enter your move (rock, paper, or scissors): ").lower().strip()
            if move in valid_moves:
                return move
            else:
                print("Invalid move. Please try again.")
    
    def main_interactive():
        """Main function to run the interactive version of the game."""
        print("=== Rock Paper Scissors: Interactive Edition ===")
        print("You are Player 1, competing against Player 2.")
        print("Each move carries weight and consequences.")
        print("\n")
        
        # Initialize scorer
        scorer = Scorer()
        
        # Predefined moves for Player 2 - could be randomized for more fun
        player2_moves = ['rock', 'rock', 'paper', 'scissors', 'paper']
        
        # Play 5 rounds
        for round_num in range(5):
            print(f"=== Round {round_num + 1} ===")
            
            # Get player's move
            player1_move = get_player_move()
            player2_move = player2_moves[round_num]
            
            print(f"Player 1 (You) choose: {player1_move.upper()}")
            print(f"Player 2 chooses: {player2_move.upper()}")
            
            winner = determine_winner(player1_move, player2_move)
            winning_move = player1_move if winner == 1 else player2_move if winner == 2 else None
            
            if winner == 0:
                print("It's a DRAW! No points awarded.")
            else:
                winner_name = "Player 1 (You)" if winner == 1 else "Player 2"
                points = scorer.calculate_points(winning_move)
                print(f"{winner_name} WINS with {winning_move.upper()}! {points} points awarded.")
                scorer.update_score(winner, winning_move)
            
            print(f"Current scores: Player 1 (You) {scorer.player1_score}, Player 2 {scorer.player2_score}")
            print("\n")
        
        # Determine overall winner
        print("=== Final Results ===")
        final_scores = scorer.get_final_scores()
        print(f"Final scores: Player 1 (You) {final_scores[0]}, Player 2 {final_scores[1]}")
        
        overall_winner = scorer.get_winner()
        if overall_winner == 0:
            print("The match ends in a DRAW!")
        else:
            winner_name = "Player 1 (You)" if overall_winner == 1 else "Player 2"
            print(f"{winner_name} is the WINNER of the Rock Paper Scissors match!")
    ```

To run the interactive version, you would add this to your `game.py` file and modify the main block:

```python
if __name__ == "__main__":
    # Choose which version to run
    interactive = input("Do you want to play interactively? (y/n): ").lower() == 'y'
    if interactive:
        main_interactive()
    else:
        main()
```

## GitHub Copilot Tips 💡

### Use Copilot to improve efficiency

See if you can use Copilot to find out the complexity (BigO notation) of the code.

1. Open the GitHub Copilot Chat view in the sidebar if it's not already open. Make sure your solution file is still open as well.

2. Ask Copilot Chat what the complexity of the code is.

3. Ask Copilot Chat to make the code more efficient.

4. Ask for the complexity again - is it better?

### Use Copilot to generate code comments

1. Highlight all of the code with Ctrl/Cmd+A.

2. Press Ctrl/Cmd+I to open the inline chat.

3. Type "/doc"

4. Ask Copilot Chat to document the function.

### Use Copilot to simplify your code

1. Open GitHub Copilot Chat in the sidebar.

2. Type "/simplify" and press Enter. You can also add any text you want after the "/simplify" to give Copilot more instructions.

3. What did Copilot Chat suggest you do to make it simpler?

### Got Errors?

Copilot Chat can help with that too! Just copy the error message and paste it into Chat. Often that's all Copilot needs to resolve your issue.

## Summary 📝

In this lab, you've learned how to:

- Use GitHub Copilot to create a Rock Paper Scissors game simulation
- Implement game logic and scoring systems in Python
- Simulate a multi-round match with predefined moves
- Determine the winner based on accumulated points

GitHub Copilot has helped you write code faster and with less effort, allowing you to focus on the game design rather than the implementation details. This is a great example of how AI-assisted coding can enhance your development workflow! 🚀

## Bonus Challenges 🌟

If you've completed the lab and want an extra challenge, try:

1. Implementing different scoring rules
2. Adding more players to the game
3. Creating a tournament system with multiple matches
4. Adding sound effects for each move