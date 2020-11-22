'''
Creates out of the SSID of the network, the encryption technology and the password a QR-Code that automatically logs you into the wifi.
'''
import pyqrcode as pqr

def create_qr_code(ssid, security, password):
    qr = pqr.create('WIFI:S:{ssid};T:{security};P:{password};;'.format(
        ssid=ssid,
        security=security,
        password=password
    ))
    print(qr.terminal())

if __name__ == "__main__":
    create_qr_code('testSSID', 'WPA2', 'testexample_!')