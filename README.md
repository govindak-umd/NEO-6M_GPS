# NEO-6M_GPS
This repository records the development and setup of the NEO-6M GPS Module.


The connections are laid out here:

| Connect From Arduino |  Connect To gps |
| ------------- | ------------- | 
| D3  | Rx  | 
| D2 | Tx | 
| GND | GND  | 
| 5V | Vin | 

The connections are made as follows:

<p align="center">
  <img height="500" src="Images/my_connection.jpeg">
</p>


The pinout is as follows:

<p align="center">
  <img height="500" src="Images/neo_6m_pinout.png">
</p>

Install the following on your Arduino IDE by going to **Tools > Manage Libraries**

- Arduino BNO055
- Adafruit Unified Sensor
- TinyGPS ++
	- To install this, click [this](https://github.com/mikalhart/TinyGPSPlus/archive/master.zip) and download
	- Unzip
	- Rename to TinyGPSPlus
	- Move it to the location with all the libraries. In my case it is *~/Arduino/libraries*
	- Re-open IDE

Install Pyserial

    pip install pyserial

Verify the USB Port by entering:

    ls /dev/tty

After verifying, make this port an executable by entering:

    sudo chmod a+rw /dev/ttyUSB0 


## ARDUINO C CODE LOOKUP TABLE


| Serial Number| Arduino Code Folder  | Function | 
| ------------- | ------------- | ------------- |
| 1  | GPS_READ_TEST | To access the GPS Data and print it in NMEA format | 
| 1  | GPS_LONGITUDE_LATITUDE_TEST | To access the GPS Data and print it in Longitudes and Latitudes | 
