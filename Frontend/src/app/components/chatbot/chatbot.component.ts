import {Component, EventEmitter, OnInit, Output, ViewChild} from '@angular/core';
import {DialogBoxComponent} from "../dialog-box/dialog-box.component";

@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})
export class ChatbotComponent implements OnInit {
  @ViewChild(DialogBoxComponent, {static: false}) dialog: DialogBoxComponent;

  constructor() { }

  @Output()
  toggleDisplay: EventEmitter<any> = new EventEmitter<any>();

  ngOnInit() {
  }

  private Exit() {
    this.toggleDisplay.emit();
  }

  private previousChoice() {
    this.dialog.previousChoice();
  }


}
