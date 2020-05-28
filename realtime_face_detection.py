import cv2
import face_recognition


class realtimeFaceDetect:
    def detect(self):
        # capture the video from default camera

        webcam_video_stream = cv2.VideoCapture(0)

        # initialize the array variable to hold the all face location in the frame
        all_face_location = []

        # loop through every frame in the video

        while True:
            # get the current frame from the video stream as an image
            ret, current_frame = webcam_video_stream.read()
            # resize the current frame to 1/4 size to process faster
            current_frame_small = cv2.resize(current_frame,(0,0),fx=0.25,fy=0.25)

            # detect all faces in the image
            # here we can use cnn or hog , cnn is better but takes time

            all_face_location = face_recognition.face_locations(current_frame_small,number_of_times_to_upsample=2, model='hog')

            # looping through face locations
            for index, current_face_location in enumerate(all_face_location):
                # splitting the tuple to get the four position values

                top_pos, right_pos, bottom_pos, left_pos = current_face_location

                # change the position maginitude to fit the actual size video frame

                top_pos = top_pos*4
                right_pos = right_pos*4
                bottom_pos = bottom_pos*4
                left_pos = left_pos*4

                # printing the location of current face

                print('Found face {} at top:{}, right:{}, bottom:{}, left:{}'.format(index + 1, top_pos, right_pos, bottom_pos,left_pos))

                # draw rectangle around face detected

                cv2.rectangle(current_frame, (left_pos,top_pos),(right_pos,bottom_pos),(0,0,255),2)

            # showing the current frame with rectangle box
            cv2.imshow("Webcam Video",current_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # release the stream and cam
        # close all opencv windows open
        webcam_video_stream.release()
        cv2.destroyAllWindows()




