import cv2
from ultralytics import YOLO


model = YOLO('runs/detect/runs/train/yolo26n_custom/weights/best.pt')


video_path = "test.mp4"
cap = cv2.VideoCapture(video_path)


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# OpenCV bazen FPS'yi çok düşük (örn. 2.95) yanlış okuyabilir, bu video yavaşlar.
# Eğer FPS değeri gerçekçi değilse standart olan 30 kabul ediyoruz:
if fps == 0 or fps < 5 or fps > 120:
    fps = 30.0


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('test_sonucu.mp4', fourcc, fps, (width, height))

fail_count = 0
while cap.isOpened():
    success, frame = cap.read()

    if success:
        fail_count = 0 # Başarılı kare okunduğunda sayacı sıfırla
        
        results = model(frame, conf=0.5)

       
        annotated_frame = results[0].plot()

        
        out.write(annotated_frame)

        
        cv2.imshow("YOLO Test", annotated_frame)

        # 'q' tuşuna basılırsa döngüden çık
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        fail_count += 1
        # Eğer peş peşe 50 kare (veya istenen sayı) okunamadıysa videonun cidden bittiğini varsayalım
        if fail_count > 50:
            print("Video tamamlandı veya çok fazla bozuk kare atlandı. Çıkılıyor...")
            break
        continue

cap.release()
out.release()
cv2.destroyAllWindows()