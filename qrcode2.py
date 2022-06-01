import qrcode

qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
	)
data = "https://www.youtube.com/watch?v=5ud8Bfbo9vk"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color='white')
img.save("youtube.png")