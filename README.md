# Assignment 2 - Gene Expression Analysis

## Overview
This assignment analyzes yeast transcript expression levels over time, focusing on identifying transcripts with the highest and lowest half-lives. Additionally, functional enrichment analysis is performed using GO annotations.

## Data
- The dataset consists of time-course data showing relative expression levels of yeast transcripts at different time points (0 to 60 minutes in 5-minute intervals) in tab-delimited text format.
- Expression values are normalized to 1 at time 0.
- Some transcripts lack data across all time points due to missing probes and are ignored in the analysis.

## Objective
1. Identify genes/transcripts with very high (top 10%) and very low (bottom 10%) half-lives.
2. Perform functional enrichment analysis using GO annotations.
3. Report results and insights.

## Methodology
### Step 1: Data Preprocessing
- Load the dataset.
- Remove transcripts with missing expression values across all time points.
- Normalize expression levels where necessary.

### Step 2: Computing Half-Lives
- Fit an exponential decay model to estimate transcript half-lives.
- Rank transcripts based on half-life values.
- Identify the top 10% (longest-lived) and bottom 10% (shortest-lived) transcripts.

### Step 3: Functional Enrichment Analysis
- Perform GO term enrichment using:
  - [g:Profiler](http://biit.cs.ut.ee/gprofiler/)
  - [GO Term Finder](http://go.princeton.edu/cgi-bin/GOTermFinder)
- Compare functional categories enriched in long-lived and short-lived transcripts.

## Results
- **Top 10% Long-Lived Transcripts**: These genes are mostly associated with structural and housekeeping functions, indicating stability.
- **Bottom 10% Short-Lived Transcripts**: These genes are predominantly involved in regulatory functions, suggesting rapid turnover is necessary.
- **Enrichment Analysis**:
  - Long-lived transcripts show enrichment in metabolic processes and structural components.
  - Short-lived transcripts are enriched in stress response and regulatory processes.

## Code
- The Python script used for this analysis is included in this submission.
- Ensure dependencies (pandas, numpy) are installed before running the script.

## Submission Details
- Programming Language: **Python**
- Results and analysis are included in this README.
- Delays beyond 4 days from the deadline will result in zero points.

## Conclusion
This analysis identifies key functional differences between long- and short-lived transcripts, providing insight into the regulation of yeast gene expression.

---
**Prepared by:** JATHIN YARRA 
**Date:** 03/07/2025
