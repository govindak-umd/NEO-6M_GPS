"""Code to read GPS Data through pyserial

Attributes:
    ser (TYPE): Serial
"""
import serial

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 9600

while ser.isOpen():

    # Convert from ascii encoding

    imu_data = ser.readline().decode("ascii")

    data_code = imu_data[0:3]

    # Getting the Lattitude data and split it at the right
    # parsing points

    if data_code == 'Lat':

        lat_data = ((imu_data.split(': ')[1]).split('\r\n'))[0]
        print(lat_data)

    # Getting the Longitude data and split it at the right
    # parsing points
    
    if data_code == 'Lon':

        lon_data = ((imu_data.split(': ')[1]).split('\r\n'))[0]
        print(lon_data)

    # Getting the Altitude data and split it at the right
    # parsing points
    
    if data_code == 'Alt':

        alt_data = ((imu_data.split(': ')[1]).split('\r\n'))[0]
        print(alt_data)
    
    # Getting the TimeStamp data and split it at the right
    # parsing points
    
    if data_code == 'Tim':

        tim_data = ((imu_data.split(': ')[1]).split('\r\n'))[0]
        print(tim_data)

    print('--------')
