import os, sys, csv, time, json, argparse, requests, pandas as pd

def post_one(url, row):
    payload = {
        "id": str(row.get("id","")),
        "title": str(row.get("title","")),
        "description": str(row.get("description","")),
    }
    r = requests.post(url, json=payload, timeout=60)
    r.raise_for_status()
    try:
        data = r.json()
    except Exception:
        data = {"raw": r.text}
    label = data.get("label") or data.get("type") or data.get("prediction") or data.get("data",{}).get("label")
    conf = data.get("confidence") or data.get("data",{}).get("confidence")
    rationale = data.get("rationale") or data.get("data",{}).get("rationale")
    return {"id": row.get("id"), "predicted_label": label, "confidence": conf, "rationale": rationale}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="input CSV with id,title,description")
    ap.add_argument("--out", dest="out", required=True, help="output CSV")
    ap.add_argument("--webhook", default=os.getenv("WEBHOOK_URL", ""), help="n8n webhook URL")
    ap.add_argument("--sleep", type=float, default=0.2, help="sleep between requests (s)")
    args = ap.parse_args()

    if not args.webhook:
        print("ERROR: Provide --webhook or set WEBHOOK_URL env var.", file=sys.stderr)
        sys.exit(2)

    df = pd.read_csv(args.inp)
    rows = []
    for _, row in df.iterrows():
        try:
            rows.append(post_one(args.webhook, row))
        except Exception as e:
            rows.append({"id": row.get("id"), "predicted_label": None, "confidence": None, "rationale": f"ERROR: {e}"})
        time.sleep(args.sleep)

    out_df = pd.DataFrame(rows)
    out_df.to_csv(args.out, index=False)
    print(f"Wrote {args.out} with {len(out_df)} rows.")

if __name__ == "__main__":
    main()
