# 3D Spiral Visualization

A Python project for visualizing a 3D spiral dataset containing 1500 points with x, y, z coordinates. The visualization generates three views: a full 3D scatter plot, an XY plane view showing a ring pattern, and an XZ plane view showing a sinusoidal/spiral pattern.

## Project Description

This project was created for CSC864 (Spring 2022) to visualize a spiral dataset. The data consists of 1500 points that form a loose spiral along the z-axis. Point numbers (from the "name" field) generally ascend along the Z axis, and the visualization confirms this pattern.

## Features

- 3D scatter plot visualization with color-coding by point number
- XY plane view showing a ring/circular pattern
- XZ plane view showing a sinusoidal/spiral pattern
- Automatic sanity check verifying point numbers increase with Z axis
- Support for both CSV and JSON data formats
- Data statistics and correlation analysis

## Requirements

- Python 3.6 or higher
- matplotlib >= 3.5.0
- numpy >= 1.21.0

## Installation

### Using Virtual Environment (Recommended)

Create and activate a virtual environment to avoid modifying system Python packages:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Direct Installation

If you prefer not to use a virtual environment:

```bash
pip install matplotlib numpy
```

Note: On some systems (especially macOS with Homebrew Python), you may need to use `--break-system-packages` flag, but this is not recommended as it can cause system issues. Use a virtual environment instead.

## Usage

### Basic Usage

If using a virtual environment, make sure it's activated first:

```bash
source venv/bin/activate  # On macOS/Linux
```

Then run the visualization script:

```bash
python visualize_spiral.py
```

The script will automatically use `spiral.csv` if available, or `spiral.json` if CSV is not found.

### Specify Data File

You can also specify which data file to use:

```bash
python visualize_spiral.py spiral.csv
# or
python visualize_spiral.py spiral.json
```

## Output

The script generates:

1. **Visualization Image**: `spiral_visualization.png` containing three views:
   - 3D View: Full 3D scatter plot colored by point number
   - XY Plane: Ring/circular pattern
   - XZ Plane: Sinusoidal/spiral pattern

2. **Console Output**:
   - Number of points loaded
   - Sanity check results (correlation between Z and point numbers)
   - Data statistics (ranges for X, Y, Z coordinates and point numbers)

## Expected Results

- **XY View**: Circular/ring shape (points distributed in a circle)
- **XZ View**: Sinusoidal/spiral pattern (points form a wave/spiral along Z)
- **Point Numbers**: Should generally increase as Z increases (positive correlation)

## Sanity Check

The script includes a correlation check between Z coordinates and point numbers. A positive correlation (typically > 0.3) indicates that point numbers are generally ascending along the Z axis, as expected. The test data should show a correlation close to 1.0.

## Data Format

The data files contain points with the following structure:

- **name**: Point identifier (e.g., "Point #1", "Point #2")
- **x**: X coordinate (typically ranges from -1.3 to 1.3)
- **y**: Y coordinate (typically ranges from -1.3 to 1.3)
- **z**: Z coordinate (typically ranges from 1.0 to 19.0)

Data is available in both CSV and JSON formats:
- `spiral.csv`: Comma-separated values format
- `spiral.json`: JSON array format

## Files

- `visualize_spiral.py`: Main visualization script
- `requirements.txt`: Python dependencies
- `spiral.csv`: Data in CSV format
- `spiral.json`: Data in JSON format
- `spiral.m`: Original MATLAB data generation script
- `README.txt`: Original project instructions

## Project Information

This project was created for CSC864 (Spring 2022). The original data generation script (`spiral.m`) was provided in MATLAB format and generates 1500 points with added noise to create a loose spiral pattern.

## License

This project is for educational purposes.

