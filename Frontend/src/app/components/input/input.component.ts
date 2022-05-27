import {Component, EventEmitter, OnInit, Output, ViewChild} from '@angular/core';
import {fakeAsync} from "@angular/core/testing";

@Component({
  selector: 'app-input',
  templateUrl: './input.component.html',
  styleUrls: ['./input.component.css']
})
export class InputComponent implements OnInit {
  message = '';

  constructor() { }

  @Output()
  messageReceived: EventEmitter<any> = new EventEmitter<any>();

  @ViewChild('input', {static: false}) inputValue;


  ngOnInit() {
  }

  getMessage(val: string) {
    this.message = val;
    this.inputValue.nativeElement.value = '';
    this.messageReceived.emit();
  }

}
