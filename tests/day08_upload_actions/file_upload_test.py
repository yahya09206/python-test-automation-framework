from utils.test_base import TestBase

from selenium.webdriver.common.by import By
class FileUpload(TestBase):
    def test_file_upload(self):

        self.driver.get("https://practice.cydeo.com/upload")
        file_input_field = self.driver.find_element(By.ID, "file-upload")

        file_path = "/Users/yahyahussein91/Desktop/photo-1756474215990-a18a9a0521d5.avif"
        file_input_field.send_keys(file_path)

        self.driver.find_element(By.XPATH, "//input[@id='file-submit']").click()
