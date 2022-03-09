import {Component, EventEmitter, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})
export class ChatbotComponent implements OnInit {

  constructor() { }

  @Output()
  toggleDisplay: EventEmitter<any> = new EventEmitter<any>();

  ngOnInit() {
  }

  Exit() {
    this.toggleDisplay.emit();
  }

}
