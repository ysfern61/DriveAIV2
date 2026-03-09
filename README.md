#  DriveAIV2

DriveAIV2, otonom sürüş sistemleri için optimize edilmiş, yüksek performanslı ve düşük gecikmeli bir nesne tespiti modelidir. Bu çalışma, gerçek zamanlı çıkarım (inference) yeteneklerini minimize edilmiş donanım kaynaklarıyla sunmayı hedefler.

---

##  1. Eğitimin Amacı ve Kapsamı
Projenin temel vizyonu, `data.yaml` veri seti üzerinde **YOLO26n** mimarisini kullanarak özelleştirilmiş bir nesne tespiti modeli geliştirmektir. 

* **Mimari:** Nano (n) serisi seçilerek düşük güç tüketimli cihazlarda (Edge AI) bile stabil FPS değerlerine ulaşılması amaçlanmıştır.
* **Hedef:** Minimum kayıp (loss) oranı ile maksimum gerçek zamanlı doğruluk.

---

##  2. Model Performans Metrikleri
Model, 100 epoch sonunda doygunluğa ulaşmış ve aşağıdaki nihai başarı skorlarını elde etmiştir:

| Metrik | Değer | Teknik Analiz |
| :--- | :---: | :--- |
| **Hassasiyet (Precision)** | **%89.8** | Modelin tespitlerinin doğruluğu yüksektir; yanlış pozitif (False Positive) oranı oldukça düşüktür. |
| **Duyarlılık (Recall)** | **%75.2** | Sahadaki nesnelerin %75.2'si başarıyla yakalanmıştır. |
| **mAP50** | **%85.0** | %50 IoU eşiğinde genel başarı puanıdır. Sınıflandırma ve konumlandırma dengesini simgeler. |
| **mAP50-95** | **%53.6** | Modelin nesne sınırlarını (bounding box) hassas bir şekilde belirleme yeteneğini gösterir. |

---

##  3. Karmaşıklık Matrisi (Confusion Matrix) Analizi
Karmaşıklık matrisi, modelin tahminleri ile gerçek etiketler arasındaki ilişkiyi temsil eder.

* **Köşegen Analizi:** Sol üstten sağ alta uzanan koyu renkli hücreler (diagonal), doğru tahmin edilen sınıfların yüzdesini yansıtır. Hücredeki değer 1.00'e yaklaştıkça modelin o sınıf üzerindeki başarısı artar.
* **Background (Arka Plan) Etkileşimi:** "Background" satır/sütununa kayan oranlar, nesnelerin arka planla karıştırılma veya atlanma durumlarını analiz etmemizi sağlar.

<p align="center">
  <img src="https://github.com/user-attachments/assets/bae716d1-ab59-4439-83ac-684779388eb7" width="700" alt="Confusion Matrix">
</p>

---

##  4. Eğitim Süreci ve Gelişim Grafikleri
100 epoch'luk eğitim süreci boyunca modelin gelişim grafikleri, sağlıklı bir öğrenme eğrisi çizmiştir.

* **Genelleme Yeteneği:** `train_loss` ve `val_loss` (hata/kayıp) değerlerinin sürekli ve uyumlu şekilde azalması, modelde **overfitting (aşırı öğrenme)** olmadığını kanıtlar.
* **Olgunlaşma:** Precision, Recall ve mAP değerleri 80. epoch civarından sonra en üst seviyelerde stabilize olmuştur.

<p align="center">
  <img src="https://github.com/user-attachments/assets/1b54fbce-f586-4f1b-b302-a0b769c06fc2" width="700" alt="Training Progress">
</p>
