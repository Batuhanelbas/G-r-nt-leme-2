# Batuhan Elbaş 02205076009

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Gri seviye görüntüyü yükleyin
image = cv2.imread('indir.jpeg', cv2.IMREAD_GRAYSCALE)

# Histogramı hesaplayın
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Histogramı normalize edin (isteğe bağlı)
hist = hist / hist.sum()

# Histogramı çizin
plt.plot(hist)
plt.title('Gri Seviye Görüntü Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.xlim([0, 256])
plt.show()