# Object Tracking

This Python script uses OpenCV to perform real-time object tracking on a video
file. The code allows users to manually select multiple objects to track, and
then it marks their position and draws their paths on the output_video.mp4

## Features

- **Object Tracking**: Track multiple objects in a video.
- **Path Visualization**: Tracks the movement of the objects, encircles objects and visualizes their paths with lines.
- **Custom Object Selection**: Allows the user to manually select the objects to track by drawing bounding boxes (ROIs).
- **Video Output**: Saves the result in a new video file with tracked objects and their paths drawn on each frame.

## Requirements

To run this project, you need Python 3.x and OpenCV installed. You can install the required dependencies using pip:

```bash
pip install opencv-python opencv-contrib-python numpy
```

## How to Use

Follow these simple steps to get started with the object tracking script:

1. **Set the Video Path**:
   Open the Python script (`tracking_objects.py`) and update the path to your video file where indicated.

2. **Run the Script**:
   Execute the Python script. 

3. Indicate number of object you want to track

4. Select the objects to track.
## How to Use

Follow these simple steps to get started with the object tracking script:

1. **Set the Video Path**  
   Open the Python script (`tracking_objects.py`) and update the path to your video file where indicated.

2. **Run the Script**  
   Execute the Python script by running.

3. **Indicate the Number of Objects to Track** <br>
   When prompted, enter the number of objects you want to track in the video.

4. **Select the Objects to Track** <br>
   Use your mouse to manually select the objects you want to track by drawing bounding boxes (ROIs) around them in the first frame.


## Output example

<img src="rbltro.gif" width="354" height="200">




The algorithm is very basic and not always robust. If you have any suggestions on
how to improve the robustness, they are very welcome.
