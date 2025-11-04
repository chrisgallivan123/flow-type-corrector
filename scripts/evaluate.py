import argparse, pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gold", required=True, help="CSV with columns: id,title,description,label")
    ap.add_argument("--pred", required=True, help="CSV with columns: id,predicted_label")
    args = ap.parse_args()

    gold = pd.read_csv(args.gold).rename(columns=str.lower)
    pred = pd.read_csv(args.pred).rename(columns=str.lower)

    df = gold.merge(pred[['id','predicted_label']], on='id', how='left')
    df['predicted_label'] = df['predicted_label'].fillna('UNKNOWN')

    y_true = df['label'].astype(str)
    y_pred = df['predicted_label'].astype(str)

    print("Labels in gold:", sorted(y_true.unique()))
    print("Labels in pred:", sorted(y_pred.unique()), "\n")
    print("Classification Report:")
    print(classification_report(y_true, y_pred, digits=4))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))

if __name__ == "__main__":
    main()
