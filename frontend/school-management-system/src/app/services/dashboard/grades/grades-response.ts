export interface GradesResponse {
    className: number,
    class_id: number
    semester: string,
    subjectName: string,
    number_of_passed: number, 
    number_of_average: number,
    number_of_failed: number,
    date_recorded: string
}

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

  export interface gradeStatisticsAllSemesters{
    student_name: string
    student_id: number,
    semester_scores: [
    {
      semester_name: string,
      total_score: number
    }
  ]
  }
  