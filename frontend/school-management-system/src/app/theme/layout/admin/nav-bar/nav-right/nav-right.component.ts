// Angular import
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { UserProfileResponse } from 'src/app/services/dashboard/user/user-profile-response';
import { UserService } from 'src/app/services/dashboard/user/user.service';

@Component({
  selector: 'app-nav-right',
  templateUrl: './nav-right.component.html',
  styleUrls: ['./nav-right.component.scss']
})
export class NavRightComponent implements OnInit{

  profileData$ : Observable<UserProfileResponse> | undefined

  constructor(private profile:UserService ){}
ngOnInit(): void {
  this.profileData$ = this.profile.getUserDetails()
}

}
