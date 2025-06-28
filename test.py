import cv2
img = cv2.imread(r"C:\Users\HP\OneDrive\Desktop\pythonncodes\data\user.1.38.jpg", cv2.IMREAD_GRAYSCALE)
clf = cv2.face.LBPHFaceRecognizer.create()
clf.read("classifier.xml")
label, dist = clf.predict(img)
print("Predicted label:", label, " distance:", dist)