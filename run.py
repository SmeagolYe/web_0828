import pytest


# pytest.main(["-m", "test_login", "--html=html_report/report.html"])
pytest.main(["-m", "test_index", "--html=html_report/report.html"])
# pytest.main(["--html=html_report/report.html"])