import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DemoDateComponent } from './demo-date.component';

describe('DemoDateComponent', () => {
  let component: DemoDateComponent;
  let fixture: ComponentFixture<DemoDateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DemoDateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DemoDateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
