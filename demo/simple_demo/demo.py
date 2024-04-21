import serial


import numpy as np
from pyproj import CRS, Transformer
from um982.assic_driver import UM982Driver

import time



if __name__ == "__main__":
    um982_driver = UM982Driver()                # 实例化驱动对象
    ser = serial.Serial("/dev/ttyACM0", 921600) # 打开串口
    while True:
        msg = str(ser.read_all(),'utf-8')       # 读取UM982的输出
        um982_driver.decode(msg)                # 解码
        # 输出位置相关的信息
        print("####################################################")
        print("The GPS location is: ")
        print("Latitude and Longitude is: {}, {}".format(um982_driver.bestpos_lat, um982_driver.bestpos_lon)) # 维度, # 经度
        print()

        print("UTM x and y is: {}, {}".format(um982_driver.utm_x, um982_driver.utm_y))               # utm坐标的x（东方向为正）# utm坐标的y（北方向为正）             
        print("Height is:", um982_driver.bestpos_hgt)         # 海拔高度（天方向为正
        print()

        print("UTM x STD is: ", um982_driver.bestpos_latstd)      # 维度的标准差，也可以视为utm坐标下x的标准差
        print("UTM y STD is: ", um982_driver.bestpos_lonstd)      # 维度的标准差，也可以视为utm坐标下y的标准差
        print("UTM h STD is: ", um982_driver.bestpos_hgtstd)      # 海拔高度测量的标准差#
        print()

        # 输出速度相关的信息
        print("UTM x velocity is: ", um982_driver.vel_east)            # utm坐标下x方向的速度
        print("UTM y velocity is: ", um982_driver.vel_north)           # utm坐标下y方向的速度
        print("UTM h velocity is: ", um982_driver.vel_up)              # 垂直方向的速度
        print()

        print("UTM h velocity STD is: ", um982_driver.vel_up_std)          # 垂直方向速度的标准差
        print("UTM y velocity STD is: ", um982_driver.vel_north_std)       # utm坐标下y方向的速度的标准差
        print("UTM x velocity STD is: ", um982_driver.vel_east_std)        # utm坐标下x方向的速度的标准差
        print()

        # 输出姿态相关的信息
        print("heading is: ", um982_driver.heading)             # 航向角
        print("pitch is: ", um982_driver.pitch)               # pitch
        print("roll is: ", um982_driver.roll)                # roll
        print("####################################################")
        print()
        

        time.sleep(0.05)
        



