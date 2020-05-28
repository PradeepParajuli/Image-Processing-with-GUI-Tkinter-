import cv2
import face_recognition


class imageAgeGenderDetect:
    def __init__(self,image_path):
        self.image_path = image_path
        # loading the image to detect
        self.image_to_detect = cv2.imread(self.image_path)             # girl.jpg


    def detect(self):
            # detect all faces in the image
            # here we can use cnn or hog , cnn is better but takes time

        all_face_location = face_recognition.face_locations(self.image_to_detect, model='hog')

            # print the number of face detected

        print('there are {} number of faces in this image'.format(len(all_face_location)))

            # looping through face locations

        for index, current_face_location in enumerate(all_face_location):
            # splitting the tuple to get the four position values

            top_pos, right_pos, bottom_pos, left_pos = current_face_location
            print('Found face {} at top:{}, right:{}, bottom:{}, left:{}'.format(index + 1, top_pos, right_pos, bottom_pos, left_pos))

            current_face_image = self.image_to_detect[top_pos:bottom_pos, left_pos:right_pos]
            cv2.imshow("Face no" + str(index + 1), current_face_image)
            #cv2.imwrite("saved_images//age_detect-.jpg".format(index+1), current_face_image)

            # the 'AGE_GENDER_MODEL_MEAN_VALUES' calculated by using the numpy.mean()
            AGE_GENDER_MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

            # create blob of current slice
            # params , image , scale, (size) , RBswap

            current_face_image_blob = cv2.dnn.blobFromImage(current_face_image, 1, (227, 227), AGE_GENDER_MODEL_MEAN_VALUES,swapRB=False)

            # declaring the labels
            gender_label_list = ['Male', 'Female']

            # declaring the file paths
            gender_protext = "gender_deploy.prototxt"
            gender_caffemodel = "gender_net.caffemodel"

            # creating the model
            gender_cov_net = cv2.dnn.readNet(gender_caffemodel, gender_protext)

            # giving input to the model
            gender_cov_net.setInput(current_face_image_blob)

            # get the predictions from the model
            gender_predictions = gender_cov_net.forward()

            # find the max value of predictions index
            # pass index to label array and get the label text
            gender = gender_label_list[gender_predictions[0].argmax()]

            # predicting age
            age_label_list = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

            # declaring the file paths
            age_protext = "age_deploy.prototxt"
            age_caffemodel = "age_net.caffemodel"

            # creating the model
            age_cov_net = cv2.dnn.readNet(age_caffemodel, age_protext)

            # giving input to the model
            age_cov_net.setInput(current_face_image_blob)

            # get the predictions from the model
            age_predictions = age_cov_net.forward()

            # find the max value of predictions index
            # pass index to label array and get the label text
            age = age_label_list[age_predictions[0].argmax()]

            # draw rectangle around face detected
            cv2.rectangle(self.image_to_detect, (left_pos, top_pos), (right_pos, bottom_pos), (0, 0, 255), 2)

            # display the name as text in the image
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(self.image_to_detect, gender + " " + age + "yrs", (left_pos, bottom_pos), font, 0.5, (0, 255, 0), 1)

            # showing the current frame with rectangle box
            print(index,"  -->age : ",age,"  gender: ",gender)
        cv2.imshow("Age and Gender", self.image_to_detect)

        # save the image
        image_name = self.image_path.split("/")[-1][:-4]
        cv2.imwrite('Saved Images//{} Image Age and Gender.jpg'.format(image_name),self.image_to_detect)

        cv2.waitKey(1) & 0xFF == ord('q')

