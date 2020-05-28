import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk,Image

# importing packages
from face_landmark import faceLandmark
from face_landmark_makeup import faceMakeup
from img_face_detection import imageFaceDetection
from image_face_recognition import imageFaceRecognition
from image_age_gender import imageAgeGenderDetect
from realtime_face_detection_blur import realtimeFaceBlur
from realtime_face_detection import realtimeFaceDetect
from realtime_face_recognition import realtimeFaceRecognition


class main_page:
    def __init__ (self, window):
        self.window = window
        self.window.title("Image Processing")
        self.window.geometry("1350x700")
        self.window.resizable(width=False, height=False)

        # Background Image
        #self.bg_icon = ImageTk.PhotoImage(file = "Program_images/bg_image.jpg")
        #bg_lbl = Label(self.window, image = "Program_images/bg_image.jpg")

        # All variables here
        self.topics_names = ["Image Landmark", "Image Face Detection", "Image Face Recognition", "Image Age and Gender",
                        "Realtime Face Blur", "Realtime Face Detection", "Realtime  Face Recognition"]

        self.btn_commands = [lambda: screen.image_landmark(screen.dummy()),
                        lambda: screen.image_face_detection(screen.dummy()),
                        lambda: screen.image_face_recognition(screen.dummy()),
                        lambda: screen.image_age_gender(screen.dummy()),
                        lambda: screen.realtime_face_blur(screen.dummy()),
                        lambda: screen.realtime_face_detection(screen.dummy()),
                        lambda: screen.realtime_face_recognition(screen.dummy())]

        self.image_path = "Images.jpg"


        # ---- Lables -------------------------
        title = tk.Label(self.window, text="Image Processing", font=("times new roman", 40, "bold"),
                      bg="#BFCEFF", fg="red", bd=10, relief=tk.GROOVE)
        title.place(x=0, y=0, relwidth=1)

    def open_file(self):
        """Open and select image for processing"""
        filepath = askopenfilename(filetypes=[("Image Files", ("*.jpg", "*.png")), ("All Files", "*.*")])
        if not filepath:
            return
        return filepath

    def dummy(self):
        # frame 1
        frm1 = tk.Frame(self.window, bd=4, relief=tk.RIDGE, bg="white")
        frm1.place(x=25, y=160, width=645, height=510)

        # frame 2
        frm2 = tk.Frame(self.window, bd=4, relief=tk.RIDGE, bg="white")
        frm2.place(x=670, y=160, width=645, height=510)
        return (frm1, frm2)

    def lowerPart(self):
        frm = tk.Frame(self.window, bd=4, relief=tk.RIDGE, bg="#007AA8")
        frm.place(x=20, y=155, width=1300, height=520)

    def options_bar(self):
        # Frame options
        frm_options = tk.Frame(self.window, bd=4, relief=tk.RIDGE, bg="#007AA8")
        frm_options.place(x=20, y=100, width=1300, height=50)
        # making all option buttons

        for index, text in enumerate(self.topics_names):
            # creating label widget with the text form
            options_btn = tk.Button(master=frm_options, text=text, width=25, height=2, command=self.btn_commands[index])
            options_btn.grid(row=0, column=index, sticky=tk.NS)

        # calling lower part
        screen.lowerPart()
        #screen.image_landmark(screen.dummy())

    def btn_select_image(self, frm2):
        self.image_path = screen.open_file()
        if self.image_path:
            image_name = self.image_path.split("/")[-1]

            # frm 2
            tk.Label(master=frm2, text=image_name, bg="#007AA8", fg="white",
                     font=("times new roman", 20, "bold")).place(x=0, y=0, relwidth=1)

            # image
            photo = Image.open(self.image_path)
            photo = photo.resize((600, 400), Image.ANTIALIAS)
            photo.save("ArtWrk.ppm")

            img = ImageTk.PhotoImage(Image.open("ArtWrk.ppm"))
            image_frame = tk.Label(frm2, bd=4, image=img)
            image_frame.image = img
            image_frame.place(x=0, y=40)

    def btn_run(self,image_path,index):
        if index == 0:
            landmark = faceLandmark(image_path)
            landmark.landmarks()

        elif index == 1:
            detect = imageFaceDetection(self.image_path)
            detect.detect_face()

        elif index == 2:
            recognition = imageFaceRecognition(self.image_path)
            recognition.encoding()

        elif index == 3:
            detect = imageAgeGenderDetect(self.image_path)
            detect.detect()

        elif index == 4:
            face_blur = realtimeFaceBlur()
            face_blur.blur()

        elif index == 5:
            detect = realtimeFaceDetect()
            detect.detect()

        elif index == 6:
            recognise = realtimeFaceRecognition()
            recognise.recognise()

        elif index == 7:
            makeup = faceMakeup(self.image_path)
            makeup.makeup()

    def image_landmark(self, dummy):
        frm1 = dummy[0]
        frm2 = dummy[1]

        # frm 1
        tk.Label(master=frm1, text="Image Landmark", bg="#007AA8", fg="white", font=("times new roman", 20)).pack(fill=tk.X)

        # frm 2
        tk.Label(master=frm2, text="Selected Image", bg="#007AA8", fg="white", font=("times new roman", 20, "bold")).pack(fill=tk.X)

        # creating btns
        btns_frame = tk.Frame(master=frm1, relief=tk.RIDGE, bg="white")
        btns_frame.pack(fill=tk.BOTH)

        btn_select = tk.Button(master=btns_frame, text="Select Image", width=25, height=2,
                               command=lambda: screen.btn_select_image(frm2))
        btn_select.grid(row=0, column=0, sticky=tk.NS, padx=15, pady=10)

        btn_run = tk.Button(master=btns_frame, text="Run", width=25, height=2,
                            command=lambda: screen.btn_run(self.image_path, 0))
        btn_run.grid(row=0, column=1, sticky=tk.NS, padx=15, pady=10)

        # makeup
        makeup_label = tk.Label(master=btns_frame, text="Makeup Selected Image", bg="white", fg="Black", font=("times new roman", 20, "bold"))
        makeup_label.grid(row=1, column =1,sticky=tk.N, padx=15, pady=10)

        # run makeup
        btn_run = tk.Button(master=btns_frame, text="Run", width=25, height=2,
                            command=lambda: screen.btn_run(self.image_path, 7))
        btn_run.grid(row=2, column=1, sticky=tk.NS, padx=15, pady=10)

    def image_face_detection(self, dummy):
        frm1 = dummy[0]
        frm2 = dummy[1]

        # frm 1
        tk.Label(master=frm1, text="Image Face Detection", bg="#007AA8", fg="white", font=("times new roman", 20)).pack(
            fill=tk.X)

        # frm 2
        tk.Label(master=frm2, text="Selected Image", bg="#007AA8", fg="white",
                 font=("times new roman", 20, "bold")).pack(fill=tk.X)

        # creating btns
        btns_frame = tk.Frame(master=frm1, relief=tk.RIDGE, bg="white")
        btns_frame.pack(fill=tk.BOTH)

        options_btn = tk.Button(master=btns_frame, text="Select Image", width=25, height=2,
                                command=lambda: screen.btn_select_image(frm2))

        options_btn.grid(row=0, column=0, sticky=tk.NS, padx=15, pady=10)

        options_btn = tk.Button(master=btns_frame, text="Run", width=25, height=2,
                                command=lambda: screen.btn_run(self.image_path, 1))
        options_btn.grid(row=0, column=1, sticky=tk.NS, padx=15, pady=10)

    def image_face_recognition(self, dummy):
        frm1 = dummy[0]
        frm2 = dummy[1]

        # frm 1
        tk.Label(master=frm1, text="Image Face Recognition", bg="#007AA8", fg="white", font=("times new roman", 20)).pack(
            fill=tk.X)

        # frm 2
        tk.Label(master=frm2, text="Selected Image", bg="#007AA8", fg="white",
                 font=("times new roman", 20, "bold")).pack(fill=tk.X)

        # creating btns
        btns_frame = tk.Frame(master=frm1, relief=tk.RIDGE, bg="white")
        btns_frame.pack(fill=tk.BOTH)

        options_btn = tk.Button(master=btns_frame, text="Select Image", width=25, height=2,
                                command=lambda: screen.btn_select_image(frm2))

        options_btn.grid(row=0, column=0, sticky=tk.NS, padx=15, pady=10)

        options_btn = tk.Button(master=btns_frame, text="Run", width=25, height=2,
                                command=lambda: screen.btn_run(self.image_path, 2))
        options_btn.grid(row=0, column=1, sticky=tk.NS, padx=15, pady=10)

    def image_age_gender(self, dummy):
        frm1 = dummy[0]
        frm2 = dummy[1]

        # frm 1
        tk.Label(master=frm1, text="Image Age Gender Detection", bg="#007AA8", fg="white", font=("times new roman", 20)).pack(
            fill=tk.X)

        # frm 2
        tk.Label(master=frm2, text="Selected Image", bg="#007AA8", fg="white",
                 font=("times new roman", 20, "bold")).pack(fill=tk.X)

        # creating btns
        btns_frame = tk.Frame(master=frm1, relief=tk.RIDGE, bg="white")
        btns_frame.pack(fill=tk.BOTH)

        options_btn = tk.Button(master=btns_frame, text="Select Image", width=25, height=2,
                                command=lambda: screen.btn_select_image(frm2))

        options_btn.grid(row=0, column=0, sticky=tk.NS, padx=15, pady=10)

        options_btn = tk.Button(master=btns_frame, text="Run", width=25, height=2,
                                command=lambda: screen.btn_run(self.image_path, 3))
        options_btn.grid(row=0, column=1, sticky=tk.NS, padx=15, pady=10)

    def realtime_face_blur(self, dummy):
        frm1 = dummy[0]
        frm2 = dummy[1]

        # frm 1
        tk.Label(master=frm1, text="Realtime Face Blur", bg="#007AA8", fg="white", font=("times new roman", 20)).pack(
            fill=tk.X)

        # # frm 2
        # tk.Label(master=frm2, text="Selected Image", bg="#007AA8", fg="white",
        #          font=("times new roman", 20, "bold")).pack(fill=tk.X)

        # creating btns
        btns_frame = tk.Frame(master=frm1, relief=tk.RIDGE, bg="white")
        btns_frame.pack(fill=tk.BOTH)



        options_btn = tk.Button(master=btns_frame, text="Run", width=25, height=2,
                                command=lambda: screen.btn_run(self.image_path, 4))
        options_btn.grid(row=0, column=0, sticky=tk.NS, padx=15, pady=10)

    def realtime_face_detection(self, dummy):
        frm1 = dummy[0]
        frm2 = dummy[1]

        # frm 1
        tk.Label(master=frm1, text="Realtime Face Detection", bg="#007AA8", fg="white", font=("times new roman", 20)).pack(
            fill=tk.X)

        # frm 2
        # tk.Label(master=frm2, text="Selected Image", bg="#007AA8", fg="white",
        #          font=("times new roman", 20, "bold")).pack(fill=tk.X)

        # creating btns
        btns_frame = tk.Frame(master=frm1, relief=tk.RIDGE, bg="white")
        btns_frame.pack(fill=tk.BOTH)

        options_btn = tk.Button(master=btns_frame, text="Run", width=25, height=2,
                                command=lambda: screen.btn_run(self.image_path, 5))
        options_btn.grid(row=0, column=0, sticky=tk.NS, padx=15, pady=10)

    def realtime_face_recognition(self, dummy):
        frm1 = dummy[0]
        frm2 = dummy[1]

        # frm 1
        tk.Label(master=frm1, text="Realtime Face Recognition", bg="#007AA8", fg="white", font=("times new roman", 20)).pack(
            fill=tk.X)

        # frm 2
        # tk.Label(master=frm2, text="Selected Image", bg="#007AA8", fg="white",
        #          font=("times new roman", 20, "bold")).pack(fill=tk.X)

        # creating btns
        btns_frame = tk.Frame(master=frm1, relief=tk.RIDGE, bg="white")
        btns_frame.pack(fill=tk.BOTH)

        options_btn = tk.Button(master=btns_frame, text="Run", width=25, height=2,
                                command=lambda: screen.btn_run(self.image_path, 6))
        options_btn.grid(row=0, column=1, sticky=tk.NS, padx=15, pady=10)



window = tk.Tk()
screen = main_page(window)
screen.options_bar()
window.mainloop()
