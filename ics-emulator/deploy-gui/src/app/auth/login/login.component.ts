import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginForm: FormGroup;
  constructor(private _fb: FormBuilder) {}

  ngOnInit() {
    this.loginForm = this._fb.group({
      email: ['', Validators.required],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });
  }

  login() {
    if (!this.loginForm.valid) return;
    console.log(this.loginForm.value);
  }

  private get email() {
    return this.loginForm.get('email');
  }
  private get password() {
    return this.loginForm.get('password');
  }
}
