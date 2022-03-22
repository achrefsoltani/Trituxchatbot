import {Component, Input, OnInit} from '@angular/core';
import {Choice} from '../../models/choice';

@Component({
  selector: 'app-choice',
  templateUrl: './choice.component.html',
  styleUrls: ['./choice.component.css']
})
export class ChoiceComponent implements OnInit {
  @Input() choice: Choice;

  constructor() { }

  ngOnInit() {
  }

}
