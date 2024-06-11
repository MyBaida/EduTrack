import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AuthenticationRoutingModule } from './authentication-routing.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import LoginComponent from './login/login.component';
import { RouterModule } from '@angular/router';
import RegisterComponent from './register/register.component';

@NgModule({
  declarations: [LoginComponent, RegisterComponent],
  imports: [CommonModule,RouterModule,AuthenticationRoutingModule, ReactiveFormsModule, FormsModule]
})
export class AuthenticationModule {}
