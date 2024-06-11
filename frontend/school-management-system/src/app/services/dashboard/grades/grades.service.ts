import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { GradesResponse } from './grades-response';

export interface allClassesResponse {
  className: string
  class_id: number
  school: string
}

export interface allSemestersResponse{
  _id: number
  name: string
  start_date: string
  end_date: string
}




@Injectable({
  providedIn: 'root'
})
export class GradesService {

  constructor(private http: HttpClient) { }

  private gradesURl(classNumber:number, semester: number)  {
    return `/api/classes/${classNumber}/semester/${semester}/subject-statistics`
 };

 private allClassesUrl = '/api/classes'
 private allSemestersUrl = 'api/semesters'

 getGrades(classNumber, semesterId){
  return this.http.get<GradesResponse[]>(this.gradesURl(classNumber,semesterId))
 }

 getClasses(){
  return this.http.get<allClassesResponse[]>(this.allClassesUrl)
 }

 getSemesters(){
  return this.http.get<allSemestersResponse[]>(this.allSemestersUrl)
 }


}
