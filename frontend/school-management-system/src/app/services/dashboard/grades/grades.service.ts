import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { GradesResponse } from './grades-response';
import { map, Subject } from 'rxjs';

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

export interface  topAndWorstPerformanceResponse{
  top_students: [{
    class_name: string
    student_name:string
    student_id: number
    semester: string
    total_score: number
  }]

  bottom_students: [{
    class_name: string
    student_name:string
    student_id: number
    semester: string
    total_score: number
  }]

}

export interface classAndSemesterSharing {
  classId : number
  semesterID: number
}



@Injectable({
  providedIn: 'root'
})
export class GradesService {

  constructor(private http: HttpClient) { }


  // grades endpoints
  private gradesURl(classNumber:number, semester: number)  {
    return `/api/classes/${classNumber}/semester/${semester}/subject-statistics`
 };
 private topAndWorstPerformanceUrl(classNumber: number,semester:number){
  return `api/classes/${classNumber}/semester/${semester}/top-students/`
 } 

// Handle current semester and class
private currentClassAndSemester = new Subject<classAndSemesterSharing>()


currentClassAndSemester$ = this.currentClassAndSemester.asObservable()



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

 getStudentPerformance(classNumber, semesterId){
  return this.http.get<topAndWorstPerformanceResponse>(this.topAndWorstPerformanceUrl(classNumber,semesterId))

 }

 setCurrentClassAndSemester(classNumber, semesterID){
  return this.currentClassAndSemester.next({classId: classNumber, semesterID})
 }


}
