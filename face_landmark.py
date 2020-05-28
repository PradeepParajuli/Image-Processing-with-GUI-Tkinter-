import face_recognition
import cv2
from PIL import Image,ImageDraw

class faceLandmark:

    def __init__(self, image_path):
        self.image_path = image_path
        # load the image file
        self.face_image = face_recognition.load_image_file(self.image_path)

        # get the face landmarks list
        self.face_landmarks_list = face_recognition.face_landmarks(self.face_image)

        # print the face landmarks list
        print(self.face_landmarks_list)

    def landmarks(self):
        for face_landmarks in self.face_landmarks_list:
            # convert the numpy array image into pil image object
            pil_image = Image.fromarray(self.face_image)

            # convert the pil image to draw image
            d = ImageDraw.Draw(pil_image)

            # join each face landmark points
            d.line(face_landmarks['chin'], fill=(255,255,255), width=10)
            d.line(face_landmarks['left_eyebrow'], fill=(255, 255, 255), width=10)
            d.line(face_landmarks['right_eyebrow'], fill=(255, 255, 255), width=10)
            d.line(face_landmarks['nose_bridge'], fill=(255, 255, 255), width=10)
            d.line(face_landmarks['nose_tip'], fill=(255, 255, 255), width=10)
            d.line(face_landmarks['left_eye'], fill=(255, 255, 255), width=10)
            d.line(face_landmarks['right_eye'], fill=(255, 255, 255), width=10)
            d.line(face_landmarks['top_lip'], fill=(255, 255, 255), width=10)
            d.line(face_landmarks['bottom_lip'], fill=(255, 255, 255), width=10)

            # show the final image
            pil_image.show()


            # save the image
            image_name = self.image_path.split("/")[-1]
            pil_image.save('Saved Images//{} -- Face Landmarks.jpg'.format(image_name))
