from jira import JIRA

# Jira credentials and project details
JIRA_URL = 'https://vanigeetha108.atlassian.net'
USERNAME = 'vanigeetha108@gmail.com'
API_TOKEN = 'YOUR_KEY'
PROJECT_KEY = 'SCRUM'

# Define the use cases as a list of dictionaries
use_cases = [
    {
        "summary": "Predictive Maintenance: Performance Tracking",
        "description": (
            "Continuously monitor the performance of deployed models.\n\n"
            "**Steps**:\n"
            "1. Collect and log performance metrics such as accuracy, precision, recall, and F1 score.\n"
            "2. Set up dashboards for real-time performance monitoring using tools like Grafana or Kibana.\n"
            "3. Implement alerting mechanisms to notify when performance metrics fall below predefined thresholds.\n"
            "4. Periodically review and adjust performance thresholds based on new data and business requirements."
        )
    },
    {
        "summary": "Predictive Maintenance: Drift Detection",
        "description": (
            "Detect and address data drift or concept drift.\n\n"
            "**Steps**:\n"
            "1. Define metrics to measure data and concept drift.\n"
            "2. Implement drift detection algorithms such as Population Stability Index (PSI) or KL Divergence.\n"
            "3. Set up alerts to notify when significant drift is detected.\n"
            "4. Retrain models if drift exceeds predefined thresholds, ensuring they adapt to new data patterns."
        )
    },
    {
        "summary": "Predictive Maintenance: Periodic Retraining",
        "description": (
            "Regularly retrain models with new data.\n\n"
            "**Steps**:\n"
            "1. Schedule periodic data collection to gather new data.\n"
            "2. Automate the retraining pipeline using tools like Airflow or Kubeflow.\n"
            "3. Validate the performance of the retrained model on a validation set.\n"
            "4. Deploy the updated model to production if it meets performance criteria."
        )
    },
    {
        "summary": "Data Pipeline Management: Data Quality Checks",
        "description": (
            "Implement automated checks to ensure data quality and integrity.\n\n"
            "**Steps**:\n"
            "1. Define data quality rules such as handling missing values, duplicates, and outliers.\n"
            "2. Implement automated data validation scripts to check for data quality issues.\n"
            "3. Set up alerts to notify when data quality issues are detected.\n"
            "4. Log data quality metrics and review them regularly to ensure data integrity."
        )
    },
    {
        "summary": "Data Pipeline Management: ETL Process Optimization",
        "description": (
            "Optimize ETL pipelines for efficient data flow.\n\n"
            "**Steps**:\n"
            "1. Review the current ETL process to identify bottlenecks.\n"
            "2. Optimize data extraction, transformation, and loading steps.\n"
            "3. Implement parallel processing where feasible to improve performance.\n"
            "4. Monitor and log ETL performance metrics to track improvements."
        )
    },
    {
        "summary": "Feature Engineering: New Feature Creation",
        "description": (
            "Continuously explore and create new features.\n\n"
            "**Steps**:\n"
            "1. Analyze existing data to identify potential new features.\n"
            "2. Create and test new features in a development environment.\n"
            "3. Validate the impact of new features on model performance through experiments.\n"
            "4. Integrate valuable features into the production pipeline."
        )
    },
    {
        "summary": "Feature Engineering: Feature Importance Analysis",
        "description": (
            "Analyze and update feature importance regularly.\n\n"
            "**Steps**:\n"
            "1. Calculate feature importance using model-specific techniques such as SHAP values or feature importance scores.\n"
            "2. Review and interpret the importance scores to understand feature contributions.\n"
            "3. Identify and remove irrelevant or redundant features to simplify the model.\n"
            "4. Document changes to the feature set and their impact on model performance."
        )
    },
    {
        "summary": "Anomaly Detection: Operational Anomalies",
        "description": (
            "Detect and investigate anomalies in operational data.\n\n"
            "**Steps**:\n"
            "1. Define criteria for identifying operational anomalies based on historical data.\n"
            "2. Implement anomaly detection algorithms such as Isolation Forest or LOF.\n"
            "3. Set up automated alerting for detected anomalies to ensure timely response.\n"
            "4. Investigate and address the root causes of anomalies to prevent recurrence."
        )
    },
    {
        "summary": "Anomaly Detection: Model Anomalies",
        "description": (
            "Identify anomalies in model predictions.\n\n"
            "**Steps**:\n"
            "1. Define metrics for acceptable prediction ranges based on historical performance.\n"
            "2. Monitor model predictions in real-time for deviations from expected ranges.\n"
            "3. Implement alerts for prediction anomalies to notify relevant stakeholders.\n"
            "4. Review and adjust model parameters or retrain if necessary to maintain accuracy."
        )
    },
    {
        "summary": "A/B Testing: Model Experimentation",
        "description": (
            "Run A/B tests to compare model versions.\n\n"
            "**Steps**:\n"
            "1. Define the hypothesis and metrics for the A/B test to measure success.\n"
            "2. Split data or users into control and test groups to ensure valid comparisons.\n"
            "3. Deploy the models to their respective groups and collect performance data.\n"
            "4. Collect and analyze test results to determine if the new model outperforms the existing one.\n"
            "5. Make decisions based on the test outcomes and document the findings."
        )
    },
    {
        "summary": "A/B Testing: Impact Analysis",
        "description": (
            "Analyze the impact of new models on business metrics.\n\n"
            "**Steps**:\n"
            "1. Define key business metrics to monitor before and after model deployment.\n"
            "2. Implement tracking for these metrics using analytics tools.\n"
            "3. Compare metrics before and after deploying the new model to assess impact.\n"
            "4. Report on the impact and make recommendations for further action."
        )
    },
    {
        "summary": "Automation: Automate Repetitive Tasks",
        "description": (
            "Develop scripts to automate repetitive data science tasks.\n\n"
            "**Steps**:\n"
            "1. Identify tasks suitable for automation through analysis of workflows.\n"
            "2. Develop scripts or tools to automate these tasks using Python or other languages.\n"
            "3. Test the automation in a controlled environment to ensure reliability.\n"
            "4. Deploy automation to production and monitor performance regularly."
        )
    },
    {
        "summary": "Automation: CI/CD Pipelines for ML",
        "description": (
            "Implement CI/CD pipelines for model deployment and monitoring.\n\n"
            "**Steps**:\n"
            "1. Set up version control for model code using Git or other tools.\n"
            "2. Implement automated testing for model changes to ensure quality.\n"
            "3. Configure continuous integration and deployment pipelines using Jenkins, GitHub Actions, or similar tools.\n"
            "4. Monitor pipeline performance and address issues promptly to ensure smooth operation."
        )
    },
    {
        "summary": "Model Interpretability: Interpretability Tools",
        "description": (
            "Use tools to explain model predictions to stakeholders.\n\n"
            "**Steps**:\n"
            "1. Select appropriate interpretability tools such as SHAP or LIME.\n"
            "2. Generate explanations for model predictions using these tools.\n"
            "3. Present explanations to stakeholders in a clear and understandable format.\n"
            "4. Use feedback from stakeholders to improve model transparency and trust."
        )
    },
    {
        "summary": "Model Interpretability: Documentation and Reporting",
        "description": (
            "Document model decisions and performance metrics.\n\n"
            "**Steps**:\n"
            "1. Maintain detailed documentation of model development, including assumptions and design choices.\n"
            "2. Track and report performance metrics regularly to stakeholders.\n"
            "3. Share reports with relevant stakeholders to keep them informed.\n"
            "4. Update documentation regularly to reflect changes and improvements."
        )
    },
    {
        "summary": "Collaboration: Interdisciplinary Projects",
        "description": (
            "Work with other teams to integrate models into applications.\n\n"
            "**Steps**:\n"
            "1. Identify collaboration opportunities with other teams such as data engineering or product development.\n"
            "2. Define project goals and deliverables collaboratively to align expectations.\n"
            "3. Establish communication channels and regular meetings to ensure smooth collaboration.\n"
            "4. Collaborate on integrating models into applications, providing support and expertise as needed."
        )
    },
]

 


# Initialize Jira client
jira = JIRA(JIRA_URL, basic_auth=(USERNAME, API_TOKEN))

# Function to create a Jira issue
def create_issue(summary, description):
    issue_dict = {
        'project': {'key': PROJECT_KEY},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Task'}  # Change this if you use a different issue type
    }
    issue = jira.create_issue(fields=issue_dict)
    return issue

# Upload use cases to Jira
for use_case in use_cases:
    issue = create_issue(use_case['summary'], use_case['description'])
    print(f'Created issue {issue.key}: {use_case["summary"]}')

print("All use cases have been uploaded to Jira.")
