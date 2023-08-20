def read_csv(path = ''):
    if (path == ''):
       return []
    csv_file = open(path)
    csv_file_data = csv_file.readlines()
    columns = []
    main_list = []
    for i in range(0, len(csv_file_data)):
        csv_file_data_item = csv_file_data[i].replace('\n', '')
        csv_file_data_item = csv_file_data_item.split(',')
        if i == 0:
            columns = csv_file_data_item
        else:
            dict = {}
            for l in range(0, len(columns)):
                dict[columns[l]] = csv_file_data_item[l]
            main_list.append(dict)
    csv_file_data.close()
    return main_list

def calculate_grade_point(subjectMarks, subject_grade_point):
    gradePoint = 0
    if subjectMarks >= 90:
      gradePoint += 10 * subject_grade_point
    elif subjectMarks >= 80:
      gradePoint += 8 * subject_grade_point
    elif subjectMarks >= 70:
      gradePoint += 6 * subject_grade_point
    elif subjectMarks >= 60:
      gradePoint += 4 * subject_grade_point
    elif subjectMarks >= 50:
      gradePoint += 2 * subject_grade_point
    return gradePoint

def calculate_grade(sgpa):
    grades = ['A', 'B', 'C', 'D', 'E', 'F']
    grade_key = len(grades)
    if sgpa== 10:
      grade_key = 0
    elif sgpa>= 8 and sgpa< 10:
      grade_key = 1
    elif sgpa>= 6 and sgpa< 8:
      grade_key = 2
    elif sgpa>= 4 and sgpa< 6:
      grade_key = 3
    elif sgpa>= 2 and sgpa< 4:
      grade_key = 4
    return grades[grade_key]


if __name__ == '__main__':
    total_points = 15
    file_name = 'sample_data_cgpa'
    read_file_path = ('./sample-data/{}.csv').format(file_name)
    data = read_csv(read_file_path)
    if data:
        enriched_data = []
        for i in range(0, len(data)):
            enriched = data[i]
            field_name = list(enriched.keys())
            field_name = [field for field in field_name if field.lower() != 'name' and field.lower() != 'rollnumber' and field.lower() != 'trade']
            per_subject_points = total_points / len(field_name)
            grade_points = 0
            for field_key in field_name:
                grade_points += float(enriched[field_key])
            enriched['sgpa'] = round(grade_points / total_points, 2)
            enriched['grade'] = calculate_grade(enriched['sgpa'])
            enriched_data.append(enriched)
        if (len(enriched_data) > 0):
            all_keys = enriched_data[0].keys()
            keys = ('{}\n').format(",".join(all_keys))
            new_file_data = [keys]
            for enriched in enriched_data:
                row_record = []
                for keys in all_keys:
                    row_record.append(str(enriched[keys]))
                new_file_data.append(('{}\n').format(",".join(row_record)))
            new_file_name = 'sample_data_cgpa_edited'
            new_file_path = ('./sample-data/{}_enriched.csv').format(new_file_name)
            new_file = open(new_file_path, 'w')
            new_file.write("".join(new_file_data))
            new_file.close()
            print("File saved")
    else:
       print('Please select a file')