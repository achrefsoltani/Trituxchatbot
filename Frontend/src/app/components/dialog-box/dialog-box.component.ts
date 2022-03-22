import {Component, OnInit} from '@angular/core';
import {Choice} from '../../models/choice';
import {ChoiceService} from '../../services/choice.service';

@Component({
  selector: 'app-dialog-box',
  templateUrl: './dialog-box.component.html',
  styleUrls: ['./dialog-box.component.css']
})
export class DialogBoxComponent implements OnInit {
  choices: Choice[] = [];
  firstChoice: Choice ;
  nextChoices: Choice[];


  constructor(private choiceService: ChoiceService) { }

  ngOnInit() {
    this.choiceService.getChoices().subscribe((choices) => {
      this.choices = choices;
      this.firstChoice = choices.find(i => i.id === 25);
      this.nextChoices = choices.filter(element => this.firstChoice.next_choices.includes(element.id));
    });

    console.log(this.firstChoice);
  }

}
