import pandas as pd
df = pd.read_csv("vendas.csv")
df.head()

df.shape
# (300, 8) → linhas, colunas
df.describe()
# resumo estatístico automático

df[df["vendedor"] == "Ana Lima"]
df[df["preco_unitario"] > 1000]

df["total"] = (
 df["quantidade"] *
 df["preco_unitario"]
)
df["total"].sum()

df.groupby("vendedor")["total"].sum().sort_values(ascending=False)