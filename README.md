# Programming for Data Science

University of London ST2195 coursework in Python and R. This project brings together a random walk Metropolis simulation and an analysis of US domestic flight delays and diversions from 2004 to April 2008.

## What I investigated

**Part 1: Monte Carlo simulation.** I implemented a Gaussian random walk Metropolis sampler for the Laplace density `f(x) = 0.5 exp(-|x|)` independently in Python and R. I compared the simulated distribution with the target and explored how proposal scale affects a four-chain variance diagnostic, using seed 2195.

**Part 2: Airline performance.** The Python notebook combines approximately 31.25 million flight records to examine departure timing, aircraft age and flight diversions. It exports summary tables that the R Markdown file uses to recreate the visualisations. Part 2 in R is a presentation of the Python results, not an independent modelling pipeline.

The supplied results suggest:

- Among hour-year groups with at least 10,000 flights, the lowest mean arrival delay occurs at 05:00 in four years and 06:00 in 2007. Saturday has the lowest mean arrival delay in every year.
- Aircraft age has a very weak flight-level correlation with total delay, approximately -0.006 to 0.013. Older aircraft have slightly higher average total delay in four years, with the direction reversed in 2006.
- Yearly logistic regression models achieve held-out AUC values of 0.6245, 0.6303, 0.6603, 0.6506 and 0.6424, respectively. These are saved coursework results, not a newly reproduced full-data evaluation.

## Selected figures

![Metropolis samples and target density](figures/part1_python_plot_a.png)

![Aircraft age and delay](figures/part2_r_2b_agegroup_bar.png)

![Yearly diversion ROC curves](figures/part2_python_2c_roc_curves.png)

## Files

The four original code files remain at the repository root with their original names and contents so their relative data paths continue to work. `data/` contains supplied summary tables and small reference datasets. `figures/` contains all supplied PNG figures. `report/` contains the submitted PDF and Word report. `scripts/` provides optional runners without modifying the originals.

## Run the project

Use Python 3.11 or later and a virtual environment. From the repository folder:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/run_python.py 1
```

Alternatively, run `jupyter notebook` from this folder and open either original notebook. Execute cells in order. Restore the raw flight files before running Part 2, then use `python scripts/run_python.py 2`. Read [data setup](data/README.md) first. Part 2 loads tens of millions of rows and holds multiple copies in memory. It can require many gigabytes of RAM and substantial runtime; no minimum hardware specification has been benchmarked.

For R, install R and the packages below, then run from the repository folder:

```r
install.packages(c("ggplot2", "dplyr", "readr", "tidyr", "knitr", "rmarkdown"))
```

```sh
Rscript scripts/run_r.R 1
Rscript scripts/run_r.R 2
```

The R runner executes extracted code chunks. For a formatted HTML document, use `rmarkdown::render("240672870_part1_r.Rmd")` or the Part 2 filename in RStudio; HTML rendering also requires Pandoc. Rendered HTML was not tested here. Part 2 R can run immediately from the supplied CSV outputs without the large flight files. Both runners save new plots at the repository root, as the original code specifies. The supplied previews in `figures/` stay separate.

## Interpretation and limitations

- These are descriptive associations. Separate hour and weekday summaries do not establish an optimal combined departure slot or explain why delays occur.
- The 2008 file covers January through April, so annual comparisons mix different seasonal coverage.
- `TotalDelay` adds arrival and departure delay. It is a coursework measure and can count overlapping delay rather than passenger time lost.
- Roughly 25% of flights lack an aircraft manufacture-year match. Age comparisons can be affected by this exclusion and by route/carrier differences.
- The age overlay fits lines to age-group means, while the reported tiny correlations are calculated across individual flights. The R overlay legend uses correlations of aggregated means; these are different statistics.
- The Part 1 diagnostic is the implemented `sqrt((B + W) / W)` coursework statistic. It is not modern split, rank-normalized R-hat. Identical starting points and a value near one alone do not demonstrate convergence.
- Diversion modelling samples non-diverted flights at roughly five per diverted flight, then filters carriers. Probabilities are not calibrated to population prevalence. Carrier eligibility uses the whole sampled dataset before the split, and the random split does not measure performance on future years.
- Coefficient magnitudes depend on feature units and carrier reference categories; the heatmap is not a reliable ranking of feature importance across years. The coefficient heatmap uses full sampled fits, whereas ROC curves use separately fitted training splits.
- Seeds are provided, but the submission has no original dependency lockfile. Exact numerical and image reproduction across versions is not guaranteed.

See [AUDIT.md](AUDIT.md) for checks performed and remaining publication decisions.

## Data source and sharing

The report attributes the data to the [ASA Data Expo 2009](https://community.amstat.org/jointscsg-section/dataexpo/dataexpo2009) and [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HG7NV7). Large raw files are omitted from this browser-upload package and listed with SHA-256 checksums in `data/manifest.json`.

This package does not establish permission to publish assessed coursework or redistribute the reference datasets and derived outputs. Keep the repository private until those permissions are confirmed. Original filenames and report content include student number 240672870. No open-source licence has been added because rights have not been established.
