// angular import
import { Component, Input, OnChanges, SimpleChanges, ViewChild } from '@angular/core';

// project import
import { SharedModule } from 'src/app/theme/shared/shared.module';

// third party
import {
  NgApexchartsModule,
  ApexChart,
  ChartComponent,
  ApexDataLabels,
  ApexAxisChartSeries,
  ApexTooltip,
  ApexPlotOptions,
  ApexResponsive,
  ApexStroke,
  ApexXAxis,
  ApexTitleSubtitle
} from 'ng-apexcharts';
import { GradesService } from 'src/app/services/dashboard/grades/grades.service';
import { gradeStatisticsAllSemesters } from 'src/app/services/dashboard/grades/grades-response';

export type ChartOptions = {
  series: ApexAxisChartSeries;
  chart: ApexChart;
  title: ApexTitleSubtitle;
  subtitle: ApexTitleSubtitle;
  dataLabels: ApexDataLabels;
  plotOptions: ApexPlotOptions;
  responsive: ApexResponsive[];
  xaxis: ApexXAxis;
  colors: string[];
  stroke: ApexStroke;
  tooltip: ApexTooltip;
};

@Component({
  selector: 'app-performance-chart',
  standalone: true,
  imports: [SharedModule, NgApexchartsModule],
  templateUrl: './performance-chart.html',
  styleUrl: './performance-chart.scss'
})
export class PerformanceChartComponent implements OnChanges {
  // public props
  @ViewChild('chart') chart!: ChartComponent;
  chartOptions!: Partial<ChartOptions>;

  @Input() data : gradeStatisticsAllSemesters

  // constructor
  constructor() {
    this.chartOptions = {
      chart: {
        type: 'area',
        height: 95,
        stacked: true,
        sparkline: {
          enabled: true
        },
        background: 'transparent'
      },
      stroke: {
        curve: 'smooth',
        width: 1
      },
      series: [
        {
          data: this.semesterScores
        }
      ],
      tooltip: {
        theme: 'light',
        fixed: {
          enabled: false
        },
        marker: {
          show: false
        }
      },
      xaxis: {
        type: 'category',
        categories: this.semesters
      },
      colors: ['#673ab7']
    };
  }

  semesters = []
  semesterScores = []
  studentName = ''

  //helper functions
  private sortData(scoresData : gradeStatisticsAllSemesters){
    //reset properties
    this.semesters =[]
    this.semesterScores = []
    this.studentName = ''

    //sort data
    this.studentName = scoresData.student_name
    scoresData.semester_scores.forEach(
      score => {
        this.semesters.push(score.semester_name)
        this.semesterScores.push(score.total_score)
      }
    )
    this.chartOptions = {
      ...this.chartOptions,
      series: [
        {
          data: this.semesterScores
        }
      ],
      xaxis: {
        categories: this.semesters
      },
      title: {
        text: this.studentName
      }
    }
  }

ngOnChanges(changes: SimpleChanges): void {
  this.sortData(this.data)
}

}
