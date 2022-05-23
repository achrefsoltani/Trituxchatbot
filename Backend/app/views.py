from django.shortcuts import render
from .models import Chat,Message,Choice
import pandas as pd

import plotly.express as px



def main_view(request):
    #bar chart
    df = create_df()
    d = df['choice'].value_counts().rename_axis('choice').reset_index(name='counts')
    fig = px.bar(d, x=d['choice'], y=d['counts'])
    chart = fig.to_html()



    context = {
        'chart': chart
    }

    return render(request, 'home/index.html' , context=context)



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

    df['choice'] = df['choice'].map(lambda x : Choice.objects.get(id=x).title_en)


    return df

def chart(request):
    df = create_df()

    d = df['choice'].value_counts().rename_axis('choice').reset_index(name='counts')



    fig = px.bar(d, x=d['choice'], y=d['counts'])

    chart = fig.to_html()

    context ={'chart': chart}

    return render(request, 'bar_chart.html', context=context)






