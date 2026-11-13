# build_static_data.py -> data/<bucket>.json  (one small file per 2000 TransactionIDs, loaded on demand by the page)
# Needs lookup.csv.gz, lookup_train.csv.gz, lookup_kaggle_test.csv.gz in this folder.   Run:  python build_static_data.py
import json, math, os, pandas as pd
os.makedirs("data", exist_ok=True)
SRC = [("lookup.csv.gz", 0), ("lookup_train.csv.gz", 1), ("lookup_kaggle_test.csv.gz", 2)]
df = pd.concat([pd.read_csv(f).assign(src=s) for f, s in SRC]).drop_duplicates("TransactionID")
names = sorted({n for k in range(1, 6) for n in df[f"f{k}"].unique()}); idx = {n: i for i, n in enumerate(names)}
df["b"] = df.TransactionID // 2000; n = 0
for b, g in df.groupby("b"):
    rows = {}
    for r in g.itertuples(index=False):
        d = r._asdict(); feats = []
        for k in range(1, 6):
            v = d[f"v{k}"]; feats += [idx[d[f"f{k}"]], None if (v is None or (isinstance(v, float) and math.isnan(v))) else round(float(v), 4), round(float(d[f"s{k}"]), 4)]
        a = d["Actual"]; rows[str(d["TransactionID"])] = [round(d["probability"], 5), int(d["predicted"]), round(d["amount"], 2), -1 if pd.isna(a) else int(a), d["src"], feats]
    json.dump(rows, open(f"data/{b}.json", "w"), separators=(",", ":")); n += 1
json.dump(dict(names=names, bucket=2000), open("data/meta.json", "w"), separators=(",", ":"))
print(n, "files,", len(df), "transactions")
