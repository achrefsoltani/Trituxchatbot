import {Component, EventEmitter, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-chatbot-title',
  templateUrl: './chatbot-title.component.html',
  styleUrls: ['./chatbot-title.component.css']
})
export class ChatbotTitleComponent implements OnInit {

  constructor() { }

 @Output()
  toggleDisplay: EventEmitter<any> = new EventEmitter<any>();

  ngOnInit() {
  }

  Exit() {
    this.toggleDisplay.emit();
  }
}

