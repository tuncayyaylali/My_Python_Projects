# Kütüphanelerin Yüklenmesi
import pandas as pd
import seaborn as sns
import numpy as np
import researchpy as rp
import matplotlib.pyplot as plt
from scipy.stats import norm

# Rassal Olarak Bir Popülasyon Oluşturulması
np.random.seed(15) # Her seferinde aynı rassal değerlerin elde edilmesi için kullanılır.
population = np.random.randint(0,80,10000)

# Popülasyon Ortalaması
population.mean()
# 39.6116

# Örneklem Çekme ve Örneklem Ortalaması
orneklem = np.random.choice(a=population, size=100)
orneklem.mean()
# 38.11

# Daha Fazla Sayıda Örneklem Çekilmesi
orneklem1=np.random.choice(a=population, size=100)
orneklem2=np.random.choice(a=population, size=100)
orneklem3=np.random.choice(a=population, size=100)
orneklem4=np.random.choice(a=population, size=100)
orneklem5=np.random.choice(a=population, size=100)
orneklem6=np.random.choice(a=population, size=100)
orneklem7=np.random.choice(a=population, size=100)
orneklem8=np.random.choice(a=population, size=100)
orneklem9=np.random.choice(a=population, size=100)
orneklem10=np.random.choice(a=population, size=100)

# Örneklemlerin Ortalaması
orneklem_ort = [orneklem.mean(), orneklem1.mean(), orneklem2.mean(), orneklem3.mean(), orneklem4.mean(),
                orneklem5.mean(), orneklem6.mean(), orneklem7.mean(), orneklem8.mean(), orneklem9.mean(),
                orneklem10.mean()]
sum(orneklem_ort)/len(orneklem_ort)
# 39.70181818181819

# Grafiklerin Çizdirilmesi
sns.distplot(orneklem_ort)
plt.axvline(population.mean(), color='r', linestyle='-')
plt.show()

# Yorum: Örneklemler ortalamaları popülasyon ortalamaları civarında normal dağılıma uyacak şekilde çıkar.