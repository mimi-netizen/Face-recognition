# Complete Face Recognition Using SQL Database Project

![](<image/fr_PObolJML%20(1).gif>)

This project implements a face recognition system using Python, OpenCV, and SQLite. The system captures video from a webcam, detects faces, recognizes them using a trained model, and retrieves user information from a SQLite database.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Features

- Real-time face detection and recognition.
- User information retrieval from a SQLite database.
- Easy to set up and run.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- SQLite

You can install the required libraries using pip:

```bash
pip install opencv-python numpy
```

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/mimi-netizen/Face-recognition.git

   cd Face-recognition
   ```

2. Download the Haar Cascade file for face detection:

   - Ensure `haarcascade_frontalface_default.xml` is present in the project directory.

3. Set up the SQLite database:

   - Create a SQLite database (`sqlite.db`) and a table named `STUDENTS` with appropriate fields.

## Usage

1. Train the model (if not already trained):

   - Run the `trainer.py` script to train the face recognizer using images stored in the dataset.

   ```bash
   python trainer.py
   ```

2. Start the face recognition application:

   ```bash
   python detect.py
   ```

3. Press `q` to exit the application.

## File Structure

```bash
Face-recognition/
│
├── .idea/                     # IDE-specific files
├── __pycache__/               # Compiled Python files
├── haarcascade_frontalface_default.xml  # Haar Cascade file for face detection
├── database.db                # SQLite database file
├── dataset_creator.py         # Module to create datasets
├── detect.py                  # Main detection script
├── sqlite.db                  # SQLite database file
├── trainer.py                 # Script to train the face recognizer
└── README.md                  # Project documentation
```

### Notes

- Customize the database setup instructions according to your actual database schema.
- Ensure that all necessary files are correctly referenced and included in your repository.
- You may want to include more detailed instructions or features based on your specific implementation.
