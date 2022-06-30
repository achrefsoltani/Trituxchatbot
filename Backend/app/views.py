from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Chat, Message, Choice, ContactRequest, DemoRequest
import pandas as pd
import datetime
import plotly.express as px


def main_view(request):
    # Choices bar chart
    df = create_df()
    d = df['choice'].value_counts().rename_axis('choice').reset_index(name='counts')
    fig = px.bar(d, x=d['choice'], y=d['counts'])
    barchart = fig.to_html()

    # Total Interactions
    totalInt = df['chat_id'].count()
    today = datetime.date.today()
    past7 = today - datetime.timedelta(days=7)
    df["chat_start"] = pd.to_datetime(df["chat_start"]).dt.tz_localize(None)
    df["chat_date"] = df['chat_start'].dt.date
    df_filtered = df[(df['chat_date'] >= past7) & (df['chat_date'] <= today)]
    weekInt = len(df_filtered)

    # Language
    frenchIntTotal = len(df[df['language'] == 'fr'])
    englishIntTotal = len(df[df['language'] == 'en'])
    frenchIntWeek = len(df_filtered[df_filtered['language'] == 'fr'])
    englishIntWeek = len(df_filtered[df_filtered['language'] == 'en'])

    # Avg messages

    davg = df['chat_id'].value_counts().rename_axis('chat_id').reset_index(name='counts')
    avgMsg = round(davg['counts'].mean())

    # Contact Requests
    cr_df = create_cr_df()
    past30 = today - datetime.timedelta(days=30)
    avgRt = cr_df['responseTime'].mean().days
    cr_df["created_at"] = pd.to_datetime(cr_df["created_at"]).dt.tz_localize(None)
    cr_df["cr_date"] = cr_df['created_at'].dt.date
    cr_df_filtered = cr_df[(cr_df['cr_date'] >= past30) & (cr_df['cr_date'] <= today)]
    monthCr = len(cr_df_filtered)
    cr_waiting = len(cr_df_filtered[cr_df_filtered['status'] == 'unclaimed'])

    # Demo Requests
    dr_df = create_dr_df()
    dr_df["created_at"] = pd.to_datetime(dr_df["created_at"]).dt.tz_localize(None)
    dr_df["cr_date"] = dr_df['created_at'].dt.date
    dr_df_filtered = dr_df[(dr_df['cr_date'] >= past30) & (dr_df['cr_date'] <= today)]
    monthDr = len(dr_df_filtered)

    context = {
        'barchart': barchart,
        'totalInt': totalInt,
        'weekInt': weekInt,
        'frenchInt': frenchIntTotal,
        'englishInt': englishIntTotal,
        'frenchIntWeek': frenchIntWeek,
        'englishIntWeek': englishIntWeek,
        'avgMessages': avgMsg,
        'avgResponseTime': avgRt,
        'monthContactRequests': monthCr,
        'waitingCRequests': cr_waiting,
        'monthDemoRequests': monthDr,
    }

    return render(request, 'home/index.html', context=context)


def create_df():
    chat_qs = Chat.objects.all().values()
    chat_data = pd.DataFrame(chat_qs)

    message_qs = Message.objects.all().values()
    message_data = pd.DataFrame(message_qs)

    df = chat_data.merge(message_data, left_on=['id'], right_on=['chat_id'])
    df.drop(['chat_id'], inplace=True, axis=1)
    df.rename(columns={'id_x': 'chat_id',
                       'id_y': 'message_id',
                       'date_x': 'chat_start',
                       'date_y': 'message_date',
                       'choice_id': 'choice'},
              inplace=True)

    df['choice'] = df['choice'].map(lambda x: Choice.objects.get(id=x).title_en, na_action='ignore')

    return df

def create_cr_df():
    cr = ContactRequest.objects.all().values()
    df = pd.DataFrame(cr)
    return df

def create_dr_df():
    dr = DemoRequest.objects.all().values()
    df = pd.DataFrame(dr)
    return df

def change_status_view(request, id):
    cr = ContactRequest.objects.get(id=id)
    if (cr.status == 'unclaimed'):
        if (cr.agent is None):
            cr.agent = request.user
        cr.status = 'claimed'
        print('claimed')
        cr.save()
        return redirect('../../app/contactrequest/')
    elif (cr.status == 'claimed'):
        cr.status = 'closed'
        print('closed')
        cr.save()
        return redirect('../../app/contactrequest/'+str(id))

