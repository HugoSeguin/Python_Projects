#Delete emails
import smtplib

imapObj.select_folder('', readonly=false)
UIDs = imapObj.search(['ON 09-JUL-2015'])
imapObj.delete_message(UIDs)
imapOjbj.expunge()
imapObj.logout()