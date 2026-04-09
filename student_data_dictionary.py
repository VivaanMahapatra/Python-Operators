student_data = {
    "id1" : {"name":"sarah", "class":"V", "subject_integration" : "english, math, science"},
    "id2" : {"name":"david", "class":"V", "subject_integration" : "english, math, science"},
    "id3" : {"name":"sarah", "class":"V", "subject_integration" : "english, math, science"},
    "id4" : {"name":"surya", "class":"V", "subject_integration" : "english, math, science"},
}

results = {}
seen_keys = []
for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        results[student_id] = details
for k, v in results.items():
    print(k,":", v)
    
