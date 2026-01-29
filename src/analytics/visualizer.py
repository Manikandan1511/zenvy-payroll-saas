import matplotlib.pyplot as plt
import seaborn as sns
from .dashboard import get_master_data

def build_mock_dashboards():
    df = get_master_data()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    #  Salary Distribution Chart 
    sns.histplot(df['net_salary'], kde=True, ax=axes[0], color='blue')
    axes[0].set_title('Salary Distribution Chart ')

    #  Department-wise Payroll Expenses [
    dept_expenses = df.groupby('department')['gross_salary'].sum().reset_index()
    sns.barplot(data=dept_expenses, x='department', y='gross_salary', ax=axes[1], hue='department', legend=False)
    axes[1].set_title('Dept-wise Payroll Expenses')

    plt.tight_layout()
    plt.savefig('reports/week3_mock_dashboards.png')
    print(" Week 3: Mock Dashboards saved to reports.")