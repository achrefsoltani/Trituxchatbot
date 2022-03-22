import {Component, Input, OnInit} from '@angular/core';
import {Choice} from '../../models/choice';

@Component({
  selector: 'app-choice-list',
  templateUrl: './choice-list.component.html',
  styleUrls: ['./choice-list.component.css']
})
export class ChoiceListComponent implements OnInit {
  @Input() choices: Choice[];

  constructor() { }

  ngOnInit() {
  }

}
