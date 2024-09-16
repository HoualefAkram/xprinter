from escpos import printer

p = printer.Network("192.168.123.100")

p.set(
    align="center",
    font="a",
    bold=True,
    underline=None,
    width=None,
    height=None,
    density=None,
    invert=None,
    smooth=None,
    flip=None,
    normal_textsize=None,
    double_width=None,
    double_height=None,
    custom_size=None,
)
p.text("Ministry of transport\n\n")
p.text("Payment System\n\n")
p.image("logo2.jpg")
p.qr("Scan qr code", size=10)
p.text("15/9/2024")
p.cut()
