import pandas as pd
import glob
import os
import math

# -------------------------
# 1. Paths
# -------------------------
input_folder = "reddit"   # folder with 4 Reddit CSVs
output_file = os.path.join(input_folder, "reddit_combined_22k.csv")

# -------------------------
# 2. Load all CSVs
# -------------------------
csv_files = sorted(glob.glob(os.path.join(input_folder, "*.csv")))

if not csv_files:
    print("⚠️ No CSV files found in 'reddit/' folder.")
else:
    print(f"📂 Found {len(csv_files)} Reddit CSV files.")

    dfs = []
    target_total = 22245
    per_file_target = target_total // len(csv_files)  # 5561 rows each

    for file in csv_files:
        try:
            df = pd.read_csv(file, lineterminator="\n")

            n = len(df)
            step = math.floor(n / per_file_target) if n > per_file_target else 1

            # ✅ Systematic sampling: take every `step` row
            sampled_df = df.iloc[::step].head(per_file_target)

            dfs.append(sampled_df)
            print(f"✅ {file}: {n} rows → sampled {len(sampled_df)} rows (step={step})")

        except Exception as e:
            print(f"❌ Error processing {file}: {e}")

    # -------------------------
    # 3. Combine & Save
    # -------------------------
    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        combined_df.to_csv(output_file, index=False)

        print(f"\n🎯 Systematic combined dataset saved: {output_file}")
        print(f"📊 Final row count: {len(combined_df)} (target {target_total})")
