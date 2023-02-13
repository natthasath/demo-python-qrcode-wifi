import qrcode
import pywifi

# Get the Wi-Fi information
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

# Get the SSID, encryption type, and key of the Wi-Fi network
ssid = iface.status().ssid
auth = iface.status().auth
encryption = iface.status().akm[0]
key = iface.status().key

# Encode the Wi-Fi information in the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data("WIFI:T:{};S:{};P:{};".format(encryption, ssid, key))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("wifi.png")
