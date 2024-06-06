// angular import
import { Component, viewChild, ViewChild } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { delay } from 'rxjs';
import { authService } from 'src/app/services/auth/auth.service';
import { loginResponse } from 'src/app/services/auth/interfaces/login';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export default class LoginComponent {
  constructor(private fb: FormBuilder, private auth: authService, private router: Router){}
  alertMessage={
    type:'success' || 'warning' || 'danger'||  '', 
    message: '',
}



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
      this.alertMessage={
        type: 'warning',
        message:'Invalid username or password. Please try again later'
      }
    }
    else{
      this.alertMessage={
        type: 'success',
        message:`Welcome ${response.name}. Redirecting to dashboard...`
      }

      setTimeout(
        ()=>{
          return this.router.navigate(['/dashboard'])
        },2000
      )
     
    }
  }

  login() {
    if (this.loginForm.valid) {
      console.log(this.username.value, this.password.value);
      this.auth.Login(this.username.value, this.password.value).subscribe(
        response => this.loginCheck(response),
        (error)=>{
          this.alertMessage={
            type: 'danger',
            message:'An error occured. Please try again later'
          }
           return console.log(error);
        }
      );
    }
  }

}
