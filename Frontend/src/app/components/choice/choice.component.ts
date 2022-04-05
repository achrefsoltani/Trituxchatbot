import {Component, Input, OnInit} from '@angular/core';
import {Choice} from '../../models/choice';
import {Subscription} from 'rxjs';
import {LanguageService} from '../../services/language.service';

@Component({
  selector: 'app-choice',
  templateUrl: './choice.component.html',
  styleUrls: ['./choice.component.css']
})
export class ChoiceComponent implements OnInit {
  @Input() choice: Choice;
  language: string;
  subscription: Subscription;

  constructor(private languageService: LanguageService) {
    this.subscription = this.languageService.onLanguageChange().subscribe(Value => this.language = Value);
  }

  ngOnInit() {
  }

}
