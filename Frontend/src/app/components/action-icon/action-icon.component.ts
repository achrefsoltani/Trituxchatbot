import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-action-icon',
  templateUrl: './action-icon.component.html',
  styleUrls: ['./action-icon.component.css']
})
export class ActionIconComponent implements OnInit {

  constructor() { }


  @Input() image: string;

  ngOnInit() {
  }

}
