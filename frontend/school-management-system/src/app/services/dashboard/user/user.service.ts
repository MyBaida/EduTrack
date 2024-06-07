import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { UserProfileResponse } from './user-profile-response';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private currentUserUrl = 'api/users/profile';

  constructor(private http: HttpClient ) { }

  getUserDetails(){
    return this.http.get<UserProfileResponse>(this.currentUserUrl)
  }
}
