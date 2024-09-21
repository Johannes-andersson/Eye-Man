# Eye-Man
Eye-Controlled Game
An interactive eye-controlled game built with Python, using MediaPipe for facial landmark detection and Pygame for game development. Control the player character with your head movements detected via your webcam.

<!-- Replace with an actual screenshot of your game -->

Table of Contents
Features
Demo
Installation
Usage
Requirements
How It Works
Customization
Troubleshooting
Future Enhancements
Contributing
License
Acknowledgements
Features
Eye-Controlled Movement: Control the player character using your head movements detected through your webcam.
Interactive Gameplay: Collect pellets to grow in size.
Responsive Controls: Adjusted for faster responsiveness and smooth movement.
Cross-Platform: Works on Windows, macOS, and Linux.
Demo
<!-- Optionally, include a GIF or video demo of your game -->

Installation
Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/eye-controlled-game.git
cd eye-controlled-game
Set Up a Virtual Environment (Optional but Recommended)
bash
Copy code
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Alternatively, install packages individually:

bash
Copy code
pip install pygame opencv-python mediapipe numpy
Place the Eye Image (Optional)
Ensure you have an eye.png image in the project directory.
If you don't have one, the game will use a simple circle to represent the player.
Usage
Run the game using:

bash
Copy code
python eye_controlled_game.py
Make sure your webcam is connected and accessible.

Controls
Movement: Move your head to control the player character.
Objective: Collect the pellets appearing on the screen to grow in size.
Notes
Ensure you're in a well-lit environment for better facial recognition.
Position your face within the webcam frame for optimal control.
Requirements
Python 3.7 or higher
Webcam
Operating System: Windows, macOS, or Linux
How It Works
MediaPipe Face Mesh: Detects facial landmarks using your webcam feed.
Nose Tip Tracking: The game tracks the position of your nose to control the player character.
Pygame Rendering: Handles game graphics, drawing the player and pellets, and updating the display.
Customization
Adjusting Player Responsiveness
Player Speed: Modify player_speed in eye_controlled_game.py to change responsiveness.

python
Copy code
player_speed = 10  # Increase for faster movement
Smoothing Factor: Adjust smoothing_factor to control movement smoothness.

python
Copy code
smoothing_factor = 0.3  # Lower for more responsiveness
Changing Player Appearance
Replace eye.png with your own image.

Modify player_size to adjust the initial size.

python
Copy code
player_size = 40  # Adjust as desired
Adding Sound Effects
Use pygame.mixer to add sounds when collecting pellets.
Displaying Score
Implement a score counter to display how many pellets you've collected.
Troubleshooting
Player Not Reaching Edges: Adjust boundary checks in the code.
Unresponsive Controls: Ensure your face is well-lit and fully visible to the webcam.
Webcam Issues: Close other applications that might be using the webcam.
Future Enhancements
Obstacle Implementation: Introduce obstacles to increase difficulty.
Multiplayer Mode: Allow multiple players to join the game.
High Score Tracking: Keep track of and display the highest scores.
Calibration Step: Add a calibration process to adjust controls for different users.
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

Fork the repository.
Create your feature branch: git checkout -b feature/YourFeature
Commit your changes: git commit -am 'Add some feature'
Push to the branch: git push origin feature/YourFeature
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
MediaPipe: MediaPipe Face Mesh
Pygame: Pygame Library
OpenCV: OpenCV Library
Inspired by tutorials and examples on facial landmark detection and eye-tracking.
