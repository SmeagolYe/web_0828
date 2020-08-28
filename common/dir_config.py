import os


current_file_dir = os.path.abspath(__file__)
common_dir = os.path.split(current_file_dir)[0]
base_dir = os.path.split(common_dir)[0]

test_case_dir = os.path.join(base_dir, "test_case")
test_data_dir = os.path.join(base_dir, "test_data")
logs_dir = os.path.join(base_dir, "logs")
html_report_dir = os.path.join(base_dir, "html_report")
screenshot_dir = os.path.join(base_dir, "screenshot")
