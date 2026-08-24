import pandas as pd
import numpy as np
import random
import os
import argparse

def generate_synthetic_data(num_rows=1000, output_path='synthetic_al_data.csv'):
    print(f"Generating {num_rows} rows of synthetic data...")
    
    streams = ['ARTS', 'COMMERCE', 'SCIENCE', 'MATHS', 'TECH']
    subjects_pool = ['POLITICAL SCIENCE', 'ECONOMICS', 'BUSINESS STUDIES', 'ACCOUNTING', 'TAMIL', 'HINDU CIVILIZATION', 'PHYSICS', 'CHEMISTRY', 'BIOLOGY']
    grades = ['A', 'B', 'C', 'S', 'F', 'Absent']
    
    data = []
    for i in range(num_rows):
        stream = random.choice(streams)
        zscore = np.round(np.random.normal(0, 1), 4)
        
        row = {
            'index': i,
            'stream': stream,
            'Zscore': zscore,
            'district_rank': f"{random.randint(1, 10000)} (NEW)",
            'island_rank': f"{random.randint(1, 100000)} (NEW)",
            'al_year': 2020,
            'sub1': random.choice(subjects_pool),
            'sub1_r': random.choice(grades),
            'sub2': random.choice(subjects_pool),
            'sub2_r': random.choice(grades),
            'sub3': random.choice(subjects_pool),
            'sub3_r': random.choice(grades),
            'cgt_r': random.choice([f"{random.randint(20, 80):03d}", 'Absent', 'S', 'F']),
            'ge_r': random.choice(['S', 'F', 'C', 'B', 'A', 'Absent']),
            'syllabus': 'new',
            'birth_day': random.randint(1, 31),
            'birth_month': random.choice(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']),
            'birth_year': random.randint(2000, 2002),
            'gender': random.choice(['male', 'female'])
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Synthetic data saved to {output_path}")
    return df

def analyze_data(csv_path):
    if not os.path.exists(csv_path):
        print(f"Error: File '{csv_path}' not found.")
        return
        
    print(f"Loading data from {csv_path}...")
    df = pd.read_csv(csv_path)
    
    print("\n--- Basic Information ---")
    print(f"Total Records: {len(df)}")
    print(f"Columns: {', '.join(df.columns)}")
    
    print("\n--- Stream Distribution ---")
    print(df['stream'].value_counts())
    
    print("\n--- Gender Distribution ---")
    print(df['gender'].value_counts())
    
    try:
        df['Zscore_numeric'] = pd.to_numeric(df['Zscore'], errors='coerce')
        avg_z = df['Zscore_numeric'].mean()
        print(f"\n--- Overall Average Z-Score: {avg_z:.4f} ---")
        
        print("\n--- Average Z-Score by Stream ---")
        print(df.groupby('stream')['Zscore_numeric'].mean())
    except Exception as e:
        print(f"Could not calculate Z-Score statistics: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, choices=['generate', 'analyze'], required=True)
    parser.add_argument('--file', type=str, default='synthetic_al_data.csv')
    parser.add_argument('--rows', type=int, default=1000)
    
    args = parser.parse_args()
    
    if args.action == 'generate':
        generate_synthetic_data(num_rows=args.rows, output_path=args.file)
    elif args.action == 'analyze':
        analyze_data(csv_path=args.file)
