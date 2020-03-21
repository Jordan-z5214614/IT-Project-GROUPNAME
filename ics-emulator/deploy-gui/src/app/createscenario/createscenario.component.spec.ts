import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreatescenarioComponent } from './createscenario.component';

describe('CreatescenarioComponent', () => {
  let component: CreatescenarioComponent;
  let fixture: ComponentFixture<CreatescenarioComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreatescenarioComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreatescenarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
