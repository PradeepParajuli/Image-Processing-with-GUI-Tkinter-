import cv2
import face_recognition


class imageFaceDetection:
    def __init__(self, image_path):
        self.image_path = image_path
        # loading the image to detect
        self.image_to_detect = cv2.imread(self.image_path) # img1

    def detect_face(self):
        # detect all faces in the image
        # here we can use cnn or hog , cnn is better but takes time

        all_face_location = face_recognition.face_locations(self.image_to_detect, model='cnn')

        # print the number of face detected

        print('there are {} number of faces in this image'.format(len(all_face_location)))

        # looping through face locations

        for index, current_face_location in enumerate(all_face_location):
            # splitting the tuple to get the four position values

            top_pos, right_pos, bottom_pos, left_pos = current_face_location
            print('Found face {} at top:{}, right:{}, bottom:{}, left:{}'.format(index+1, top_pos, right_pos, bottom_pos, left_pos))

            current_face_image = self.image_to_detect[top_pos:bottom_pos, left_pos:right_pos]
            cv2.imshow("Face no" + str(index+1), current_face_image)

            # save the image
            image_name = self.image_path.split("/")[-1]
            cv2.imwrite('Saved Images//{} -- Face Detection.jpg'.format(image_name),current_face_image)

        cv2.waitKey(1) & 0xFF == ord('q')


