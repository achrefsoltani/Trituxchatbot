import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { contactRequest} from '../models/contactRequest';
import {Observable} from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};
@Injectable({
  providedIn: 'root'
})
export class ContactService {
  private apiUrl = 'http://127.0.0.1:8000/app/api/cr/';

  constructor(private http: HttpClient) { }

  addContactRequest(cr: contactRequest): Observable<contactRequest> {
    return this.http.post<contactRequest>(this.apiUrl, cr, httpOptions);
  }
}
