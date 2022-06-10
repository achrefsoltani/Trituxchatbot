import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private chatIdSource = new BehaviorSubject<number>(22);
  currentChatId = this.chatIdSource.asObservable();

  constructor() { }

  changeChatId(id: number) {
    this.chatIdSource.next(id);
  }
}
