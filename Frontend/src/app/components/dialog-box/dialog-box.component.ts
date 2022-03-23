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
import {element} from "protractor";


@Component({
  selector: 'app-dialog-box',
  templateUrl: './dialog-box.component.html',
  styleUrls: ['./dialog-box.component.css']
})
export class DialogBoxComponent implements OnInit {
  choices: Choice[] = [];
  firstChoice: Choice ;
  nextChoices: Choice[];

  private messageFactory: ComponentFactory<MessageComponent>;
  private choiceListFactory: ComponentFactory<ChoiceListComponent>;

  @ViewChild('componentTarget', {read: ViewContainerRef, static: false}) target: ViewContainerRef;

  constructor(private choiceService: ChoiceService, private componentFactoryResolver: ComponentFactoryResolver) { }

  ngOnInit() {
    this.choiceService.getChoices().subscribe((choices) => {
      this.choices = choices;
      this.firstChoice = choices.find(i => i.id === 25);
      this.nextChoices = choices.filter(element => this.firstChoice.next_choices.includes(element.id));
    });

    this.messageFactory = this.componentFactoryResolver.resolveComponentFactory(MessageComponent);
    this.choiceListFactory = this.componentFactoryResolver.resolveComponentFactory(ChoiceListComponent);
  }

  public answerChoice(choice: Choice): void {
    const messagefactory = this.messageFactory;
    const choiceListFactory = this.choiceListFactory;
    const target = this.target;

    const MessageComponentRef = target.createComponent(messagefactory);
    MessageComponentRef.instance.message = choice.title_en;

    const ChoiceListComponentRef = target.createComponent(choiceListFactory);
    ChoiceListComponentRef.instance.choices = this.choices.filter(
      e => choice.next_choices.includes(e.id)
    );
    ChoiceListComponentRef.instance.answerChoice.subscribe($event => {
      this.answerChoice($event.choice);
    });


  }

}
