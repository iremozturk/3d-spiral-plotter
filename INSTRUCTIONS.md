# Spiral Visualization Project - Instructions

## Overview
This project visualizes a 3D spiral dataset containing 1500 points with x, y, z coordinates.

## Setup

### Option 1: Using Virtual Environment (Recommended - Safest)

Create and activate a virtual environment to avoid modifying system Python packages:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Direct Installation (Not Recommended)

If you prefer not to use a virtual environment, you can install directly:
```bash
pip install matplotlib numpy
```

**Note**: On some systems (especially macOS with Homebrew Python), you may need to use `--break-system-packages` flag, but this is **not recommended** as it can cause system issues. Use a virtual environment instead.

## Running the Visualization

### Basic Usage

**If using virtual environment**, make sure it's activated first:
```bash
source venv/bin/activate  # On macOS/Linux
```

Then run:
```bash
python visualize_spiral.py
```

This will automatically use `spiral.csv` if available, or `spiral.json` if CSV is not found.

### Specify Data File
```bash
python visualize_spiral.py spiral.csv
# or
python visualize_spiral.py spiral.json
```

## Output

The script will:
1. Display an interactive 3D visualization window with three views:
   - **3D View**: Full 3D scatter plot colored by point number
   - **XY Plane**: Should show a ring/circular pattern
   - **XZ Plane**: Should show a sinusoidal/spiral pattern
2. Save the visualization as `spiral_visualization.png`
3. Print sanity check results verifying that point numbers increase along the Z axis
4. Display data statistics

## Expected Results

- **XY View**: Circular/ring shape (points distributed in a circle)
- **XZ View**: Sinusoidal/spiral pattern (points form a wave/spiral along Z)
- **Point Numbers**: Should generally increase as Z increases (positive correlation)

## Sanity Check

The script includes a correlation check between Z coordinates and point numbers. A positive correlation (typically > 0.3) indicates that point numbers are generally ascending along the Z axis, as expected.

