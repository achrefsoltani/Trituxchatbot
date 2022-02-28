import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { ChatbotComponent } from './chatbot/chatbot.component';
import { LogoComponent } from './logo/logo.component';
import { ChatbotTabComponent } from './chatbot-tab/chatbot-tab.component';
import { ChatbotTitleComponent } from './chatbot-title/chatbot-title.component';
import { DialogBoxComponent } from './dialog-box/dialog-box.component';
import { ActionsBarComponent } from './actions-bar/actions-bar.component';
import { ActionIconComponent } from './action-icon/action-icon.component';
import { MessageComponent } from './message/message.component';
import { ChoiceListComponent } from './choice-list/choice-list.component';
import { ChoiceComponent } from './choice/choice.component';

@NgModule({
  declarations: [
    AppComponent,
    ChatbotComponent,
    LogoComponent,
    ChatbotTabComponent,
    ChatbotTitleComponent,
    DialogBoxComponent,
    ActionsBarComponent,
    ActionIconComponent,
    MessageComponent,
    ChoiceListComponent,
    ChoiceComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
