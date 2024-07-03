// angular import
import { ChangeDetectorRef, Component,  OnInit, ViewChild } from '@angular/core';

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
import {  GradesService } from 'src/app/services/dashboard/grades/grades.service';
import { allClassesResponse, allSemestersResponse } from 'src/app/services/dashboard/grades/grades-response';
import { Observable } from 'rxjs';
import { GradesResponse } from 'src/app/services/dashboard/grades/grades-response';
import { FormBuilder, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';

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
  imports: [NgApexchartsModule, SharedModule, FormsModule, ReactiveFormsModule],
  templateUrl: './bar-chart.component.html',
  styleUrl: './bar-chart.component.scss'
})
export class BarChartComponent implements OnInit{


  constructor(private gradesService: GradesService, private fb : FormBuilder, private cd: ChangeDetectorRef) {
    this.classes$ = gradesService.getClasses();
    this.semesters$ = gradesService.getSemesters();
  }


  // public props
  @ViewChild('chart') chart!: ChartComponent;
  chartOptions!: Partial<ChartOptions>;

  // grades
  grades : GradesResponse[] | undefined;
  classes$ : Observable<allClassesResponse[]> | undefined;
  semesters$: Observable<allSemestersResponse[]> | undefined;

  semesterToFetch = '';
  classToFetch = '';

  //chart options
  private courses = []
  private failedStudents = []
  private averageStudents = []
  private passedStudents = []

  private sortData(grades : GradesResponse[]){
    this.courses = [];
    this.failedStudents = [];
    this.averageStudents = [];
    this.passedStudents= [];
    grades.forEach(
      (data)=>{
        this.courses.push(data.subjectName);
        this.failedStudents.push(data.number_of_failed);
        this.averageStudents.push(data.number_of_average);
        this.passedStudents.push(data.number_of_passed); 
      }
    );
    this.chartOptions = {
      ...this.chartOptions,
      series: [{
        name: 'Failed Students',
        data: this.failedStudents || []
      }, {
        name: 'Average Students',
        data: this.averageStudents || []
      }, {
        name: 'Passed Students',
        data: this.passedStudents || []
      }],
      xaxis: {
        categories: this.courses || []
      }
    };
    console.log(this.chartOptions)
  
  }


  //Grade submission and class and semester selections
  classSemesterSelectionFrom = this.fb.group({
    semester : ['',[Validators.required]],
    class : ['', [Validators.required]]
  });
  
  get semesterInput(){
    return this.classSemesterSelectionFrom.get('semester')
  }
  get classInput(){
    return this.classSemesterSelectionFrom.get('class')
  }

  classSemesterSelectionFormSubmission(){
    this.gradesService.setCurrentClassAndSemester(this.classToFetch,this.semesterToFetch)
    return this.gradesService.getGrades(this.classToFetch, this.semesterToFetch).subscribe(
      (grades)=> this.sortData(grades)
    )
  }

  


  

ngOnInit(): void {
  this.chartOptions = {
      series: [
        {
          name: 'failed',
          data: this.failedStudents
        },
        {
          name: 'average',
          data: this.averageStudents
        },
        {
          name: 'passed',
          data: this.passedStudents
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
        categories: this.courses
      },
      tooltip: {
        theme: 'light'
      }
    };
}



}
