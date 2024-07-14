# Brand Logo Detection Pipeline

This project provides a comprehensive pipeline for detecting Brand Logos like (Pepsi and Coca-Cola) in a video file  and recording their presence with timestamps. It consists of two main files:

- `timestamp.py`: A Python script to detect logos in a video and record their timestamps.
- `video.ipynb`: A Jupyter Notebook providing an training file for custom model.

## Table of Contents

1. [Requirements](#requirements)
2. [Setup](#setup)
3. [Usage](#usage)
   - [Running the Python Script](#running-the-python-script)
   - [Using the Jupyter Notebook](#using-the-jupyter-notebook)
4. [Output](#output)

## Requirements

- Python 3.7+
- OpenCV
- Ultralytics YOLO
- Jupyter Notebook (for `video.ipynb`)
- roboflow

## Setup

1. Clone the repository or download the project files.

2. Install the required Python libraries:

    ```bash
    pip install opencv-python ultralytics jupyter roboflow
    ```

3. Make sure you have the trained YOLO model file (`best.pt`) using the `video.ipynb` and run training and place it in the appropriate directory.

## Usage

### Running the Python Script

The `timestamp.py` script processes a video file to detect objects and records their timestamps.

1. Open a terminal and navigate to the directory containing `timestamp.py`.

2. Run the script:

    ```bash
    python timestamp.py
    ```

3. The script will read the video file, perform logo detection, and save the timestamps of detected objects in a JSON file named `timestamps.json`.

### Using the Jupyter Notebook

The `video.ipynb` notebook provides an interactive interface for custom model training on coke and pepsi logo.

1. Open a terminal and navigate to the directory containing `video.ipynb`.

2. Start Jupyter Notebook:

    ```bash
    jupyter notebook
    ```



## Output

- The `timestamp.py` script outputs a `timestamps.json` file containing the timestamps of detected objects in the following format:

    ```json
    {
        "Pepsi_pts": [10.1, 10.2, 10.3, ...],
        "CocaCola_pts": [20.3, 31.8, 40.12, ...]
    }
    ```

- The Jupyter Notebook provides visualizations and detailed ste

https://github.com/user-attachments/assets/1a4ea78d-4e68-49e5-8a12-c35be3597c4a



https://github.com/user-attachments/assets/fc54f1e2-b1cb-4a54-98ab-f522ea327474

ps for video processing and object detection.

---

Feel free to modify the files and the pipeline according to your needs. Happy detecting!
