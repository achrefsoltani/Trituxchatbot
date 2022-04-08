from django.shortcuts import render
from .models import Chat,Message,Choice
import pandas as pd




def main_view(request):
    df = create_df()

    context = {
        "df": df.to_html()
    }
    return render(request, 'base.html' , context)


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

    df['choice'] = df['choice'].map(lambda x : Choice.objects.get(id=x))

    return df



