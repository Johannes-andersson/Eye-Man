import pygame
import cv2
import mediapipe as mp
import numpy as np
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 700, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eye-Man")

# Load the eye image and scale it
try:
    eye_image = pygame.image.load('eye.png')  
    player_size = 40
    eye_image = pygame.transform.scale(eye_image, (player_size, player_size))
except pygame.error:
    # If image not found, use a simple circle instead
    eye_image = None
    player_size = 40

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Player settings
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 12  

# Initialize previous positions and smoothing factor
prev_x = player_pos[0]
prev_y = player_pos[1]
smoothing_factor = 0.3  

# Pellet settings
pellet_size = 10
pellet_positions = []

for _ in range(10):
    x = random.randint(0, WIDTH - pellet_size)
    y = random.randint(0, HEIGHT - pellet_size)
    pellet_positions.append([x, y])

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp.solutions.face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        break

    
    frame = cv2.flip(frame, 1)

    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and find face landmarks
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]

        # Get the coordinates of the nose tip (landmark 1)
        nose_tip = face_landmarks.landmark[1]
        x = int(nose_tip.x * WIDTH)
        y = int(nose_tip.y * HEIGHT)

        # Update player position with smoothing
        player_pos[0] = int(prev_x * smoothing_factor + (x - player_size // 2) * (1 - smoothing_factor))
        player_pos[1] = int(prev_y * smoothing_factor + (y - player_size // 2) * (1 - smoothing_factor))

        # Update previous positions
        prev_x = player_pos[0]
        prev_y = player_pos[1]

    # Keep player within screen boundaries
    player_pos[0] = max(0, min(WIDTH - player_size, player_pos[0]))
    player_pos[1] = max(0, min(HEIGHT - player_size, player_pos[1]))

    # Collision detection with pellets
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    pellets_to_remove = []
    for pellet in pellet_positions:
        pellet_rect = pygame.Rect(pellet[0], pellet[1], pellet_size, pellet_size)
        if player_rect.colliderect(pellet_rect):
            pellets_to_remove.append(pellet)

    for pellet in pellets_to_remove:
        pellet_positions.remove(pellet)
        # Optionally, add new pellets to keep the game going
        x = random.randint(0, WIDTH - pellet_size)
        y = random.randint(0, HEIGHT - pellet_size)
        pellet_positions.append([x, y])
        # Increase player size
        player_size += 2
        if eye_image:
            eye_image = pygame.transform.scale(eye_image, (player_size, player_size))

    # Clear the screen
    window.fill(BLACK)

    # Draw the player
    if eye_image:
        window.blit(eye_image, (player_pos[0], player_pos[1]))
    else:
        pygame.draw.circle(window, (0, 255, 0), (int(player_pos[0] + player_size // 2), int(player_pos[1] + player_size // 2)), player_size // 2)

    # Draw the pellets
    for pellet in pellet_positions:
        pygame.draw.rect(window, WHITE, (pellet[0], pellet[1], pellet_size, pellet_size))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

# Clean up
cap.release()
cv2.destroyAllWindows()
pygame.quit()
sys.exit()



