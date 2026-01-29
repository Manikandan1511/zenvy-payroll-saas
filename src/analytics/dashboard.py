import pandas as pd
import os

def get_master_data():
    emp = pd.read_csv('data/zenvy_employees.csv')
    att = pd.read_csv('data/zenvy_attendance.csv')
    pay = pd.read_csv('data/zenvy_payroll.csv')
    
    master = pd.merge(emp, pay, on='employee_id')
    master = pd.merge(master, att, on='employee_id')
    return master

def calculate_metrics():
    """Generates key metrics for the Dashboard."""
    df = get_master_data()
    dept_spending = df.groupby('department')['gross_salary'].sum()
    total_ot = df['overtime_hours'].sum()
    return dept_spending, total_ot

def export_for_powerbi():
    """Create a Master CSV for Power BI Visualization."""
    master = get_master_data()
    
    master['tax_percentage'] = (master['tax_deduction'] / master['gross_salary']) * 100
    
    if not os.path.exists('reports'):
        os.makedirs('reports')
        
    output_path = 'reports/zenvy_master_powerbi.csv'
    master.to_csv(output_path, index=False)
    print(f" Success! Master file exported to: {output_path}")
    return output_path