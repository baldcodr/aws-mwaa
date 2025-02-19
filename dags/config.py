
# COMMON
REGION_NAME="us-east-1"
S3_URL="s3://mwaa-dags-XXXXXXXXXXXX"

# AIRFLOW
AIRFLOW_DAG_ID="mwaa-sm-customer-churn-dag"

# GLUE
GLUE_ROLE_NAME="AmazonMWAAGlueRole"
GLUE_JOB_NAME_PREFIX="mwaa-xgboost-preprocess"
GLUE_JOB_SCRIPT_S3_BUCKET="mwaa-dags-XXXXXXXXXXXX"
GLUE_JOB_SCRIPT_S3_KEY="scripts/glue_etl.py"
DATA_S3_SOURCE="s3://mwaa-dags-XXXXXXXXXXXX/data/customer-churn.csv"
DATA_S3_DEST="s3://mwaa-dags-XXXXXXXXXXXX/mwaa-xgboost/processed/"

# SAGEMAKER
SAGEMAKER_ROLE_NAME="AmazonMWAA-SageMaker-Role"
SAGEMAKER_TRAINING_JOB_NAME_PREFIX="mwaa-sm-training-job"
SAGEMAKER_TRAINING_DATA_S3_SOURCE="s3://mwaa-dags-XXXXXXXXXXXX/mwaa-xgboost/processed/train/"
SAGEMAKER_VALIDATION_DATA_S3_SOURCE="s3://mwaa-dags-XXXXXXXXXXXX/mwaa-xgboost/processed/validation/"
SAGEMAKER_CONTENT_TYPE="text/csv"
SAGEMAKER_MODEL_NAME_PREFIX="mwaa-sm-customer-churn-model"
SAGEMAKER_ENDPOINT_NAME_PREFIX="mwaa-sm-endpoint"
SAGEMAKER_MODEL_S3_DEST="s3://mwaa-dags-XXXXXXXXXXXX/mwaa-xgboost/model/"