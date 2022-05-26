import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Choice} from '../../models/choice';

@Component({
  selector: 'app-choice-list',
  templateUrl: './choice-list.component.html',
  styleUrls: ['./choice-list.component.css']
})
export class ChoiceListComponent implements OnInit {
  @Input() choices: Choice[];
  @Output() answerChoice: EventEmitter<any> = new EventEmitter();

  constructor() { }

  ngOnInit() {
  }

  AnswerChoice(choice: Choice) {
    this.answerChoice.emit({choice});
  }

}
