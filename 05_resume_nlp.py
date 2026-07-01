import os

resume_path = "data/raw/Resume"
print("Files in Resume folder:")
for root, dirs, files in os.walk(resume_path):
    print(f"\nFolder: {root}")
    for file in files[:5]:  # show first 5 files only
        print(f"  - {file}")
    if len(files) > 5:
        print(f"  ... and {len(files)-5} more files")