#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
帝意排行榜 · 复算脚本 v0 (P0-3)
输入: 指标原始分 CSV（见 tests/sample.csv）
口径: 帝意指数 = 民意分×0.60 + 专业分×0.40
      民意分 = 读者0.40 + 客服0.20 + 商店0.20 + 电商0.20
      专业分 = 道0.25 + 法0.30 + 利0.15 + 愈0.15 + 守0.15
来源: scoring-weights_20261111.csv（已公开口径，未改）
用法: python recompute.py input.csv [-o output.csv]
"""
import csv, sys, argparse, hashlib, os

# 权重直接来自已公开 scoring-weights_20261111.csv
PUBLIC_W = 0.60
PRO_W = 0.40
PUBLIC_ITEMS = {"reader_vote": 0.40, "service_sentiment": 0.20,
                "app_store": 0.20, "ecommerce_good_rate": 0.20}
PRO_ITEMS = {"dao": 0.25, "fa": 0.30, "li": 0.15, "yu": 0.15, "shou": 0.15}

REQUIRED = ["name"] + list(PUBLIC_ITEMS.keys()) + list(PRO_ITEMS.keys())

def clamp01(x):
    x = max(0.0, min(100.0, float(x)))
    return x

def compute(row):
    pub = sum(clamp01(row[k]) * w for k, w in PUBLIC_ITEMS.items())
    pro = sum(clamp01(row[k]) * w for k, w in PRO_ITEMS.items())
    score = pub * PUBLIC_W + pro * PRO_W
    return round(pub, 4), round(pro, 4), round(score, 4)

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-o", "--output")
    args = ap.parse_args()

    rows = []
    with open(args.input, encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        missing = [c for c in REQUIRED if c not in (r.fieldnames or [])]
        if missing:
            print("MISSING_COLUMNS: " + ",".join(missing), file=sys.stderr)
            sys.exit(2)
        for row in r:
            pub, pro, score = compute(row)
            rows.append({"name": row["name"], "public": pub, "professional": pro, "index": score})
    rows.sort(key=lambda x: x["index"], reverse=True)
    for i, row in enumerate(rows, 1):
        row["rank"] = i

    out = args.output or (os.path.splitext(args.input)[0] + "_result.csv")
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["rank", "name", "public", "professional", "index"])
        w.writeheader()
        w.writerows(rows)

    print("INPUT_SHA256=" + sha256(args.input))
    print("ROWS=%d OUTPUT=%s" % (len(rows), out))
    for row in rows[:10]:
        print("  %2d. %-20s index=%.4f (pub=%.2f pro=%.2f)" % (
            row["rank"], row["name"], row["index"], row["public"], row["professional"]))

if __name__ == "__main__":
    main()
