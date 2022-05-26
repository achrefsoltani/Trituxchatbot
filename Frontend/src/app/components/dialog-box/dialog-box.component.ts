/* tslint:disable:one-line */
import {
  AfterViewChecked,
  Component,
  ComponentFactory,
  ComponentFactoryResolver,
  OnInit,
  ViewChild,
  ViewContainerRef
} from '@angular/core';
import {Choice} from '../../models/choice';
import {ChoiceService} from '../../services/choice.service';
import {MessageComponent} from '../message/message.component';
import {ChoiceListComponent} from '../choice-list/choice-list.component';
import {Chat} from '../../models/chat';
import {Message} from '../../models/message';
import {ChatService} from '../../services/chat.service';
import {MessageService} from '../../services/message.service';



@Component({
  selector: 'app-dialog-box',
  templateUrl: './dialog-box.component.html',
  styleUrls: ['./dialog-box.component.css']
})
export class DialogBoxComponent implements OnInit, AfterViewChecked {

  public choices: Choice[] = [];
  public firstChoice: Choice = {
    link_en: '',
    link_fr: '',
    next_choices: [],
    previous_choices: [],
    response_en: '',
    response_fr: '',
    title_en: '',
    title_fr: ''

  };
  public nextChoices: Choice[];
  public selectedChoices: Choice[] = [];
  private messageFactory: ComponentFactory<MessageComponent>;
  private choiceListFactory: ComponentFactory<ChoiceListComponent>;

  // Extract language from website not yet implemented
  private language = 'fr';
  private chat: Chat = {
      language : this.language,
      user : 'Not logged in'
    };

  @ViewChild('componentTarget', {read: ViewContainerRef, static: false}) target: ViewContainerRef;
  @ViewChild('scrolldiv', {static: false}) scrolldiv: any;

  constructor(private choiceService: ChoiceService,
              private chatService: ChatService,
              private messageService: MessageService,
              private componentFactoryResolver: ComponentFactoryResolver) { }

  ngOnInit() {
    this.choiceService.getChoices().subscribe((choices) => {
      this.choices = choices;
      this.firstChoice = choices.find(i => i.id === 25);
      this.nextChoices = choices.filter(element => this.firstChoice.next_choices.includes(element.id));
      this.selectedChoices.push(this.firstChoice);
    });


    this.messageFactory = this.componentFactoryResolver.resolveComponentFactory(MessageComponent);
    this.choiceListFactory = this.componentFactoryResolver.resolveComponentFactory(ChoiceListComponent);


    this.chatService.addChat(this.chat).subscribe((c) => (this.chat = c) );



  }

  ngAfterViewChecked() {
    this.scrollBottom();
  }

  public answerChoice(choice: Choice): void {
    const m = {
      sender: 'user',
      type: 'choice',
      chat: this.chat.id,
      choice_id: choice.id,
    };
    this.messageService.addMessage(m).subscribe();
    this.selectedChoices.push(choice);

    const messagefactory = this.messageFactory;
    const choiceListFactory = this.choiceListFactory;
    const target = this.target;

    if (this.language === 'fr') {
      if (choice.title_fr !== '') {
        const MessageComponentRef = target.createComponent(messagefactory);
        MessageComponentRef.instance.message = choice.title_fr;
        MessageComponentRef.instance.css = 'client';
      }

      if (choice.response_fr !== '') {
        const MessageComponentRef = target.createComponent(messagefactory);
        MessageComponentRef.instance.message = choice.response_fr;
        MessageComponentRef.instance.css = 'chatbot';
      }
    }
    else if (this.language === 'en') {
      if (choice.title_en !== '') {
        const MessageComponentRef = target.createComponent(messagefactory);
        MessageComponentRef.instance.message = choice.title_en;
        MessageComponentRef.instance.css = 'client';
      }

      if (choice.response_en !== '') {
        const MessageComponentRef = target.createComponent(messagefactory);
        MessageComponentRef.instance.message = choice.response_en;
        MessageComponentRef.instance.css = 'chatbot';
      }
    }

    if (choice.next_choices && choice.next_choices.length) {
      const ChoiceListComponentRef = target.createComponent(choiceListFactory);
      ChoiceListComponentRef.instance.choices = this.choices.filter(
        e => choice.next_choices.includes(e.id)
      );
      ChoiceListComponentRef.instance.answerChoice.subscribe($event => {
        this.answerChoice($event.choice);
      });
    }


  }

  public previousChoice() {
    try {
      if ((this.selectedChoices.length) > 1 ) {
      const previousChoiceId = this.selectedChoices[this.selectedChoices.length - 1].previous_choices[0];
      const previousChoice = this.choices.find(i => i.id === previousChoiceId);
      this.answerChoice(previousChoice);
      }
    } catch (e) {
      console.log(e);
    }

  }

  public scrollBottom() {
    this.scrolldiv.nativeElement.scrollTop = this.scrolldiv.nativeElement.scrollHeight;
  }



}
