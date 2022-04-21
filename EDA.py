# KÜTÜPHANELERİN YÜKLENMESİ

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# PANDAS AYARLARI
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# VERİ SETİNİN YÜKLENMESİ
df = sns.load_dataset("titanic")

# DEĞİŞKENLERİN YAKALANMASI


def grab_col_names(dataframe, cat_th=10,  car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        Değişken isimlerinin alınmak istendiği dataframe' dir.
    cat_th: int, float
        Nümerik fakat kategorik olan değişkenler için sınıf eşik değeridir. Varsayılan değeri 10' dur.
    car_th: int, float
        Kategorik fakat kardinal değişkenler için sınıf eşik değeridir. Varsayılan değeri 20' dir.

    Returns
    -------
    cat_cols: list
        Kategorik değişkenlerin listesidir.
    num_cols: list
        Numerik değişkenlerin listesidir.
    cat_but_car: list
        Kategorik görünümlü kardinal değişkenlerin listesidir.

    Notes
    ------
    Toplam Değişken Sayısı = cat_cols + num_cols + cat_but_car
    Önemli Not: num_but_cat cat_cols' un içerisinde olduğu yukarıdaki toplamda ayrıca yer almamaktadır.

    """
    # cat_cols
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["category", "object", "bool"]]
    # num_bat_car
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < 10 and dataframe[col].dtypes in ["int", "float"]]
    # cat_but_car
    cat_but_car = [col for col in dataframe.columns if
                   dataframe[col].nunique() > 20 and str(dataframe[col].dtypes) in ["category", "object"]]
    # cat_cols
    cat_cols = cat_cols + num_but_cat
    # cat_cols
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int", "float"]]
    # num_cols
    num_cols = [col for col in num_cols if col not in cat_cols]
    print("--------------------------------------------------")
    print("EXPLANATORY DATA ANALYSIS")
    print("--------------------------------------------------")
    print("Head Observations of Dataframe")
    print("--------------------------------------------------")
    print(f"{dataframe.head()}")
    print("--------------------------------------------------")
    print("Tail Observations of Dataframe")
    print("--------------------------------------------------")
    print(f"{dataframe.tail()}")
    print("--------------------------------------------------")
    print(f"Information of Data frame: {dataframe.info()}")
    print("--------------------------------------------------")
    print(f"VARIABLES")
    print("--------------------------------------------------")
    print(f'Categoric Variables: {len(cat_cols)} {cat_cols}')
    print(f'Numerical variables: {len(num_cols)} {num_cols}')
    print(f'Categoric But Cardinal Variables: {len(cat_but_car)} {cat_but_car}')
    print(f'Numeric But Categoric Variables: {len(num_but_cat)} {num_but_cat}')
    print("--------------------------------------------------")
    print("MISSING VALUES")
    print("--------------------------------------------------")
    print(f"{dataframe.isnull().sum()}")

    return cat_cols, num_cols, cat_but_car


def cat_summary(dataframe, col_name, plot=False):
    print("--------------------------------------------------")
    print("KATEGORİK DEĞİŞKEN ANALİZİ")
    print("--------------------------------------------------")
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print("--------------------------------------------------")
    print("SAYISAL DEĞİŞKEN ANALİZİ")
    print("--------------------------------------------------")
    print(dataframe[numerical_col].describe(quantiles).T)
    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

cat_cols, num_cols, cat_but_car = grab_col_names(df)

for col in cat_cols:
    cat_summary(df, col, plot=True)

for col in num_cols:
    num_summary(df, col, plot=True)

# KATEGORİK DEĞİŞKENLERİN HEDEF DEĞİŞKENLE ANALİZİ


def target_summary_with_cat(dataframe, target, categorical_col):
    print("--------------------------------------------------")
    print("KATEGORİK DEĞİŞKENLERİN HEDEF DEĞİŞKEN ANALİZİ")
    print("--------------------------------------------------")
    print(pd.DataFrame({"Hedef Değişken Ortalaması": dataframe.groupby(categorical_col)[target].mean()}))


# NÜMERİK DEĞİŞKENLERİN HEDEF DEĞİŞKENLE ANALİZİ


def target_summary_with_num(dataframe, target, numerical_col):
    print("--------------------------------------------------")
    print("NÜMERİK DEĞİŞKENLERİN HEDEF DEĞİŞKEN ANALİZİ")
    print("--------------------------------------------------")
    print(dataframe.groupby(target).agg({numerical_col: "mean"}))


for col in cat_cols:
    target_summary_with_cat(df, "survived", col)

for col in num_cols:
    target_summary_with_num(df, "survived", col)

# KORELASYON ANALİZİ


def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list


drop_list = high_correlated_cols(df, plot=True)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1), plot=True)