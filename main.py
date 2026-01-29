from src.analytics.reports import generate_week3_reports, prototype_payslip_automation
from src.analytics.anomalies import run_anomaly_detection_v1
from src.analytics.visualizer import build_mock_dashboards

print(" Zenvy Payroll SaaS - Week 3: Initial Module Development ")


generate_week3_reports()
prototype_payslip_automation()


anomalies = run_anomaly_detection_v1()
print(f"--- AI Alerts: {len(anomalies)} salaries flagged  ---")


build_mock_dashboards()