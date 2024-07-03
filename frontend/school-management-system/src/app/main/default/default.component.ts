// Angular Import
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

// project import
import { SharedModule } from 'src/app/theme/shared/shared.module';
import { BarChartComponent } from './bar-chart/bar-chart.component';
import { ChartDataMonthComponent } from './chart-data-month/chart-data-month.component';
import { ProfileService } from 'src/app/services/dashboard/profile/profile.service';
import { Observable } from 'rxjs';
import { GradesResponse, gradeStatisticsAllSemesters, topAndWorstPerformanceResponse } from 'src/app/services/dashboard/grades/grades-response';
import { FormsModule } from '@angular/forms';
import { PerformanceChartComponent } from './performance-chart/performance-chart';
import { GradesService } from 'src/app/services/dashboard/grades/grades.service';
import { classAndSemesterSharing } from 'src/app/services/dashboard/grades/grades-response';

@Component({
  selector: 'app-default',
  standalone: true,
  imports: [CommonModule, SharedModule, PerformanceChartComponent, BarChartComponent, ChartDataMonthComponent],
  templateUrl: './default.component.html',
  styleUrls: ['./default.component.scss']
})
export class DefaultComponent  {

  constructor(private gradesService : GradesService ){
    gradesService.currentClassAndSemester$.subscribe(
      (response)=>{
        gradesService.getStudentsPerformance(response.classId, response.semesterID).subscribe(
          (data)=>{
            let top_students = data.top_students.map(
              (student) => {
                return ({
                  name: student.student_name,
                  student_id : student.student_id,                  score: student.total_score,
                  bgColor: 'bg-light-success',
                  icon: 'ti ti-chevron-up',
                  color: 'text-success'
                })
              }
            )
                  
            let bottom_students = data.bottom_students.map(
              (student) => {
                return ({
                  name: student.student_name,
                  student_id : student.student_id,
                  score: student.total_score,
                  bgColor: 'bg-light-danger',
                  icon: 'ti ti-chevron-down',
                  color: 'text-danger'
                })
              }
            ) 
            return this.performanceList = [...top_students, ...bottom_students]
              }
            )
          }
        )
      }
  
  

  
  performanceList = []

  // public method
  // ListGroup = [
  //   {
  //     name: 'Bajaj Finery',
  //     profit: '10% Profit',
  //     invest: '$1839.00',
  //     bgColor: 'bg-light-success',
  //     icon: 'ti ti-chevron-up',
  //     color: 'text-success'
  //   },
  //   {
  //     name: 'TTML',
  //     profit: '10% Loss',
  //     invest: '$100.00',
  //     bgColor: 'bg-light-danger',
  //     icon: 'ti ti-chevron-down',
  //     color: 'text-danger'
  //   },
  //   {
  //     name: 'Reliance',
  //     profit: '10% Profit',
  //     invest: '$200.00',
  //     bgColor: 'bg-light-success',
  //     icon: 'ti ti-chevron-up',
  //     color: 'text-success'
  //   },
  //   {
  //     name: 'ATGL',
  //     profit: '10% Loss',
  //     invest: '$189.00',
  //     bgColor: 'bg-light-danger',
  //     icon: 'ti ti-chevron-down',
  //     color: 'text-danger'
  //   },
  //   {
  //     name: 'Stolon',
  //     profit: '10% Profit',
  //     invest: '$210.00',
  //     bgColor: 'bg-light-success',
  //     icon: 'ti ti-chevron-up',
  //     color: 'text-success',
  //     space: 'pb-0'
  //   }
  // ];


//fetch specific student performance across semesters
studentGradeDataAllSemesters : gradeStatisticsAllSemesters
getStudentPerformance(id){
  this.gradesService.getStudentGradeStatisticsAllSemesters(id).subscribe(
    data => this.studentGradeDataAllSemesters = data
  )
}




  profileCard = [
    {
      style: 'bg-primary-dark text-white',
      background: 'bg-primary',
      value: '$203k',
      text: 'Net Profit',
      color: 'text-white',
      value_color: 'text-white'
    },
    {
      background: 'bg-warning',
      avatar_background: 'bg-light-warning',
      value: '$550K',
      text: 'Total Revenue',
      color: 'text-warning'
    }
  ];
}
