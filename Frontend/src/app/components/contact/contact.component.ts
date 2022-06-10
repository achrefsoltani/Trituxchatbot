import {Component, Inject, OnInit} from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import {ContactService} from '../../services/contact.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {

  constructor(private contactService: ContactService,
              private dialogRef: MatDialogRef<ContactComponent>,
              @Inject(MAT_DIALOG_DATA) public data: any) { }

  lastName: string;

  ngOnInit() {
  }

  public closeDialog() {
    this.dialogRef.close();
  }

  public onSubmit(contactForm) {

    const form = {
      client: {
        firstName: contactForm.value.firstName,
        lastName: contactForm.value.lastName,
        phone: contactForm.value.phone,
        email: contactForm.value.email,
      },
      content: contactForm.value.content,
      chat: 710
    };
    this.contactService.addContactRequest(form).subscribe();
    this.closeDialog();
  }



}
