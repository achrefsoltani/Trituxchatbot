import { Injectable } from '@angular/core';
import {Observable, Subject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LanguageService {
  private language = 'fr';
  private subject = new Subject<any>();

  constructor() { }

  changeToEnglish(): void {
    this.language = 'en';
    this.subject.next(this.language);
  }

  onLanguageChange(): Observable<any> {
    return this.subject.asObservable();
  }
}
