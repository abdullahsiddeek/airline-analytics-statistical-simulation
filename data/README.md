# Data setup

The CSV files supplied here include Python-generated analysis summaries, ROC points, airport coordinates, carrier codes, aircraft information and variable descriptions. Their original filenames and contents are unchanged.

The following raw inputs are deliberately omitted from this browser-upload package:

| File | Bytes |
| --- | ---: |
| 2004.csv.bz2 | 110825331 |
| 2005.csv.bz2 | 112450321 |
| 2006.csv.bz2 | 115019195 |
| 2007.csv.bz2 | 121249243 |
| 2008.csv.bz2 | 39277452 |

All exceed GitHub's 25 MiB browser upload limit; the first four also exceed its 100 MiB ordinary Git file limit. Do not upload the original coursework ZIP as a repository file.

To reproduce the Python Part 2 analysis locally, copy these five files from your original coursework folder into this `data` folder. Keep them compressed and retain their exact names. Others can obtain the corresponding historical files from the [ASA Data Expo page](https://community.amstat.org/jointscsg-section/dataexpo/dataexpo2009), which links to the [Harvard dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HG7NV7). Verify the filenames and SHA-256 values against `manifest.json`; the expected 2008 input has only January through April. The download process was not tested and the Dataverse page blocked automated access during review.

The manifest describes the supplied source files, not newly regenerated data. The full Python pipeline overwrites the derived CSV files. R Part 2 only reads those CSV files and can run without raw flight data.

Source terms for redistribution were not verified. Confirm them before publishing the small reference datasets or derived outputs. The `.gitignore` excludes local raw files from Git; browser uploads do not apply `.gitignore`, so do not drag restored raw files onto GitHub.
