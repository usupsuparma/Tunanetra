import time
import RPi.GPIO as GPIO
import  string, time
import numpy as np
import argparse
import cv2
import os
import time
from serial import Serial



# class deteksi objek
class Klasifikasi():
	__image = "test.jpg"

	def __init__(self,img):
		self.__image = img

	def identifikasi(self):
		CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
			"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
			"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
			"sofa", "train", "tvmonitor"]
		COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

		print("[INFO] loading model...")
		net = cv2.dnn.readNetFromCaffe("proto.txt", "model.caffemodel")

		image = cv2.imread(self.__image)
		(h, w) = image.shape[:2]
		blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

		print("[info] computing object detections")
		net.setInput(blob)
		detections = net.forward()

		#loop over the detections
		for i in np.arange(0, detections.shape[2]):
			# extract the confidence (i.e., probability) associated with the
		    # prediction
			confidence = detections[0, 0, i, 2]

			if confidence > args["confidence"]:
				idx = int(detections[0,0,i,1])
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")


				#display the prediction
				label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
				print("[INFO] {}".format(label))
				cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)

				y = startY - 15 if startY - 15 > 15 else startY + 15
				cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

				# menampilkan hasil
				# cv2.imshow("output",image)
				# cv2.waitKey(0)

				return label

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--confidence", type=float, default=0.8,
                help="minimum probability to filter weak detections")
args = vars(ap.parse_args())


# main program
print("=="*15)
print("== Program Berjalan ==")
print("=="*15)
output = (" ")
ser = serial.Serial('/dev/ttyACM0', 9600)


try:
    while True:
        output =int(ser.readline())
        print("data jarak: ", output)
        if output > 50:
            print(output)
            print("jarak aman")
        elif output < 50:
            print("jarak bahaya")
            jumlah = 0
            vidio = cv2.VideoCapture(0)
            cond , frame = vidio.read()
            cv2.imshow("Take Picture", frame)
            sleep(2)
            cv2.imwrite("user.jpg",frame)
            konek = Klasifikasi("user.jpg")
            if konek == "none":
                print("Data tidak ditemukan")
            else:
                show = konek.identifikasi()
                print(show[0:6])
                if show[0:6] == "person":
                    print("manusia terdeteksi")
                elif show[0:9] == "motorbike":
                    print("motor terdeteksi")
                elif show[0:3] == "car":
                    print("mobil terdeteksi")
                elif show[0:5] == "chair":
                    print("kursi terdeteksi")

            print("hasil uji: ",show)
            os.remove("user.jpg")
            jumlah += 1
        else:
            print("data jarak tidak ada")

except KeyboardInterrupt:
    # gunakan ctrl + c
    GPIO.cleanup()
