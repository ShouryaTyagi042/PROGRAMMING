import cv2
video_reader = cv2.VideoCapture(0)  # ZERO stands for reding with webcamera

while True:
    # we use .read() to read the video, it returns a boolean and frame , when video stops it returns false ;
    success, frame = video_reader.read()
    if not success:
        break

    cv2.imshow("MyVideo", frame)
    # python returns unicode value
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
video_reader.release()
cv2.destroyAllWindows()
