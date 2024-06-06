import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, tap } from 'rxjs';
import { loginResponse } from './interfaces/login';

@Injectable({
  providedIn: 'root'
})
export class authService {

  constructor(private http:HttpClient) { }

  private loginUrl = '/api/users/login/';

  // loginSatus =  new BehaviorSubject<boolean>(false);
  // loginStatus$ = this.loginSatus.asObservable();
  isLoggedIn = localStorage.getItem('token') ? true : false;

  Login(username: string, password:string){
    return this.http.post<loginResponse>(this.loginUrl,{username,password},).pipe(
      tap(
        (response)=> {
          if(response.token){
            this.isLoggedIn = true;
            localStorage.setItem('token', response.token);
          }
          else{
            this.isLoggedIn = false;
          }
          
        }
      )
    )
  }



}
