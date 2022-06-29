import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable, Observer} from 'rxjs';
import {DemoRequest} from '../models/demoRequest';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class DemoService {
  private apiUrl = 'http://127.0.0.1:8000/app/api/dr/';

  constructor(private http: HttpClient) { }

  getDemos(id: string): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl + id);
  }

  addDemoRequest(dr: DemoRequest): Observable<DemoRequest> {
    return this.http.post<DemoRequest>(this.apiUrl, dr, httpOptions);
  }
}
