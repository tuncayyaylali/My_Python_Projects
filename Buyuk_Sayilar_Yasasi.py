# Büyük sayılar Yasası
import numpy as np
rng = np.random.RandomState(123)
for i in np.arange(1,51):
    deney_sayisi = 2**i
    yazi_turalar = rng.randint(0, 2, size=deney_sayisi)
    yazi_olasiliklari = np.mean(yazi_turalar)
    print("Atış Sayısı:",deney_sayisi,"---",'Yazı Olaslığı: %.2f' % (yazi_olasiliklari*100))


# Atış Sayısı: 2 --- Yazı Olaslığı: 50.00
# Atış Sayısı: 4 --- Yazı Olaslığı: 0.00
# Atış Sayısı: 8 --- Yazı Olaslığı: 62.50
# Atış Sayısı: 16 --- Yazı Olaslığı: 43.75
# Atış Sayısı: 32 --- Yazı Olaslığı: 46.88
# Atış Sayısı: 64 --- Yazı Olaslığı: 56.25
# Atış Sayısı: 128 --- Yazı Olaslığı: 50.78
# Atış Sayısı: 256 --- Yazı Olaslığı: 52.73
# Atış Sayısı: 512 --- Yazı Olaslığı: 52.93
# Atış Sayısı: 1024 --- Yazı Olaslığı: 50.20
# Atış Sayısı: 2048 --- Yazı Olaslığı: 48.58
# Atış Sayısı: 4096 --- Yazı Olaslığı: 49.49
# Atış Sayısı: 8192 --- Yazı Olaslığı: 49.58
# Atış Sayısı: 16384 --- Yazı Olaslığı: 49.96
# Atış Sayısı: 32768 --- Yazı Olaslığı: 50.00
# Atış Sayısı: 65536 --- Yazı Olaslığı: 49.68
# Atış Sayısı: 131072 --- Yazı Olaslığı: 49.97
# Atış Sayısı: 262144 --- Yazı Olaslığı: 50.13
# Atış Sayısı: 524288 --- Yazı Olaslığı: 50.01
# Atış Sayısı: 1048576 --- Yazı Olaslığı: 50.09
# Atış Sayısı: 2097152 --- Yazı Olaslığı: 50.01
# Atış Sayısı: 4194304 --- Yazı Olaslığı: 50.03
# Atış Sayısı: 8388608 --- Yazı Olaslığı: 50.05
# Atış Sayısı: 16777216 --- Yazı Olaslığı: 50.01
# Atış Sayısı: 33554432 --- Yazı Olaslığı: 50.01
# Atış Sayısı: 67108864 --- Yazı Olaslığı: 50.00
# Atış Sayısı: 134217728 --- Yazı Olaslığı: 50.00
# Atış Sayısı: 268435456 --- Yazı Olaslığı: 50.00

# Bir rassal değişkenin uzun vadeli kararlılığını tanımlayan olasılık teoremidir.