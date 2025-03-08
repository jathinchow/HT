# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LwX3jnpSHPjvtPyicohaymgAun72jw38
"""

import pandas as pd
import numpy as np

file_path = "/content/DecayTimecourse.txt"
df = pd.read_csv(file_path, delimiter="\t", skiprows=1)

df.rename(columns={df.columns[0]: "Gene"}, inplace=True)
time_points = [0, 5, 10, 15, 20, 30, 40, 50, 60]
time_columns = [str(tp) for tp in time_points]
df_clean = df[["Gene"] + time_columns].copy()
df_clean[time_columns] = df_clean[time_columns].apply(pd.to_numeric, errors="coerce")

def compute_half_life(time_series, time_points):
    if np.isnan(time_series).all():
        return np.nan
    norm_exp = time_series / time_series[0]
    below_half = np.where(norm_exp <= 0.5)[0]
    if len(below_half) == 0:
        return np.nan
    return time_points[below_half[0]]

df_clean["HalfLife"] = df_clean[time_columns].apply(lambda row: compute_half_life(row.values, time_points), axis=1)

# Drop NaN values
df_half_life = df_clean.dropna(subset=["HalfLife"]).reset_index(drop=True)

top_10_threshold = np.percentile(df_half_life["HalfLife"], 90)
bottom_10_threshold = np.percentile(df_half_life["HalfLife"], 10)

top_10_genes = df_half_life[df_half_life["HalfLife"] >= top_10_threshold]
bottom_10_genes = df_half_life[df_half_life["HalfLife"] <= bottom_10_threshold]

top_10_genes.to_csv("top_10_genes.csv", index=False)
bottom_10_genes.to_csv("bottom_10_genes.csv", index=False)
df_half_life.to_csv("half_life_results.csv", index=False)

print("Top 10% Genes:")
print(top_10_genes.head())
print("\nBottom 10% Genes:")
print(bottom_10_genes.head())