import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { GradesResponse } from './grades-response';

@Injectable({
  providedIn: 'root'
})
export class GradesService {

  constructor(private http: HttpClient) { }

  private gradesURl(classNumber:number, semester: number)  {
    return `/api/grades/class/${classNumber}/semester/${semester}`
  
 }

 getGrades(classNumber: number, semester: number){
  return this.http.get<GradesResponse[]>(this.gradesURl(classNumber,semester))
 }

}
