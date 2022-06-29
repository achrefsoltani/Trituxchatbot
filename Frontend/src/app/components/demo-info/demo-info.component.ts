import {Component, Inject, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialog, MatDialogRef} from '@angular/material/dialog';
import {DemoDateComponent} from '../demo-date/demo-date.component';
import {NgForm} from '@angular/forms';

@Component({
  selector: 'app-demo-info',
  templateUrl: './demo-info.component.html',
  styleUrls: ['./demo-info.component.css']
})
export class DemoInfoComponent implements OnInit {

  constructor(private matDialog: MatDialog,
              private dialogRef: MatDialogRef<DemoInfoComponent>,
              @Inject(MAT_DIALOG_DATA) public data: any) { }

  ngOnInit() {
  }

  public closeDialog() {
    this.dialogRef.close();
  }

  public showDemoDate(f: NgForm) {
    this.matDialog.open(DemoDateComponent, {data: {form: f}, width : '50%'});
  }

  public onSubmit(f: NgForm) {
    this.dialogRef.close();
    this.showDemoDate(f);
  }

}
