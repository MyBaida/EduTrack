import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { allClassesResponse, allSemestersResponse, classAndSemesterSharing, GradesResponse, gradeStatisticsAllSemesters, topAndWorstPerformanceResponse } from './grades-response';
import { map, Subject } from 'rxjs';


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
 private gradeStatisticsAllSemesters(student_id){
  return `api/students/${student_id}/semesters-scores/`
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

 getStudentsPerformance(classNumber, semesterId){
  return this.http.get<topAndWorstPerformanceResponse>(this.topAndWorstPerformanceUrl(classNumber,semesterId))

 }

 getStudentGradeStatisticsAllSemesters(student_id){
  return this.http.get<gradeStatisticsAllSemesters>(this.gradeStatisticsAllSemesters(student_id))
 }

 setCurrentClassAndSemester(classNumber, semesterID){
  return this.currentClassAndSemester.next({classId: classNumber, semesterID})
 }


}
