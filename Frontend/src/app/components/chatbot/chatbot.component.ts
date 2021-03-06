import {Component, EventEmitter, OnInit, Output, ViewChild, ViewContainerRef} from '@angular/core';
import {DialogBoxComponent} from '../dialog-box/dialog-box.component';
import {InputComponent} from "../input/input.component";


@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})
export class ChatbotComponent implements OnInit {
  @ViewChild(DialogBoxComponent, {static: false}) dialog: DialogBoxComponent;
  @ViewChild(InputComponent, {static: false}) input : InputComponent;

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

  private resetDialog() {
    this.dialog.target.clear();
    this.dialog.ngOnInit();
  }

  private answerMessage() {
    this.dialog.answerMessage(this.input.message);
  }


}
