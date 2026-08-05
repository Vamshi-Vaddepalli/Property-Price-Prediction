# Gurgaon Real Estate Analytics Suite

A Streamlit app for Gurgaon property price prediction, market analytics, and
apartment recommendations.

## Structure

```
├── Home.py                          # Landing page (entrypoint)
├── pages/
│   ├── 1_Price_Predictor.py         # Price prediction form
│   ├── 2_Analysis_App.py            # Market analytics dashboards
│   └── 3_Recommend_Appartments.py   # Location search + recommender
├── datasets/                        # All model artifacts & data the app reads
│   ├── df.pkl
│   ├── pipeline.pkl                 # ~146 MB — tracked via Git LFS
│   ├── cosine_sim1.pkl / 2 / 3.pkl
│   ├── location_distance.pkl
│   ├── secwise.pkl
│   ├── feature_text.pkl
│   └── data_viz1.csv
├── requirements.txt
├── .gitattributes                   # Git LFS tracking rule for datasets/*.pkl
└── .gitignore
```

## Deploying to Streamlit Community Cloud

### 1. Install Git LFS (one-time, on your machine)

`pipeline.pkl` is ~146 MB, over GitHub's 100 MB hard limit for regular files,
so it must go through Git LFS. Streamlit Community Cloud supports LFS-tracked
repos natively — no extra config needed on their end.

```bash
# macOS
brew install git-lfs
# Windows: winget install GitHub.GitLFS   (or download from git-lfs.github.com)
# Linux (Debian/Ubuntu)
sudo apt-get install git-lfs

git lfs install
```

### 2. Add these files to your existing repo

Copy the contents of this folder into your repo (or clone your repo and drop
these files in), then:

```bash
cd your-repo
git lfs track "datasets/*.pkl"     # already captured in .gitattributes below
git add .gitattributes
git add .
git commit -m "Add Streamlit app with LFS-tracked model artifacts"
git push origin main
```

Since `.gitattributes` is already included in this folder, `git lfs track`
will pick it up automatically — just make sure `git lfs install` has been run
once on your machine before your first commit of the `.pkl` files.

### 3. Deploy on Streamlit Community Cloud

1. Go to https://share.streamlit.io and sign in with GitHub.
2. Click **New app**.
3. Pick your repo, branch (`main`), and set **Main file path** to `Home.py`.
4. Click **Deploy**.

First deploy will take a few minutes since it has to pull the LFS files and
install scikit-learn/pandas/plotly/wordcloud. Subsequent deploys are faster.

### Notes / gotchas already fixed in this version

- `1_Price_Predictor.py` originally loaded `df.pkl` / `pipeline.pkl` from the
  repo root while the other two pages loaded from `datasets/`. Standardized
  to `datasets/` everywhere.
- Removed a leftover module-level test call
  (`recommend_properties_with_scores('DLF The Camellias')`) in the
  recommender page — it ran on every page load for no UI benefit.
- Removed `plt.rcParams['font.family'] = 'Arial'` in the word cloud — Arial
  usually isn't installed on Linux cloud servers and this can throw a font
  warning or silently fall back; matplotlib's default font works fine here.
- Pinned `requirements.txt` to the exact scikit-learn/pandas/numpy versions
  the pickles were verified to load cleanly with, to avoid unpickling
  incompatibilities on the cloud.

### Free-tier limits worth knowing

- GitHub free tier: 1 GB Git LFS storage + 1 GB LFS bandwidth/month. A single
  146 MB model file is fine for storage; if you redeploy very frequently
  you could approach the bandwidth cap. If that ever becomes an issue, the
  fix is retraining `RandomForestRegressor` with fewer trees
  (`n_estimators=500` → e.g. 150–200) or capping `max_depth`, which shrinks
  the pickle substantially with minimal accuracy loss.
- Streamlit Community Cloud apps sleep after a period of inactivity on the
  free tier and cold-start on the next visit — expect a ~30–60s wake-up delay.
