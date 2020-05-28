# importing the required libraries
import cv2
import face_recognition


class imageFaceRecognition:
    def __init__(self,image_path):
        self.image_path = image_path
        # loading the image to detect
        self.original_image = cv2.imread(self.image_path)    # test.jpg

    def encoding(self):
        modi_image = face_recognition.load_image_file('image recognition//modi.jpg')
        modi_face_encodings = face_recognition.face_encodings(modi_image)[0]

        trump_image = face_recognition.load_image_file('image recognition//trump.jpg')
        trump_face_encodings = face_recognition.face_encodings(trump_image)[0]

        pradeep_image = face_recognition.load_image_file('image recognition//pradeep.JPG')
        pradeep_face_encodings = face_recognition.face_encodings(pradeep_image)[0]


        # save the encodings and the corresponding labels in seperate arrays in the same order
        known_face_encodings = [modi_face_encodings, trump_face_encodings, pradeep_face_encodings]
        known_face_names  = ["Narendra Modi", "Donald trump", "Pradeep Parajuli"]

        # load the unkwown image to recognize faces in it
        image_to_recognize = face_recognition.load_image_file(self.image_path)  # test.jpg

        # detect all faces in the image
        # arguments are image, no_of_times_to_upsample, model
        # here we can use cnn or hog , cnn is better but takes time

        all_face_locations = face_recognition.face_locations(image_to_recognize,model='hog')

        # detect face encodings for all the faces detected
        all_face_encodings = face_recognition.face_encodings(image_to_recognize, all_face_locations)

        # print the number of face detected
        print('there are {} number of faces in this image'.format(len(all_face_locations)))

        # looping through face locations and face embeddings
        for current_face_location, current_face_encoding in zip(all_face_locations, all_face_encodings):

            # splitting the tuple to get the four position values
            top_pos, right_pos, bottom_pos, left_pos = current_face_location

            # find all the matches and get the list of matches
            all_matches = face_recognition.compare_faces(known_face_encodings, current_face_encoding)

            # string to holt the label
            name_of_person = 'unknown face'

            # check if the all matches have atleast one item
            # if yes, get the index number of face that is located in the first index of all_matches
            if True in all_matches:
                first_match_index = all_matches.index(True)
                name_of_person = known_face_names[first_match_index]

            # draw rectangle around face detected
            cv2.rectangle(self.original_image, (left_pos, top_pos), (right_pos, bottom_pos), (255, 0, 0), 2)

            # display the name as text in the image
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(self.original_image, name_of_person, (left_pos,bottom_pos), font, 0.5, (255, 255, 255),1)

            # display the image
            cv2.imshow("Faces identified", self.original_image)

            # save the image
            image_name = self.image_path.split("/")[-1]
            cv2.imwrite('Saved Images//{} -- Face Recognition.jpg'.format(image_name), self.original_image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

