import pandas as pd
import os
from .dashboard import get_master_data

def generate_week3_reports():

    df = get_master_data()
    
    # Grouping by department for payroll summary reports [cite: 50, 67]
    summary = df.groupby('department').agg({
        'gross_salary': 'sum',
        'tax_deduction': 'sum',
        'pf_deduction': 'sum',
        'net_salary': 'sum'
    })
    
    if not os.path.exists('reports'):
        os.makedirs('reports')
        
    summary.to_csv('reports/payroll_summary_week3.csv')
    print(" Week 3: Payroll Summary CSV generated.")
    return summary

def prototype_payslip_automation():
    
    df = get_master_data()
    # Mocking data for monthly payslip generation [cite: 49]
    payslip_data = df[['employee_id', 'employee_name', 'net_salary']]
    payslip_data.to_csv('reports/payslip_prototypes_week3.csv', index=False)
    print(" Week 3: Payslip prototypes generated.")