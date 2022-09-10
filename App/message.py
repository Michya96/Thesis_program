import pywhatkit


def sendMail(title, message, recipient):
    pywhatkit.send_mail("michja144@gmail.com", "gpexmvoazpokfcuk", title,
                        message, recipient)
