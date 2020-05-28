import face_recognition
from PIL import Image,ImageDraw


class faceMakeup:
    def __init__(self,image_path):
        self.image_path = image_path

    def makeup(self):
        # load the image file
        face_image = face_recognition.load_image_file(self.image_path)

        # get the face landmarks list
        face_landmarks_list = face_recognition.face_landmarks(face_image)

        # print the face landmarks list
        print(face_landmarks_list)

        for face_landmarks in face_landmarks_list:
            # convert the numpy array image into pil image object
            pil_image = Image.fromarray(face_image)

            # convert the pil image to draw image
            d = ImageDraw.Draw(pil_image, 'RGBA')

            # draw the shapes and fill with color

            # make left,right eyebrow darker
            # polygon on top and line on bottom with dark color
            d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
            d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
            d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128), width=2)
            d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128), width=2)

            # add lipstick to top and bottom lips
            # using red polygon and eyes filled with red
            d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
            d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
            d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 128), width=2)
            d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128), width=2)

            # join each face landmark points
            # d.line(face_landmarks['chin'], fill=(255,255,255), width=10)
            # d.line(face_landmarks['left_eyebrow'], fill=(255, 255, 255), width=1)
            # d.line(face_landmarks['right_eyebrow'], fill=(255, 255, 255), width=0)
            # d.line(face_landmarks['nose_bridge'], fill=(255, 255, 255), width=1)
            # d.line(face_landmarks['nose_tip'], fill=(255, 255, 255), width=1)
            # d.line(face_landmarks['left_eye'], fill=(255, 255, 255), width=1)
            # d.line(face_landmarks['right_eye'], fill=(255, 255, 255), width=1)
            # d.line(face_landmarks['top_lip'], fill=(255, 255, 255), width=1)
            # d.line(face_landmarks['bottom_lip'], fill=(255, 255, 255), width=1)

        # show the final image
        pil_image.show()

        # save the image
        image_name = self.image_path.split("/")[-1][:-4]
        pil_image.save('Saved Images//{} -- Face Makeup.jpg'.format(image_name))