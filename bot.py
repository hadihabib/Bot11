from cgitb import text
from fileinput import close
import imp
from tkinter import Text
from unittest.mock import call
from numpy import ones_like
from telegram.ext import *
from telegram import *
import requests,json
import telegram
import pandas as pd

import csv
from openpyxl import Workbook



TOKEN = "5137905230:AAFnc7m78VR6Ria5IdAnho2BW1xPZ0vwBRw"

enter="مشروع يهدف إلى إحداث نقلة نوعية في مفهوم التعليم العالي والبحث العلمي من خلال الانتقال من التلقين النظري إلى التطبيق العملي وتحقيق الربط الفعال بين الجامعة والمجتمع عملياً وفق أسس علمية بما يسهم في تعزيز الاقتصاد الوطني والمساهمة في عملية البناء."


def start(update, context):     
    update.message.reply_text(enter)


if __name__ == '__main__':
   
    updater = Updater(TOKEN,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    updater.start_polling()
    print("Bot Started")
    updater.idle()
