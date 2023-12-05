import cv2
import numpy as np

# Create an object to read camera video 
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Camera is unable to open.")

# Set resolutions of frame.
# convert from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Create VideoWriter object.
# and store the output in 'captured_video.avi' file.

video_cod = cv2.VideoWriter_fourcc(*'XVID')
video_output= cv2.VideoWriter('captured_video.avi',
                      video_cod,
                      10,
                      (frame_width,frame_height))

while(True):
  ret, frame = cap.read()

  if ret == True: 
    
    # Write the frame into the file 'captured_video.avi'
    video_output.write(frame)

    # Display the frame, saved in the file   
    cv2.imshow('frame',frame)

    # Press x on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('x'):
      break

  # Break the loop
  else:
    break  

# release video capture
# and video write objects
cap.release()
video_output.release()

# Closes all the frames
cv2.destroyAllWindows() 

print("The video was successfully saved") 
