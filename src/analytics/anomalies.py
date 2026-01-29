import pandas as pd
from .dashboard import get_master_data

def run_anomaly_detection_v1():

    df = get_master_data()
    
    df['salary_diff_pct'] = (df['gross_salary'] - df['base_salary']) / df['base_salary']
    

    anomalies = df[df['salary_diff_pct'] > 0.20]
    
    anomalies.to_csv('reports/anomaly_detection_week3.csv', index=False)
    
    return anomalies