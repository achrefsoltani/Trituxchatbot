import {Component, Inject, Input, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialog, MatDialogRef} from '@angular/material/dialog';
import {DemoInfoComponent} from '../demo-info/demo-info.component';
import {DemoService} from '../../services/demo.service';
import {NgForm} from "@angular/forms";

@Component({
  selector: 'app-demo-date',
  templateUrl: './demo-date.component.html',
  styleUrls: ['./demo-date.component.css']
})
export class DemoDateComponent implements OnInit {
  public demos: any[];
  @Input() form: NgForm;
  private service: string;
  private fName: string;
  private email: string;
  private lName: string;
  private phone: string;

  constructor(private dialogRef: MatDialogRef<DemoDateComponent>,
              @Inject(MAT_DIALOG_DATA) public data: any,
              private demoService: DemoService) {
    this.form = this.data.form;
    this.service = this.form.value.service;
    this.fName = this.form.value.firstName;
    this.lName = this.form.value.lastName;
    this.phone = this.form.value.phone;
    this.email = this.form.value.email;
  }

  ngOnInit() {
    this.demoService.getDemos(this.form.value.service).subscribe((demos) => {
      this.demos = demos;
    });
  }

   public closeDialog() {
    this.dialogRef.close();
  }

  public onSubmit(f: NgForm) {
    console.log(this.email);
    console.log(f.value);
  }



}
