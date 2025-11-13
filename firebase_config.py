import firebase_admin
from firebase_admin import credentials, db

# Hardcoded credentials for quick testing only (DO NOT DEPLOY PUBLICLY)
service_account_info = {
    "type": "service_account",
    "project_id": "sathack-7d9d8",
    "private_key_id": "ffffbab5d69095934a235383f28a3894f8cd9f63",
    "private_key": """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDGhpCt8jQ0zM9B
eH0Hcoutvzi/EorRohtrTzUsR1BN1p1l8LZ/J5rD5ZbctxAWrOf3agh4A/F20sKi
MhHQ2/UnZa+W7bFJ5oD2++Prt5+taQ+thLmPKeOmH9FCyefM1tt8mOlKNnleHlaV
Lv1eW2XZpUiiwlBxaj5gljUWEUCwD/B2u8ZmP2UCBjt6Z4qcNTrSLyd0TlZwUZaK
G1IAoSEvEDcdow+9ZugezVMng0mlemJgwPhQRiB9B4FseCyBB9OwPZyJKJpKkKyh
nNgPqJ7xdr12ZYk3oD5ueOCsLj4DLFwXNYroPK8D1L0JOedxknYs4BZeXz3qK3/v
hd294xi1AgMBAAECggEACafW1pb+ogjKFcmZ7yhLkd5IkMaCmPKU+dGm6OnpBngn
PKOKBMI03U1H2qFOt4OeXqK6Gbg7YMecbs4Xnrxr/ogME7+ozUrYP+r9aWQLcKA5
Anv/mG51o4lNoL14ODbFAxje09y1Z3X7SRM5gILaf8zxrPTde76qnQEBQPsC1e1C
mcoN59uEVCOURFyi94NHrA12qIyvBt7Zzmjz+eayU7B1UYVl6kvaJ6Ijp0FO6EqN
SFy+UvdcldO8TrwfmbehuOtPbasxj8R7VI/W/pR3K8GwQJRc6OJl+tEblrOoalV9
Q36VHC99avx/vR4Tk6uJ5Qk/mX17zc7gbSvvu0YaqwKBgQDmz6G5FiijlCLOsjnj
NFKWDzpgcRG5fRvl590PJIXvD/GykZN/YlIH4NAkMyleN39EOAYpmbHoYcQ1PGoR
OSWR0LSQ6rNqg1MmnAKyrhlAHY8lKd1iOSt8ECmO1jopYmm6OGC+iuzh9UISLtiu
qmbldr72bpJEVvcOBFMGHuskkwKBgQDcMPKkeGmf2HjbLYrAVMp+lfg2xKUYWQRn
PwjxJvwi3wGGHWlHiSj/mxbSFIUdiZJsRWZNbnE9B9dio0VLmi/OGMvg7xU7v4bX
k7QffAbRIvHVjopcn6lBU73WxTAvnTGof2QHiMDf2izFd7qs+OAGZ7tQ8vdlp2Om
j33IYncilwKBgBaiiA6ZoLSiA2PX0Jt6dxrmNWhdzkotfb3nJiOlBklye9ZyNk/I
uZiyMFdMeSMXODDdeaU8wFi0tcQuv4we2ZNaL0sC6UNpy46+v/j739gMzgvr9hz6
1EvfXeP3GE8Uqp+rhblJ8H8cSTV1SKSga2TXZ1TNdSSkjqfePrIb+B1nAoGBAIYT
gAxKDfb5N04uwwguGUdPRl8DCoxy182OgoFk/a62IBVsH0kh6ccKxrCRMiU0OeaX
s51+nJFPDwXO6UkJ0AYs7yg+LK2/B/qIw+tP+E6seplRPEr+JW/T8Aqw85BqpWw2
ddBooxkrnot3RkJBIRiFXXgDGkXZ0UIAqdS0sFptAoGBAIDD9J/eu5rXnqRza8GD
OLFk71zvwcePSGQrPnP0+DKjMkznHJ0Jm2CaUpGRRrBSMrhkWePToZQN063jvzID
iWm2EC078xCgHvLwfM4AZ//Oaongy1WDlod/XBW5lOivzNIqU7UyyVbgCLjRBGvP
TCD1BgCNZOuf+L+JQhrClmnA
-----END PRIVATE KEY-----""",
    "client_email": "firebase-adminsdk-fbsvc@sathack-7d9d8.iam.gserviceaccount.com",
    "client_id": "118406304797252000966",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40sathack-7d9d8.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

cred = credentials.Certificate(service_account_info)

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sathack-7d9d8-default-rtdb.firebaseio.com/'
})

database = db
