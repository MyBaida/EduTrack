// angular import
import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { authService } from 'src/app/services/auth/auth.service';
import { loginResponse } from 'src/app/services/auth/interfaces/login';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export default class LoginComponent {
  constructor(private fb: FormBuilder, private auth: authService){}
  loginForm = this.fb.group({
    username: ['', [Validators.required]],
    password: ['', [Validators.required]]
  }) 
  get username() {
    return this.loginForm.get('username');
  }
  get password() {
    return this.loginForm.get('password');
  }

  loginCheck(response : loginResponse){
    if (!response.token){
      
    }
  }

  login() {
    if (this.loginForm.valid) {
      console.log(this.username.value, this.password.value);
      this.auth.Login(this.username.value, this.password.value).subscribe();
    }
  }

}
