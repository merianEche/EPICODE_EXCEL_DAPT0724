import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("owid-covid-data.csv")
df["date"] = pd.to_datetime(df["date"])

print("Prime righe del dataset:")
print(df.head())


print("Dimensioni del dataset:", df.shape)


df.info()


df_continenti = df.groupby("continent")["total_cases"].sum()


casi_totali_mondiali = df["total_cases"].sum()
df_continenti_percentuale = (df_continenti / casi_totali_mondiali) * 100


print("\nNumero totale di casi per continente:")
print(df_continenti)
print("\nPercentuale di casi per continente rispetto al totale mondiale:")
print(df_continenti_percentuale)


df_italia = df[(df["location"] == "Italy") & (df["date"].dt.year == 2022)]


print("\nDati relativi all'Italia nel 2022:")
print(df_italia.head())


plt.figure(figsize=(10, 5))
plt.plot(
    df_italia["date"],
    df_italia["total_cases"],
    linestyle="-",
    marker="o",
    markersize=2,
    color="b",
)
plt.xticks(rotation=45)
plt.xlabel("Data")
plt.ylabel("Casi totali")
plt.title("Evoluzione dei casi di COVID-19 in Italia (2022)")
plt.grid(True)
plt.show()


df_icu = df[
    (df["location"].isin(["Italy", "Germany", "France"]))
    & (df["date"] >= "2022-05-01")
    & (df["date"] <= "2023-04-30")
]


df_icu = df_icu.dropna(subset=["icu_patients"])


plt.figure(figsize=(8, 6))
sns.set_style("whitegrid")
sns.boxplot(x="location", y="icu_patients", data=df_icu)
plt.title(
    "Confronto dei pazienti in terapia intensiva (ICU) - Maggio 2022 / Aprile 2023"
)
plt.xlabel("Paese")
plt.ylabel("Pazienti in terapia intensiva")
plt.show()


df_hosp_2023 = df[
    (df["location"].isin(["Italy", "Germany", "France", "Spain"]))
    & (df["date"].dt.year == 2023)
]


df_hosp_2023 = df_hosp_2023.dropna(subset=["hosp_patients"])


suma_hosp = df_hosp_2023.groupby("location")["hosp_patients"].sum()

print("\nTotale dei pazienti ospedalizzati nel 2023 per paese:")
print(suma_hosp)

print(
    "\nNumero di valori mancanti nella colonna 'icu_patients':",
    df["icu_patients"].isna().sum(),
)
print(
    "Numero di valori mancanti nella colonna 'hosp_patients':",
    df["hosp_patients"].isna().sum(),
)

# Analisi dei dati COVID-19: esplorazione delle ospedalizzazioni, dei casi per continente e confronto dei pazienti in terapia intensiva in diversi paesi :D Arriba peru!
