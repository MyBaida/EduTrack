import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, tap } from 'rxjs';
import { loginResponse } from './interfaces/login';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  constructor(private http:HttpClient) { }

  private loginUrl = 'http://127.0.0.1:8000/api/users/login';

  loginSatus =  new BehaviorSubject<boolean>(false);
  loginStatus$ = this.loginSatus.asObservable();


  Login(username: string, passowrd:string){
    return this.http.post<loginResponse>(this.loginUrl,{username,passowrd}).pipe(
      tap(
        (response)=> {
          if(response.token){
            this.loginSatus.next(true);
            localStorage.setItem('token', response.token);
          }
          else{
            this.loginSatus.next(false)
          }
          
        }
      )
    )
  }



}
