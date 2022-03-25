import {
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



@Component({
  selector: 'app-dialog-box',
  templateUrl: './dialog-box.component.html',
  styleUrls: ['./dialog-box.component.css']
})
export class DialogBoxComponent implements OnInit {
  choices: Choice[] = [];
  firstChoice: Choice = {
    link_en: '',
    link_fr: '',
    next_choices: [],
    previous_choices: [],
    response_en: '',
    response_fr: '',
    title_en: '',
    title_fr: ''

  };
  nextChoices: Choice[];
  selectedChoices: Choice[] = [];

  private messageFactory: ComponentFactory<MessageComponent>;
  private choiceListFactory: ComponentFactory<ChoiceListComponent>;

  @ViewChild('componentTarget', {read: ViewContainerRef, static: false}) target: ViewContainerRef;
  @ViewChild('scrolldiv', {static: false}) scrolldiv: any;

  constructor(private choiceService: ChoiceService, private componentFactoryResolver: ComponentFactoryResolver) { }

  ngOnInit() {
    this.choiceService.getChoices().subscribe((choices) => {
      this.choices = choices;
      this.firstChoice = choices.find(i => i.id === 25);
      this.nextChoices = choices.filter(element => this.firstChoice.next_choices.includes(element.id));
      this.selectedChoices.push(this.firstChoice);
    });


    this.messageFactory = this.componentFactoryResolver.resolveComponentFactory(MessageComponent);
    this.choiceListFactory = this.componentFactoryResolver.resolveComponentFactory(ChoiceListComponent);



  }

  public answerChoice(choice: Choice): void {
    this.selectedChoices.push(choice);
    console.log(this.selectedChoices);

    const messagefactory = this.messageFactory;
    const choiceListFactory = this.choiceListFactory;
    const target = this.target;

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
    if ((this.selectedChoices.length) > 2) {
      const choiceListFactory = this.choiceListFactory;
      const target = this.target;
      this.selectedChoices.pop();
      const choice = this.selectedChoices[this.selectedChoices.length - 1];

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
  }

  public scrollBottom() {
    this.scrolldiv.nativeElement.scrollTop = this.scrolldiv.nativeElement.scrollHeight;
  }


}
