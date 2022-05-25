import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule} from '@angular/common/http';

import { AppComponent } from './app.component';
import { ChatbotComponent } from './components/chatbot/chatbot.component';
import { LogoComponent } from './components/logo/logo.component';
import { ChatbotTabComponent } from './components/chatbot-tab/chatbot-tab.component';
import { ChatbotTitleComponent } from './components/chatbot-title/chatbot-title.component';
import { DialogBoxComponent } from './components/dialog-box/dialog-box.component';
import { ActionsBarComponent } from './components/actions-bar/actions-bar.component';
import { ActionIconComponent } from './components/action-icon/action-icon.component';
import { MessageComponent } from './components/message/message.component';
import { ChoiceListComponent } from './components/choice-list/choice-list.component';
import { ChoiceComponent } from './components/choice/choice.component';
import { InputComponent } from './components/input/input.component';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import {MatInputModule} from '@angular/material/input';


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
    ChoiceComponent,
    InputComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    NoopAnimationsModule,
    MatInputModule
  ],
  entryComponents: [
    MessageComponent,
    ChoiceListComponent,
    InputComponent,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
