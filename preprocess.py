from ast import pattern
from email import message

from matplotlib.style import use
import streamlit as st
import preprocess
import re
import stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def gettimeanddate(string):
    string = string.split(',')
    date, time = string[0], string[1]
    time = time.split('-')
    time = time[0].strip()
    return date + " " + time

def getstring(text):
    return text.split('\n')[0]

def preprocess(data):
    # 18/08/2020, 12: 52 pm - Kauleshwar: This is attendance taken by Google meet
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_meassages': messages, 'message_date': dates})

    df['message_date'] = df['message-date'].apply(
        lambda text: gettimeanddate(text))
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []

    for meassage in df['user_meassages']:
        entry = re.split('[\W\W]+?:\s', meassage)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('Group Notification')
            messages.append(entry[0])
    
    df['Users']= users
    df['message']= messages

    df['message']= df['message'].apply(lambda text:
    getstring(text))

    df.drop(['user_messages'], axis=1)
    df= df[['message', 'date', 'User']]

    df= df.rename(columns={'message': 'Message', 'date': 'Date'})

    df['Only date'] = pd.to_datetime(df['Date']).dt.date

    df['Year'] = pd.to_datetime(df['Date']).dt.year

    df['Month_num'] = pd.to_datetime(df['Date']).dt.month

    df['Month'] = pd.to_datetime(df['Date']).dt.month_name()

    df['Day'] = pd.to_datetime(df['Date']).dt.day

    df['Day_name'] = pd.to_datetime(df['Date']).dt.day_name()

    df['Hour'] = pd.to_datetime(df['Date']).dt.hour

    df['Minute'] = pd.to_datetime(df['Date']).dt.minute

    return df
