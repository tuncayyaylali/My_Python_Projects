# Kütüphanelerin Yüklenmesi
import pandas as pd
import seaborn as sns
import numpy as np
import researchpy as rp
import matplotlib.pyplot as plt
from scipy.stats import norm

# Örnek Veri Setinin Yüklenmesi
df = sns.load_dataset("tips")
df.head()
#    total_bill   tip     sex smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4

# Betimsel İstatistik
df.describe().T
#             count       mean       std   min      25%     50%      75%    max
# total_bill  244.0  19.785943  8.902412  3.07  13.3475  17.795  24.1275  50.81
# tip         244.0   2.998279  1.383638  1.00   2.0000   2.900   3.5625  10.00
# size        244.0   2.569672  0.951100  1.00   2.0000   2.000   3.0000   6.00

# Sayısal Değişkenler İçin Diğer Bir Betimsel İstatistik Kütüphanesi
rp.summary_cont(df[["total_bill","tip","size"]])
#      Variable      N     Mean      SD      SE  95% Conf.  Interval
# 0  total_bill  244.0  19.7859  8.9024  0.5699    18.6633   20.9086
# 1         tip  244.0   2.9983  1.3836  0.0886     2.8238    3.1728
# 2        size  244.0   2.5697  0.9511  0.0609     2.4497    2.6896

# Kategorik Değişkenler İçin Diğer Bir Betimsel İstatistik Kütüphanesi
rp.summary_cat(df[["sex","smoker","day"]])
#   Variable Outcome  Count  Percent
# 0      sex    Male    157    64.34
# 1           Female     87    35.66
# 2   smoker      No    151    61.89
# 3              Yes     93    38.11
# 4      day     Sat     87    35.66
# 5              Sun     76    31.15
# 6             Thur     62    25.41
# 7              Fri     19     7.79

# Değişkenlerin Arasındaki Kovaryansın İncelenmesi
df[["tip", "total_bill"]].cov()
#                  tip  total_bill
# tip         1.914455    8.323502
# total_bill  8.323502   79.252939

# Değişkenler Arasındaki Korelasyonun İncelenmesi
df[["tip", "total_bill"]].corr()
#                  tip  total_bill
# tip         1.000000    0.675734
# total_bill  0.675734    1.000000
# Yorum: tip ve total_bill değişkenleri arasından pozitif yönlü orta derecede bir korelasyon vardır.