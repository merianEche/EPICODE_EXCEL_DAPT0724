<<<<<<< HEAD
# GIORNO ZERO - ANALISI DATI ATM
# Merian Dalila Eche Rubio

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# BLOCCO A - OBIETTIVO 1: ANALISI SCIOPERI ATM
scioperi = pd.read_excel("scioperi_atm_2019_2023.xlsx")
scioperi.columns = scioperi.columns.str.strip().str.lower()
scioperi = scioperi.rename(columns={"percentuale_adesione": "adesione"})
scioperi["data"] = pd.to_datetime(scioperi["data"], errors="coerce")
scioperi.dropna(subset=["data"], inplace=True)
scioperi["anno"] = scioperi["data"].dt.year
scioperi["sindacato"] = scioperi["sindacato"].str.upper().str.strip()
scioperi_anno = scioperi.groupby("anno").agg(
    {"data": "count", "adesione": "mean"}).reset_index()
scioperi_anno.columns = ["anno", "numero_scioperi", "media_adesione"]

plt.figure(figsize=(10, 5))
sns.barplot(data=scioperi_anno, x="anno", y="numero_scioperi", palette="Blues")
plt.title("Numero di scioperi ATM per anno")
plt.tight_layout()
plt.show()

# BLOCCO B - OBIETTIVO 2: MOBILITÀ ALTERNATIVA
sharing = pd.read_csv("ds574_dati_sharing_2011-2023.csv", sep=";", encoding="ISO-8859-1")
sharing.columns = sharing.columns.str.strip().str.lower()
sharing = sharing[sharing["anno"].between(2019, 2023)]
sharing["sharing_veicoli_tipologia"] = sharing["sharing_veicoli_tipologia"].str.upper().str.strip()
sharing["sharing_veicoli_indicatori"] = sharing["sharing_veicoli_indicatori"].str.lower().str.strip()
sharing = sharing[sharing["sharing_veicoli_indicatori"].str.contains("numero di prelievi totale")]

sharing_grouped = sharing.groupby(["anno", "sharing_veicoli"])["sharing_veicoli_valore"].sum().reset_index()
sharing_grouped.columns = ["anno", "modalità", "prelievi_giornalieri"]

plt.figure(figsize=(10, 5))
sns.lineplot(data=sharing_grouped, x="anno", y="prelievi_giornalieri", hue="modalità", marker="o")
plt.title("Prelievi giornalieri sharing (2019–2023)")
plt.tight_layout()
plt.show()

base_2023 = sharing_grouped[sharing_grouped["anno"] == 2023].set_index("modalità")["prelievi_giornalieri"].to_dict()
scenari = [(mod, s, round(val * (1 + p / 100))) for mod, val in base_2023.items()
           for s, p in zip(["Leggero", "Medio", "Totale"], [15, 30, 50])]
modalita_attese = ["BIKE SHARING", "CAR SHARING", "MONOPATTINI"]

for mod in modalita_attese:
    if mod not in base_2023:
        base_2023[mod] = 0

pd.DataFrame(scenari, columns=["modalità", "scenario", "prelievi_stimati"]).to_csv("simulazione_sharing.csv", index=False)

# BLOCCO C - OBIETTIVO 3: PERCEZIONE CITTADINA (corretto)
risposte = pd.read_excel("risposte_sondaggio_atm.xlsx")

plt.figure(figsize=(7, 4))
risposte["impatto"].value_counts().sort_index().plot(kind="bar", color="orange")
plt.title("Livello di impatto percepito")
plt.xlabel("Valutazione (1 = nessun impatto, 5 = impatto critico)")
plt.ylabel("Numero di risposte")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))
risposte["comunicazione"].value_counts().plot(kind="barh", color="green")
plt.title("Valutazione comunicazione ATM")
plt.xlabel("Numero di risposte")
plt.tight_layout()
plt.show()

# BLOCCO D - OBIETTIVO 4: GIORNO ZERO (OD)
od = pd.read_csv("matrice_od_milano.csv")
od.columns = od.columns.str.strip().str.lower()
od = od.dropna(subset=["volume"])
od = od[od["volume"] > 0]
od["volume"] = od["volume"].astype(int)
od["quota"] = od["volume"] / od["volume"].sum()
od["passeggeri_stimati"] = od["quota"] * 775000
od_zona = od.groupby("zona_dest")["passeggeri_stimati"].sum().reset_index()
od_zona = od_zona.sort_values(by="passeggeri_stimati", ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(data=od_zona, x="zona_dest", y="passeggeri_stimati", palette="Reds")
plt.title("Passeggeri stimati per zona (Giorno Zero)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# BLOCCO E - OBIETTIVO 5: IMPATTO ECONOMICO SEGMENTATO
passeggeri_totali = 775000
ore_perse_medio = 1.0
profili = [
    ["Lavoratori", 0.706, 16.5],
    ["Studenti", 0.294, 6.0]
]

df_profili = pd.DataFrame(profili, columns=["Categoria", "Quota", "€/h"])
df_profili["Passeggeri"] = df_profili["Quota"] * passeggeri_totali
df_profili["Ore perse"] = ore_perse_medio
df_profili["Perdita €"] = df_profili["Passeggeri"] * df_profili["Ore perse"] * df_profili["€/h"]

print("\n Stima economica Giorno Zero segmentata per categoria:")
print(df_profili[["Categoria", "Passeggeri", "€/h", "Perdita €"]])

perdita_totale = df_profili["Perdita €"].sum()
print(f"\nTotale stimato: €{perdita_totale:,.2f}")

with open("stima_perdita_economica_segmentata.txt", "w") as f:
    f.write(f"Stima perdita economica Giorno Zero (segmentata):\n")
    for _, row in df_profili.iterrows():
        f.write(f"{row['Categoria']}: €{row['Perdita €']:,.2f}\n")
    f.write(f"\nTOTALE: €{perdita_totale:,.2f}")

=======
# GIORNO ZERO - ANALISI DATI ATM
# Merian Dalila Eche Rubio

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# BLOCCO A - OBIETTIVO 1: ANALISI SCIOPERI ATM
scioperi = pd.read_excel("scioperi_atm_2019_2023.xlsx")
scioperi.columns = scioperi.columns.str.strip().str.lower()
scioperi = scioperi.rename(columns={"percentuale_adesione": "adesione"})
scioperi["data"] = pd.to_datetime(scioperi["data"], errors="coerce")
scioperi.dropna(subset=["data"], inplace=True)
scioperi["anno"] = scioperi["data"].dt.year
scioperi["sindacato"] = scioperi["sindacato"].str.upper().str.strip()
scioperi_anno = scioperi.groupby("anno").agg(
    {"data": "count", "adesione": "mean"}).reset_index()
scioperi_anno.columns = ["anno", "numero_scioperi", "media_adesione"]

plt.figure(figsize=(10, 5))
sns.barplot(data=scioperi_anno, x="anno", y="numero_scioperi", palette="Blues")
plt.title("Numero di scioperi ATM per anno")
plt.tight_layout()
plt.show()

# BLOCCO B - OBIETTIVO 2: MOBILITÀ ALTERNATIVA
sharing = pd.read_csv("ds574_dati_sharing_2011-2023.csv", sep=";", encoding="ISO-8859-1")
sharing.columns = sharing.columns.str.strip().str.lower()
sharing = sharing[sharing["anno"].between(2019, 2023)]
sharing["sharing_veicoli_tipologia"] = sharing["sharing_veicoli_tipologia"].str.upper().str.strip()
sharing["sharing_veicoli_indicatori"] = sharing["sharing_veicoli_indicatori"].str.lower().str.strip()
sharing = sharing[sharing["sharing_veicoli_indicatori"].str.contains("numero di prelievi totale")]

sharing_grouped = sharing.groupby(["anno", "sharing_veicoli"])["sharing_veicoli_valore"].sum().reset_index()
sharing_grouped.columns = ["anno", "modalità", "prelievi_giornalieri"]

plt.figure(figsize=(10, 5))
sns.lineplot(data=sharing_grouped, x="anno", y="prelievi_giornalieri", hue="modalità", marker="o")
plt.title("Prelievi giornalieri sharing (2019–2023)")
plt.tight_layout()
plt.show()

base_2023 = sharing_grouped[sharing_grouped["anno"] == 2023].set_index("modalità")["prelievi_giornalieri"].to_dict()
scenari = [(mod, s, round(val * (1 + p / 100))) for mod, val in base_2023.items()
           for s, p in zip(["Leggero", "Medio", "Totale"], [15, 30, 50])]
modalita_attese = ["BIKE SHARING", "CAR SHARING", "MONOPATTINI"]

for mod in modalita_attese:
    if mod not in base_2023:
        base_2023[mod] = 0

pd.DataFrame(scenari, columns=["modalità", "scenario", "prelievi_stimati"]).to_csv("simulazione_sharing.csv", index=False)

# BLOCCO C - OBIETTIVO 3: PERCEZIONE CITTADINA (corretto)
risposte = pd.read_excel("risposte_sondaggio_atm.xlsx")

plt.figure(figsize=(7, 4))
risposte["impatto"].value_counts().sort_index().plot(kind="bar", color="orange")
plt.title("Livello di impatto percepito")
plt.xlabel("Valutazione (1 = nessun impatto, 5 = impatto critico)")
plt.ylabel("Numero di risposte")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))
risposte["comunicazione"].value_counts().plot(kind="barh", color="green")
plt.title("Valutazione comunicazione ATM")
plt.xlabel("Numero di risposte")
plt.tight_layout()
plt.show()

# BLOCCO D - OBIETTIVO 4: GIORNO ZERO (OD)
od = pd.read_csv("matrice_od_milano.csv")
od.columns = od.columns.str.strip().str.lower()
od = od.dropna(subset=["volume"])
od = od[od["volume"] > 0]
od["volume"] = od["volume"].astype(int)
od["quota"] = od["volume"] / od["volume"].sum()
od["passeggeri_stimati"] = od["quota"] * 775000
od_zona = od.groupby("zona_dest")["passeggeri_stimati"].sum().reset_index()
od_zona = od_zona.sort_values(by="passeggeri_stimati", ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(data=od_zona, x="zona_dest", y="passeggeri_stimati", palette="Reds")
plt.title("Passeggeri stimati per zona (Giorno Zero)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# BLOCCO E - OBIETTIVO 5: IMPATTO ECONOMICO SEGMENTATO
passeggeri_totali = 775000
ore_perse_medio = 1.0
profili = [
    ["Lavoratori", 0.706, 16.5],
    ["Studenti", 0.294, 6.0]
]

df_profili = pd.DataFrame(profili, columns=["Categoria", "Quota", "€/h"])
df_profili["Passeggeri"] = df_profili["Quota"] * passeggeri_totali
df_profili["Ore perse"] = ore_perse_medio
df_profili["Perdita €"] = df_profili["Passeggeri"] * df_profili["Ore perse"] * df_profili["€/h"]

print("\n Stima economica Giorno Zero segmentata per categoria:")
print(df_profili[["Categoria", "Passeggeri", "€/h", "Perdita €"]])

perdita_totale = df_profili["Perdita €"].sum()
print(f"\nTotale stimato: €{perdita_totale:,.2f}")

with open("stima_perdita_economica_segmentata.txt", "w") as f:
    f.write(f"Stima perdita economica Giorno Zero (segmentata):\n")
    for _, row in df_profili.iterrows():
        f.write(f"{row['Categoria']}: €{row['Perdita €']:,.2f}\n")
    f.write(f"\nTOTALE: €{perdita_totale:,.2f}")

>>>>>>> f933ef596ecb8534518fe22ed3feabb77d5efda5
df_profili.to_csv("perdita_economica_segmentata.csv", index=False)