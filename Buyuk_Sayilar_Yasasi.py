# Büyük sayılar Yasası
import numpy as np
rng = np.random.RandomState(123)
for i in np.arange(1,51):
    deney_sayisi = 2**i
    yazi_turalar = rng.randint(0, 2, size=deney_sayisi)
    yazi_olasiliklari = np.mean(yazi_turalar)
    print("Atış Sayısı:",deney_sayisi,"---","Yazı Olaslığı: %.2f"% (yazi_olasiliklari))


# Atış Sayısı: 2 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 4 --- Yazı Olaslığı: 0.00
# Atış Sayısı: 8 --- Yazı Olaslığı: 0.62
# Atış Sayısı: 16 --- Yazı Olaslığı: 0.44
# Atış Sayısı: 32 --- Yazı Olaslığı: 0.47
# Atış Sayısı: 64 --- Yazı Olaslığı: 0.56
# Atış Sayısı: 128 --- Yazı Olaslığı: 0.51
# Atış Sayısı: 256 --- Yazı Olaslığı: 0.53
# Atış Sayısı: 512 --- Yazı Olaslığı: 0.53
# Atış Sayısı: 1024 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 2048 --- Yazı Olaslığı: 0.49
# Atış Sayısı: 4096 --- Yazı Olaslığı: 0.49
# Atış Sayısı: 8192 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 16384 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 32768 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 65536 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 131072 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 262144 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 524288 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 1048576 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 2097152 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 4194304 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 8388608 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 16777216 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 33554432 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 67108864 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 134217728 --- Yazı Olaslığı: 0.50
# Atış Sayısı: 268435456 --- Yazı Olaslığı: 0.50

# Bir rassal değişkenin uzun vadeli kararlılığını tanımlayan olasılık teoremidir.