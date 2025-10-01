# Copilot Instructions for Session-1 Codebase

## Overview
This workspace contains Python scripts and Jupyter notebooks for learning and solving problems, including project Euler challenges and a house price prediction notebook. There are two main folders:
- `Session 0/`: Contains individual Python scripts for Project Euler problems and intermediate Python exercises.
- `Session 1/`: Contains a Jupyter notebook (`house_price_predict.ipynb`) and a dataset (`Housing.csv`) for regression analysis.

## Key Patterns & Conventions
- **Project Euler Scripts**: Each script (e.g., `project_euler1.py`) solves a specific problem. Scripts are standalone and do not import from each other.
- **Notebook Data Loading**: Notebooks load data using `pd.read_csv('Housing.csv')`. Always reference the dataset with the correct relative path.
- **Feature Selection**: In the notebook, features are selected from the DataFrame using column names. Use `input_data[['col1', 'col2', ...]]` for multiple columns, not `input_data['col1','col2',...]`.
- **No Custom Modules**: All code is in scripts or notebooks; there are no shared Python modules or packages.
- **Python Version**: Use Python 3.11+ for compatibility.

## Developer Workflows
- **Run Scripts**: Execute scripts in `Session 0/` directly with `python project_eulerX.py`.
- **Jupyter Notebook**: Open `house_price_predict.ipynb` in VS Code or Jupyter Lab. Run cells sequentially for data analysis.
- **Data File**: Ensure `Housing.csv` is present in `Session 1/` for notebook execution.

## External Dependencies
- **Required Libraries**: `numpy`, `pandas` (imported in notebooks/scripts). Install with `pip install numpy pandas` if missing.
- **No Build System**: No Makefile, requirements.txt, or automated build/test scripts.

## Example Patterns
- **Correct DataFrame Slicing**:
  ```python
  # For multiple columns:
  X = input_data[['area', 'bedrooms', 'bathrooms', ...]]
  y = input_data['price']
  ```
- **Importing Libraries**:
  ```python
  import numpy as np
  import pandas as pd
  ```

## Recommendations for AI Agents
- Focus on cell-by-cell execution in notebooks; validate code before running.
- When editing or generating code, follow the existing style: simple, direct, and script-based.
- If adding new scripts, place them in the appropriate session folder and name them descriptively.
- Do not introduce complex project structures or external dependencies unless explicitly requested.

## Reference Files
- `Session 0/project_euler*.py`: Example problem-solving scripts.
- `Session 1/house_price_predict.ipynb`: Main notebook for regression analysis.
- `Session 1/Housing.csv`: Dataset for notebook analysis.

---
If any section is unclear or missing, please provide feedback for further refinement.