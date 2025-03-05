import unittest
import HtmlTestRunner
from Tests.test01_CreateGroup import TestCreateGroup
from Tests.test02_EditGroup import TestUpdateGroup
from Tests.test03_DeleteGroup import TestDeleteGroup

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(TestCreateGroup),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestUpdateGroup),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestDeleteGroup)
    ])
    return test_suite

if __name__ == "__main__":
    run_suite = HtmlTestRunner.HTMLTestRunner(output="Reports/", report_name="test_report", report_title="Test Report")
    run_suite.run(suite())