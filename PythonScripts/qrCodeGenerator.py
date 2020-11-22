'''
Creates out of the SSID of the network, the encryption technology and the password a QR-Code that automatically logs you into the wifi.
'''
import sys
import pyqrcode as pqr

def create_qr_code(ssid, security, password):
    qr = pqr.create('WIFI:S:{ssid};T:{security};P:{password};;'.format(
        ssid=ssid,
        security=security,
        password=password
    ))
    print(qr.terminal())

if __name__ == "__main__":
    ssid = sys.argv[1]
    security = sys.argv[2]
    password = sys.argv[3]
    create_qr_code(ssid, security, password)