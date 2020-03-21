import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DeviceconfigComponent } from './deviceconfig.component';

describe('DeviceconfigComponent', () => {
  let component: DeviceconfigComponent;
  let fixture: ComponentFixture<DeviceconfigComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DeviceconfigComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DeviceconfigComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
