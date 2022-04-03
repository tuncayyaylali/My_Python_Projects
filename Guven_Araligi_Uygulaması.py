# Kütüphanelerin Yüklenmesi
import numpy as np

# Rassal Olarak Fiyat Listesi Oluşturma
fiyatlar = np.random.randint(10,110,1000)
fiyatlar[0:10]
# array([104,  33,  10,  85,  46,  90,  71,  88,  35,  34])
fiyatlar.mean()
# 58.529

# Diğer Kütüphanelerin Yüklenmesi
import statsmodels.stats.api as sms
sms.DescrStatsW(fiyatlar).tconfint_mean()
# (56.74607410683151, 60.3119258931685)

# Yorum: Yukarıdaki fiyatlar % 95 güvenle 56.74607410683151 ve 60.3119258931685 arasındadır.