import os
import zipfile
import pandas as pd
import matplotlib.pyplot as plt

percorso_zip = r"C:\Users\Meria\OneDrive\Escritorio\EPICODE\datos_sanremo.zip"
percorso_destinazione = r"C:\Users\Meria\OneDrive\Escritorio\EPICODE\datos_sanremo"
file_festival = "dati-festival-sanremo-1951-2023.xlsx"
percorso_festival = os.path.join(percorso_destinazione, file_festival)

if not os.path.exists(percorso_destinazione):
    os.makedirs(percorso_destinazione, exist_ok=True)
    with zipfile.ZipFile(percorso_zip, 'r') as zip_ref:
        zip_ref.extractall(percorso_destinazione)
    print("Archivi estratti correttamente.")

if not os.path.exists(percorso_festival):
    print("Errore: file non trovato.")
    exit()

df = pd.read_excel(percorso_festival)
print("Dati caricati correttamente")

print("Colonne nel DataFrame:")
print(df.columns)

if "Genere" not in df.columns:
    print("Errore: colonna 'Genere' non trovata.")
    exit()

percorso_csv = os.path.join(percorso_destinazione, "sanremo.csv")
df.to_csv(percorso_csv, index=False)
print(f"Archivio CSV salvato: {percorso_csv}")

conteggio = df["Genere"].value_counts()
conteggio.to_csv(os.path.join(
    percorso_destinazione, "vincitori_per_genere.csv"))

plt.figure(figsize=(6, 4))
conteggio.plot(kind="bar", color=["blue", "pink"])
plt.title("Vincitori di Sanremo per genere")
plt.xlabel("Genere")
plt.ylabel("Quantità")
plt.xticks(rotation=0)
plt.show()

vincitori_anno_genere = df.groupby("Anno")["Genere"].value_counts().unstack()
vincitori_anno_genere.to_csv(os.path.join(
    percorso_destinazione, "vincitori_anno_genere.csv"))

plt.figure(figsize=(10, 5))
vincitori_anno_genere.plot(kind="area", stacked=True, alpha=0.7)
plt.title("Vincitori di Sanremo per anno")
plt.xlabel("Anno")
plt.ylabel("Vincitori")
plt.legend(title="Genere")
plt.show()

top = df["Vincitore"].value_counts().head(10)
top.to_csv(os.path.join(percorso_destinazione, "top_10_vincitori.csv"))


plt.figure(figsize=(8, 4))
top.plot(kind="bar", color="purple")
plt.title("Top 10 artisti con più vittorie a Sanremo")
plt.xlabel("Artista")
plt.ylabel("Numero di vittorie")
plt.xticks(rotation=45)
plt.show()

df["Decada"] = (df["Anno"] // 10) * 10
conteggio_decadi = df.groupby("Decada")["Vincitore"].nunique()
conteggio_decadi.to_csv(os.path.join(
    percorso_destinazione, "vincitori_unici_per_decada.csv"))

plt.figure(figsize=(8, 4))
conteggio_decadi.plot(kind="line", marker="o", color="green")
plt.title("Numero di vincitori unici per decada")
plt.xlabel("Decada")
plt.ylabel("Numero di vincitori")
plt.grid()
plt.show()


vincitori_per_decada = df.groupby(
    ["Decada", "Vincitore"]).size().unstack().fillna(0)
vincitori_per_decada.to_csv(os.path.join(
    percorso_destinazione, "vittorie_per_decada.csv"))

recurrenti = vincitori_per_decada.columns[vincitori_per_decada.sum() > 1]
pd.Series(recurrenti).to_csv(os.path.join(
    percorso_destinazione, "artisti_recurrenti.csv"), index=False)

print("\nArtisti che hanno vinto in più di una decada:")
print(list(recurrenti))
