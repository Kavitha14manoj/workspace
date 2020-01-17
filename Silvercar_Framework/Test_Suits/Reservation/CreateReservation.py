'''
Created on Jan 17, 2020

'''
import unittest
from appium import webdriver



class Test_CreateReservation(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps ['platformName'] = 'iOS'
        desired_caps ['deviceName'] = 'iPhone'
        desired_caps ['bundleId'] = 'com.silvercar'
        desired_caps['automationName'] = 'XCUITest'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        
    def tearDown(self):
        self.driver.quit()
        
    def createReservation(self):
        self.driver.implicitly_wait(15)
        print("###  Create Reservation ###")
        self.driver.launch_app()
        self.driver.find_element_by_id(create_resrvation_id).click()
        
        # select airport
        self.driver.find_element_by_id(denver_airport_id).click()
        
        #select pickup and drop off date
        self.driver.find_element_by_id(pickup_date_id).click()
        self.driver.find_element_by_id(dropoff_date_id).click()
        self.driver.find_element_by_id(continue_button_id).click()
        
        # select pickup and drop off time
        self.driver.find_element_by_id(pickup_time_id).click()
        self.driver.find_element_by_id(dropoff_time_id).click()
        self.driver.find_element_by_id(continue_id).click()
        
        # select vehicle
        self.driver.find_element_by_id(vehicle_id).click()
        
        # add personal insurance coverage
        self.driver.find_element_by_id(personal_coverage_id).click()
        self.driver.find_element_by_id(enter_insurance_carrier_id_).click()
        self.driver.find_element_by_id(insurance_carrier_id).send_keys("AllState")
        self.driver.find_element_by_id(policy_number_id).send_keys("2345678")
        self.driver.find_element_by_id(ok_button_id_).click()
        self.driver.find_element_by_id(confirm_coverage_id).click()
        self.driver.find_element_by_id(reserve_silvercar_id).click()
        
        #check your coverage amount
        self.driver.find_element_by_id(ok_id_).click()
        
        # enter contact info
        self.driver.find_element_by_id(enter_email_id).send_keys("Abc")
        self.driver.find_element_by_id(enter_mobilenumber_id).send_keys("6566661626")

                
if __name__ == "__main__":
    unittest.main()
