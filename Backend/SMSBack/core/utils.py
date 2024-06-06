from collections import defaultdict

def transform_grades(data):
    transformed_data = defaultdict(lambda: {
        'student': '',
        'student_id': '',
        'semester': '',
        'grades': {},
        'date_recorded': None,
    })
    
    for item in data:
        student_id = item['student_id']
        transformed_data[student_id]['student'] = item['student']
        transformed_data[student_id]['student_id'] = student_id
        transformed_data[student_id]['semester'] = item['semester']
        transformed_data[student_id]['grades'][item['subject']] = item['grade']
        transformed_data[student_id]['date_recorded'] = item['date_recorded']
    
    return list(transformed_data.values())
