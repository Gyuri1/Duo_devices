# Duo_devices


This python script shows how to get and delete the MFA devices on Duo. 


Please update:  
  `duo_admin_config.py` file  -> based on Your own Duo API credentials


 # How to install:

  Copy these files into a working directory and make sure `requests` is an installed python library:
  
  `pip install requests` 

  Please install `duo_client` python package as well:  
  
  `pip install duo_client`

# How to use:

You can GET the Duo registered devices using this script:

`python duo_get_devices.py >devices.txt`


You can DELETE the Duo registered device where `phone_id` is the device ID:

`python duo_delete_device.py phone_id`



