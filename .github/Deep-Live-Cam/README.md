
# Deep Live Cam

## Overview
Deep Live Cam is a deep learning application designed for real-time image processing using advanced models. This project leverages various machine learning frameworks and tools to provide efficient and effective image enhancement and manipulation.

## Project Structure
```
Deep-Live-Cam
├── models              # Directory for model files
├── src                 # Source code for the application
│   ├── run.py         # Main entry point of the application
│   ├── utils          # Utility functions
│   │   └── helpers.py # Helper functions for various tasks
│   └── __init__.py    # Marks the src directory as a Python package
├── requirements.txt    # Python dependencies
├── setup_deep_live_cam.bat # Setup script for the project
└── README.md           # Project documentation
```

## Installation
To set up the project, run the `setup_deep_live_cam.bat` script. This will check for necessary dependencies and install them if they are not already present.

### Prerequisites
- Python 3.10 or later
- Pip
- Git
- FFMPEG
- Visual Studio 2022 Runtimes

## Usage
After setting up the project, you can run the application by executing the following command in the terminal:

```
python src/run.py
```

You may also specify an execution provider for GPU acceleration if applicable.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.