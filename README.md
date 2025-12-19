# The Amazing Box

An interactive OpenGL-based animation program that allows you to create and control colorful bouncing points in a window.

## Description

The Amazing Box is a Python application built with PyOpenGL that creates an interactive particle system. Users can add colorful points that bounce around the window, with various controls to modify their behavior and appearance.

## Features

- **Interactive Point Creation**: Right-click anywhere in the window to add a new colorful bouncing point
- **Blinking Effect**: Toggle blinking animation for all points with left-click
- **Speed Control**: Adjust animation speed using arrow keys
- **Freeze/Unfreeze**: Pause and resume the animation with the spacebar
- **Dynamic Window Resizing**: The window can be resized and points adapt to the new boundaries
- **Random Colors**: Each point is assigned a random vibrant color
- **Smooth Animation**: 60 FPS animation with delta-time based movement

## Requirements

- Python 3.x
- PyOpenGL
- PyOpenGL-accelerate (optional, for better performance)
- GLUT (freeglut on Windows)

## Installation

1. Install PyOpenGL:
```bash
pip install PyOpenGL PyOpenGL-accelerate
```

2. On Windows, freeglut DLLs are included in the OpenGL package. On Linux/Mac, you may need to install GLUT separately:
   - **Linux (Ubuntu/Debian)**: `sudo apt-get install freeglut3-dev`
   - **Mac**: `brew install freeglut`

## Usage

Run the program:
```bash
python the_amaizing_box.py
```

### Controls

- **Right Mouse Click**: Add a new bouncing point at the cursor position
- **Left Mouse Click**: Toggle blinking effect on/off
- **Up Arrow Key**: Increase animation speed (up to 10x)
- **Down Arrow Key**: Decrease animation speed (down to 0.05x)
- **Spacebar**: Freeze/unfreeze all animation
- **Window Resize**: Points will bounce within the new window boundaries

## Technical Details

- **Window Size**: 800x600 pixels (default, resizable)
- **Point Size**: 5 pixels
- **Base Speed**: 100.0 units per second
- **Frame Rate**: ~60 FPS (16ms timer interval)
- **Color Range**: RGB values between 0.3 and 1.0 for vibrant colors

## Project Structure

```
.
├── the_amaizing_box.py    # Main application file
├── House_in_Rainy_Day.py  # Additional OpenGL project
├── Lets_draw_sth.py       # Additional OpenGL project
└── OpenGL/                # PyOpenGL library files
```

## How It Works

1. The program uses OpenGL's immediate mode rendering to draw points
2. Each point is stored as a dictionary with position (x, y), velocity (dx, dy), and color (r, g, b)
3. Points bounce off window boundaries by reversing their velocity components
4. A timer function updates positions every ~16ms for smooth 60 FPS animation
5. Delta-time calculation ensures consistent movement regardless of frame rate variations

## License

This project is open source and available for educational purposes.

