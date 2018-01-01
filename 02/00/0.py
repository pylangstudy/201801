#https://qiita.com/stkdev/items/a44976fb81ae90a66381
#import imaplib, re, email, six, dateutil.parser
import imaplib, re, email
email_default_encoding = 'iso-2022-jp'

def main():
    gmail = imaplib.IMAP4_SSL("imap.gmail.com")
    username = 'user'
    password = 'pass'
    gmail.login(username, password)#imaplib.error: b'[ALERT] Please log in via your web browser: https://support.google.com/mail/accounts/answer/78754 (Failure)'
    gmail.select('INBOX') #受信ボックスを指定する
    gmail.select('register') #ラベルを指定する


if __name__ == '__main__':
    main()
