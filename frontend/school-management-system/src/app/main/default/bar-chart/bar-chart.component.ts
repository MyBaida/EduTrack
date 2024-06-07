// angular import
import { Component, OnInit, ViewChild } from '@angular/core';

// project import
import { SharedModule } from 'src/app/theme/shared/shared.module';

// third party
import {
  NgApexchartsModule,
  ApexChart,
  ChartComponent,
  ApexDataLabels,
  ApexAxisChartSeries,
  ApexXAxis,
  ApexYAxis,
  ApexTooltip,
  ApexPlotOptions,
  ApexResponsive
} from 'ng-apexcharts';
import { GradesService } from 'src/app/services/dashboard/grades/grades.service';
import { Observable, Subject } from 'rxjs';
import { GradesResponse } from 'src/app/services/dashboard/grades/grades-response';

export type ChartOptions = {
  series: ApexAxisChartSeries;
  chart: ApexChart;
  dataLabels: ApexDataLabels;
  plotOptions: ApexPlotOptions;
  responsive: ApexResponsive[];
  xaxis: ApexXAxis;
  colors: string[];
  yaxis: ApexYAxis;
  tooltip: ApexTooltip;
};

@Component({
  selector: 'app-bar-chart',
  standalone: true,
  imports: [NgApexchartsModule, SharedModule],
  templateUrl: './bar-chart.component.html',
  styleUrl: './bar-chart.component.scss'
})
export class BarChartComponent{
  // public props
  @ViewChild('chart') chart!: ChartComponent;
  chartOptions!: Partial<ChartOptions>;

  // gardes Observable

  grades : GradesResponse[] | undefined;
  // private passedStudents = {
  //   name : "passed",
  //   data : []
  // }

  private failedStudents = {}
  private passedStudentsInSubject(grades: GradesResponse[], subject: string): number {
    const grade = grades.find(grade => grade.subject === subject);
    return grade ? grade.number_of_passed : 0;
  }

  private averageStudentsInSubject(grades: GradesResponse[], subject: string): number {
    const grade = grades.find(grade => grade.subject === subject);
    return grade ? grade.number_of_average : 0;
  }
  private failedStudentsInSubject(grades: GradesResponse[], subject: string): number {
    const grade = grades.find(grade => grade.subject === subject);
    return grade ? grade.number_of_failed : 0;
  }
  constructor(private gradesService: GradesService) {
  gradesService.getGrades(1,1).subscribe(
    response => this.grades = response
  )
  
  

    this.chartOptions = {
      series: [

        {
          name: 'failed',
          data: [35, 125, 35, 35, 35, 80, 35, 20, 35, 45, 15, 75]
          // data: [
          //   this.passedStudentsInSubject(this.grades, 'Math'),
          //   this.passedStudentsInSubject(this.grades, 'Science'),
          //   this.passedStudentsInSubject(this.grades, 'Social'),
          //   this.passedStudentsInSubject(this.grades, 'English'),
          //   this.passedStudentsInSubject(this.grades, 'ICT'),
          //   this.passedStudentsInSubject(this.grades, 'RME'),
          //   this.passedStudentsInSubject(this.grades, 'BDT'),
          //   this.passedStudentsInSubject(this.grades, 'GH.Lang'),
          //   this.passedStudentsInSubject(this.grades, 'French')
          // ]
        },
        {
          name: 'average',
          data: [35, 15, 15, 35, 65, 40, 80, 25, 15, 85, 25, 75]
        },
        {
          name: 'passed',
          data: [35, 145, 35, 35, 20, 105, 100, 10, 65, 45, 30, 10]
        },
        {
          name: 'Maintenance',
          data: [0, 0, 75, 0, 0, 115, 0, 0, 0, 0, 150, 0]
        }
      ],
    
    


      dataLabels: {
        enabled: false
      },
      chart: {
        type: 'bar',
        height: 480,
        stacked: true,
        toolbar: {
          show: true
        },
        background: 'transparent'
      },
      colors: ['#d3eafd', '#2196f3', '#673ab7', '#ede7f6'],
      responsive: [
        {
          breakpoint: 480,
          options: {
            legend: {
              position: 'bottom',
              offsetX: -10,
              offsetY: 0
            }
          }
        }
      ],
      plotOptions: {
        bar: {
          horizontal: false,
          columnWidth: '50%'
        }
      },
      xaxis: {
        type: 'category',
        categories: ['Math', 'Science', 'Social', 'English', 'ICT', 'RME', 'BDT', 'GH.Lang', 'French']
      },
      tooltip: {
        theme: 'light'
      }
    };
  }
  
  
}
