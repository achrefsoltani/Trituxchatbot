import {Component, Inject, OnInit} from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import {ContactService} from '../../services/contact.service';
import {DataService} from '../../services/data.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {

  chatId: number;


  constructor(private contactService: ContactService,
              private dataService: DataService,
              private dialogRef: MatDialogRef<ContactComponent>,
              @Inject(MAT_DIALOG_DATA) public data: any) { }


  ngOnInit() {
    this.dataService.currentChatId.subscribe(id => this.chatId = id);

  }

  public closeDialog() {
    this.dialogRef.close();
  }

  public onSubmit(contactForm) {
    console.log(this.chatId);
    const form = {
      client: {
        firstName: contactForm.value.firstName,
        lastName: contactForm.value.lastName,
        phone: contactForm.value.phone,
        email: contactForm.value.email,
      },
      content: contactForm.value.content,
      chat: this.chatId
    };
    this.contactService.addContactRequest(form).subscribe();
    this.closeDialog();
  }



}
