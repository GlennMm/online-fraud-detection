import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InvestigateComponent } from './investigate.component';

describe('InvestigateComponent', () => {
  let component: InvestigateComponent;
  let fixture: ComponentFixture<InvestigateComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InvestigateComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(InvestigateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
