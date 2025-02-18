import cv2
import numpy as np

# Open the video
video_path = "kuramoto7.mp4"  # Path to your video file
cap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the video's width, height, and frames per second (fps)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create a VideoWriter object to save the output video
output_path = "output_video.mp4"  # Path to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for mp4
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Create a background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

# Ask user for the number of objects to track
num_objects = int(input("Enter the number of objects to track: "))

# Initialize list for trackers and paths
trackers = []
paths = [[] for _ in range(num_objects)]  # List of lists to store the paths of each object

# Read the first frame from the video
ret, frame = cap.read()

# Loop to select ROIs for each object
for i in range(num_objects):
    print(f"Select ROI for object {i+1}")
    # Select ROI manually for each object
    roi = cv2.selectROI("Select Object", frame, fromCenter=False, showCrosshair=True)
    x, y, w, h = roi

    # Initialize the tracker for this object
    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, (x, y, w, h))

    # Add the tracker to the list
    trackers.append(tracker)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Update trackers
    for i, tracker in enumerate(trackers):
        ret, bbox = tracker.update(frame)

        if ret:
            x, y, w, h = [int(v) for v in bbox]
            center = (x + w // 2, y + h // 2)
            radius = int(min(w, h) / 2)

            # Add the current position to the path
            paths[i].append(center)

            # Draw the circle around the object
            cv2.circle(frame, center, radius, (255, 140, 0), 5)  # Black circle around the object

            # Draw the path (line connecting previous positions)
            for j in range(1, len(paths[i])):
                cv2.line(frame, paths[i][j - 1], paths[i][j], (30,144,255), 2)  # Blue path line

        else:
            cv2.putText(frame, f"Tracking failure for object {i+1}", (100, 80 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)  # Red text

    # Write the frame with the tracked objects to the output video
    out.write(frame)

    # Display the frame with the tracked objects
    cv2.imshow("Object Tracking", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects, and close all OpenCV windows
cap.release()
out.release()
cv2.destroyAllWindows()



