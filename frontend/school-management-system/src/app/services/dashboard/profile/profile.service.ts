import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ProfileResponse } from './profile-response';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  constructor(private http: HttpClient) { }
  private profileUrl = '/api/users/profile';

  getProfile(){
    return this.http.get<ProfileResponse>(this.profileUrl)
  }
}
