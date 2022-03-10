import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChatbotTabComponent } from './chatbot-tab.component';

describe('ChatbotTabComponent', () => {
  let component: ChatbotTabComponent;
  let fixture: ComponentFixture<ChatbotTabComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChatbotTabComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChatbotTabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
