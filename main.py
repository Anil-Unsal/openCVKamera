import cv2

# Bilgisayar için kamera erişimi
cap = cv2.VideoCapture(0)

# Raspberry Pi'ye geçtiğinde bu satırı kullan (YORUM SATIRI ŞU AN)
# cap = cv2.VideoCapture("/dev/video0")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Görüntü alınamadı.")
        break

    cv2.imshow("Kamera Görüntüsü", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
