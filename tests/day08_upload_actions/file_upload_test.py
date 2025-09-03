from utils.test_base import TestBase


class FileUpload(TestBase):
    def test_file_upload(self):
        self.driver.get("https://practice.cydeo.com/upload")
