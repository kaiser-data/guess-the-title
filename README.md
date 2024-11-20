# Guess the Title (Trivia Challenge Game)

## Description  
**Guess the Title (Trivia Challenge Game)** is an engaging quiz game where players test their knowledge by answering trivia questions. With a clean user interface and fun gameplay mechanics, it offers a competitive experience with a leaderboard to track the top scores.

---

![guess.png](guess.png)

---

## Features  
1. **Menu Screen**  
   - **Play:** Start the game.  
   - **High Score:** View the top 5 highest scores.  
   - **How to Play:** Learn the rules and mechanics.  
   - **Credits:** View the developers and acknowledgments.  
   - **Exit:** Close the game.  

2. **Gameplay Flow**  
   - Players input their name to begin.  
   - Each round presents a random image and related trivia question.  
   - Players choose from 4 options, aiming to pick the correct answer.  
   - Lives (starting at 3) and scores are displayed throughout the game.  

3. **Feedback Mechanisms**  
   - **Correct Answer:** Gain 100 point and receive positive feedback.  
   - **Incorrect Answer:** Lose 1 life and see a helpful message.  

4. **Game Loop**  
   - Continues until the player runs out of lives or quits.  
   - Score and lives dynamically update based on performance.  

5. **End of Game**  
   - Displays the player’s final score.  
   - Updates the leaderboard if the score is among the top 5.  
   - Shows the player’s rank and the top 5 scores.  

6. **Replay Options**  
   - After viewing scores, players return to the main menu for another round or to explore other options.

---

## How to Play  
1. Start the game and enter your name.  
2. Read the question and select the correct answer from four options.  
3. Each correct answer increases your score; incorrect answers reduce your lives.  
4. The game ends when you run out of lives.  
5. Aim for a high score and rank on the leaderboard!  

---

## 🛠️ Technologies Used  
- **Python**  
- **Requests**: Fetch external movie data via APIs.  
- **Python-Dotenv**: Secure environment variables.  
- **Wikipedia Rest API**:  lightweight, efficient API provided by Wikipedia to fetch random title, summary and image 
- **CustomTkinter**: Python GUI framework built on top of the traditional Tkinter library.
- **Urllib3**  HTTP client library for Python

---

## Credits  
- **Developers:** [Pikachu Coders/Martin Kaiser/Jerome de Dios/Mark Wernthaler]
- **Special Thanks:** [Shoval Zvulun]  

---

## Future Enhancements  
- Add more trivia categories and difficulty levels.  
- Introduce power-ups or hints to assist players.  
- Expand the leaderboard to include global rankings.  

---

## Installation  
1. Clone the repository:  
   ```bash
   git clone git@github.com:masterschool-weiterbildung/guess-the-title.git

2. Navigate to the project directory:  
   ```bash
   cd trivia-challenge-game

3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt 

4. For the CustomTkinter to work properly you need to copy:  
   ```bash  
   Run where python
   AppData\Local\Programs\Python\Python313\
   Copy the \tcl directory to your own .env directory (virtual env)
   
5. Run the game: 
   ```bash
   python main.py
   


