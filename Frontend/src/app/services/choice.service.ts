import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable, observable, of} from 'rxjs';
import {Choice} from '../models/choice';

@Injectable({
  providedIn: 'root'
})
export class ChoiceService {
  private apiUrl = 'http://127.0.0.1:8000/app/api/choices/';

  constructor(private http: HttpClient) {
  }

  getChoices(): Observable<Choice[]> {
    return this.http.get<Choice[]>(this.apiUrl);
  }
}
