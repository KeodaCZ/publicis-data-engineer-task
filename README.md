# Campaign Investment Analysis

This repository contains a solution for a data engineering task focused on analyzing
planned vs actual marketing campaign investment.

The project uses Python to load campaign data from Azure Blob Storage, clean and aggregate
the data, and compare planned and actual investment on a daily and cumulative basis.

## Project Structure

- `notebooks/`
  - `campaign_analysis.ipynb` – Jupyter notebook used for data exploration, transformation
    and visualization
- `src/`
  - `extract.py` – data extraction logic (loading CSV files from Azure Blob Storage)
  - `config.py` – configuration and environment variable handling
- `.env` – environment variables (not included in the repository)

## Output

The main output of the project is an exported HTML version of the Jupyter notebook,
which contains:
- data exploration and cleaning steps
- daily and cumulative investment comparison
- visualizations and brief explanations of results

## Notes

The notebook is intentionally kept focused on analysis and validation, while data extraction
logic is separated into standalone Python modules.
Sensitive configuration (e.g. access tokens) is handled via environment variables and is not
stored in the repository.