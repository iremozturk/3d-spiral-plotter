#!/usr/bin/env python3
"""
3D Spiral Visualization Project
This script visualizes the spiral dataset from spiral.csv or spiral.json
"""

import json
import csv
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys
import os

def load_data_from_csv(filename='spiral.csv'):
    """Load data from CSV file"""
    points = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            points.append({
                'name': row['name'],
                'x': float(row['x']),
                'y': float(row['y']),
                'z': float(row['z'])
            })
    return points

def load_data_from_json(filename='spiral.json'):
    """Load data from JSON file"""
    with open(filename, 'r') as f:
        points = json.load(f)
    return points

def extract_point_number(name):
    """Extract point number from name string like 'Point #939'"""
    try:
        return int(name.split('#')[1].strip())
    except:
        return 0

def visualize_spiral(data_source='spiral.csv'):
    """Main visualization function"""
    # Load data
    if data_source.endswith('.json'):
        points = load_data_from_json(data_source)
    else:
        points = load_data_from_csv(data_source)
    
    print(f"Loaded {len(points)} points from {data_source}")
    
    # Extract coordinates
    x = [p['x'] for p in points]
    y = [p['y'] for p in points]
    z = [p['z'] for p in points]
    point_numbers = [extract_point_number(p['name']) for p in points]
    
    # Create figure with subplots
    fig = plt.figure(figsize=(18, 6))
    
    # 1. 3D Scatter Plot
    ax1 = fig.add_subplot(131, projection='3d')
    scatter = ax1.scatter(x, y, z, c=point_numbers, cmap='viridis', alpha=0.6, s=20)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('3D Spiral View (colored by point number)')
    plt.colorbar(scatter, ax=ax1, label='Point Number')
    
    # 2. XY Plane View (should show a ring)
    ax2 = fig.add_subplot(132)
    ax2.scatter(x, y, c=point_numbers, cmap='viridis', alpha=0.6, s=20)
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_title('XY Plane View (Ring Shape)')
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    
    # 3. XZ Plane View (should show sinusoidal/spiral)
    ax3 = fig.add_subplot(133)
    ax3.scatter(x, z, c=point_numbers, cmap='viridis', alpha=0.6, s=20)
    ax3.set_xlabel('X')
    ax3.set_ylabel('Z')
    ax3.set_title('XZ Plane View (Sinusoidal/Spiral Shape)')
    ax3.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('spiral_visualization.png', dpi=150, bbox_inches='tight')
    print("Visualization saved as 'spiral_visualization.png'")
    plt.close()  # Close figure to free memory
    
    # Sanity check: Verify point numbers generally increase with Z
    # Sort points by Z and check if point numbers are generally ascending
    sorted_by_z = sorted(zip(z, point_numbers), key=lambda x: x[0])
    z_sorted, numbers_sorted = zip(*sorted_by_z)
    
    # Calculate correlation between Z and point numbers
    correlation = np.corrcoef(z, point_numbers)[0, 1]
    print(f"\nSanity Check Results:")
    print(f"Correlation between Z and point numbers: {correlation:.3f}")
    print(f"Expected: Positive correlation (point numbers should increase with Z)")
    
    if correlation > 0.3:
        print("✓ PASS: Point numbers generally increase along Z axis")
    else:
        print("⚠ WARNING: Point numbers may not be increasing along Z axis as expected")
    
    # Print some statistics
    print(f"\nData Statistics:")
    print(f"X range: [{min(x):.2f}, {max(x):.2f}]")
    print(f"Y range: [{min(y):.2f}, {max(y):.2f}]")
    print(f"Z range: [{min(z):.2f}, {max(z):.2f}]")
    print(f"Point number range: [{min(point_numbers)}, {max(point_numbers)}]")

if __name__ == '__main__':
    # Check which data file exists
    data_file = 'spiral.csv'
    if len(sys.argv) > 1:
        data_file = sys.argv[1]
    elif not os.path.exists('spiral.csv') and os.path.exists('spiral.json'):
        data_file = 'spiral.json'
    
    if not os.path.exists(data_file):
        print(f"Error: Data file '{data_file}' not found!")
        print("Available files: spiral.csv, spiral.json")
        sys.exit(1)
    
    visualize_spiral(data_file)

