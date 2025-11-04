import os, sys, json, argparse, requests

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--webhook", default=os.getenv("WEBHOOK_URL", ""), help="n8n webhook URL")
    ap.add_argument("--title", required=True)
    ap.add_argument("--description", required=True)
    ap.add_argument("--debug", default="false")
    args = ap.parse_args()

    if not args.webhook:
        print("ERROR: Provide --webhook or set WEBHOOK_URL env var.", file=sys.stderr)
        sys.exit(2)

    payload = {"title": args.title, "description": args.description, "DEBUG": args.debug}
    r = requests.post(args.webhook, json=payload, timeout=60)
    r.raise_for_status()
    print(json.dumps(r.json(), indent=2))

if __name__ == "__main__":
    main()
