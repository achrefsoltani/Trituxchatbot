import { Injectable } from '@angular/core';

import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Chat} from '../models/chat';
import {Observable} from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  private apiUrl = 'http://127.0.0.1:8000/app/api/chat/';

  constructor(private http: HttpClient) { }

  addChat(chat: Chat): Observable<Chat> {
    return this.http.post<Chat>(this.apiUrl, chat, httpOptions);
  }
}
