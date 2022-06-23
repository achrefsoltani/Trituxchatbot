import {Component, Inject, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialog, MatDialogRef} from '@angular/material/dialog';
import {DemoInfoComponent} from '../demo-info/demo-info.component';

@Component({
  selector: 'app-demo-date',
  templateUrl: './demo-date.component.html',
  styleUrls: ['./demo-date.component.css']
})
export class DemoDateComponent implements OnInit {

  constructor(private dialogRef: MatDialogRef<DemoDateComponent>,
              @Inject(MAT_DIALOG_DATA) public data: any) { }

  ngOnInit() {
  }

   public closeDialog() {
    this.dialogRef.close();
  }



}
