import cv2

# Bilgisayar için kamera erişimi
cap = cv2.VideoCapture(0)

# Raspberry Pi için (yorum satırı)
# cap = cv2.VideoCapture("/dev/video0")

# Haar Cascade yüz tanıma modeli (OpenCV ile gelen)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Görüntü alınamadı.")
        break

    # Gri tonlara çeviriyoruz (yüz tanıma için daha hızlı)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Her yüz için dikdörtgen çiz
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Yeşil kutu

    cv2.imshow("Kamera Görüntüsü - Yüz Tespiti", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
