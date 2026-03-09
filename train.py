from ultralytics import YOLO
import os

if __name__ == '__main__':
    dataset_path = r"C:\Users\yusuferencihan\Desktop\Projeler\DriveAIV2\dataset\data.yaml"


    model = YOLO("yolo26n.pt")  

    # 3. Eğitim Başlatma
    results = model.train(
        data=dataset_path,
        epochs=100,
        imgsz=640,
        batch=-1,           
        patience=30,        
        save=True,
        save_period=20,     
        augment=True,       
        project="runs/train",
        name="yolo26n_custom",
        exist_ok=True,      
        device=0         
    )
    model = YOLO("yolo26n.pt")  