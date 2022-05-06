import cv2
det = cv2.QRCodeDetector()
val,_, _ = det.detectAndDecode(cv2.imread("teams.jpg"))
print(val)