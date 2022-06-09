import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {MatDialog, MatDialogConfig} from '@angular/material/dialog';
import {ContactComponent} from '../contact/contact.component';


@Component({
  selector: 'app-actions-bar',
  templateUrl: './actions-bar.component.html',
  styleUrls: ['./actions-bar.component.css']
})
export class ActionsBarComponent implements OnInit {

  constructor(private matDialog: MatDialog) { }

  @Output()
  back: EventEmitter<any> = new EventEmitter<any>();

  @Output()
  reset: EventEmitter<any> = new EventEmitter<any>();


  ngOnInit() {
  }

  public previous() {
    this.back.emit();
  }

  public resetDialog() {
    this.reset.emit();
  }

  public showContact() {
    this.matDialog.open(ContactComponent, {data: {}, width : '50%'});
  }


}
