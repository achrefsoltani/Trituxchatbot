import {Component, EventEmitter, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-actions-bar',
  templateUrl: './actions-bar.component.html',
  styleUrls: ['./actions-bar.component.css']
})
export class ActionsBarComponent implements OnInit {

  constructor() { }

  @Output()
  back: EventEmitter<any> = new EventEmitter<any>();

  ngOnInit() {
  }

  public previous() {
    this.back.emit();
  }

}
