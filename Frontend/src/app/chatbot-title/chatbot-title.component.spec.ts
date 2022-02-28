import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChatbotTitleComponent } from './chatbot-title.component';

describe('ChatbotTitleComponent', () => {
  let component: ChatbotTitleComponent;
  let fixture: ComponentFixture<ChatbotTitleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChatbotTitleComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChatbotTitleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
