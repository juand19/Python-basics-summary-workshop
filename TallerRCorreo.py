import re
import smtplib
def inf(i=0, step=1):
    while True:
        yield i
        i+=step

for i in inf():
    ms = "Hola"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("pythonlasso@gmail.com", "Uceva2020")
    for i in inf():
        print("Introduzca un email de Google")
        email = input("")
        emailG = re.search("@gmail.com", email)
        try:
            if emailG != None:
                print("email de gmail confirmado")
                server.sendmail("pythonlasso@gmail.com", email, ms)
                server.quit()
                print("Se envio el correo y se cerro sesion")
            else:
                raise TypeError
        except TypeError:
            print("Correo incorrecto")