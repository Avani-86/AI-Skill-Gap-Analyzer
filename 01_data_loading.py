import pandas as pd
import numpy as np

print("Libraries imported successfully!")

# Load all datasets
postings_df = pd.read_csv("data/raw/postings.csv")
jobs_in_data_df = pd.read_csv("data/raw/jobs_in_data.csv")

print("\n--- Postings Dataset ---")
print("Shape:", postings_df.shape)
print("Columns:", postings_df.columns.tolist())

print("\n--- Jobs in Data Dataset ---")
print("Shape:", jobs_in_data_df.shape)
print("Columns:", jobs_in_data_df.columns.tolist())
linkedin_job_postings_df = pd.read_csv("data/raw/linkedin_job_postings.csv")
job_skills_df = pd.read_csv("data/raw/job_skills.csv")

print("\n--- LinkedIn Job Postings Dataset ---")
print("Shape:", linkedin_job_postings_df.shape)
print("Columns:", linkedin_job_postings_df.columns.tolist())

print("\n--- Job Skills Dataset ---")
print("Shape:", job_skills_df.shape)
print("Columns:", job_skills_df.columns.tolist())

print("\n--- Merging LinkedIn Postings + Job Skills ---")
merged_df = pd.merge(linkedin_job_postings_df, job_skills_df, on='job_link', how='inner')

print("Merged Shape:", merged_df.shape)
print("Merged Columns:", merged_df.columns.tolist())
print(merged_df.head())

print("\n--- Saving Merged Dataset ---")
merged_df.to_csv("data/cleaned/master_jobs_skills.csv", index=False)
print("Saved successfully to data/cleaned/master_jobs_skills.csv!")

print("\n--- Data Quality Check ---")
print("Missing values:\n", merged_df.isnull().sum())
print("\nDuplicate job_links:", merged_df['job_link'].duplicated().sum())
print("\nUnique job titles:", merged_df['job_title'].nunique())
print("Unique companies:", merged_df['company'].nunique())
print("Unique locations:", merged_df['job_location'].nunique())