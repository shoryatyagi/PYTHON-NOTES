import csv


with open("./Code/csv_module/random_data.csv","w") as f:
    #writing data through list
    csv_writer = csv.writer(f)
    csv_writer.writerow(["name","email","number","description"])
    csv_writer.writerow(["Shorya","shoryatyagi29@gmail.com",975790504,"Hello folks!"])
    csv_writer.writerow(["yash","yash@1.com",958593,"12th grade student"])
    csv_writer.writerow(["dev","hello@gamil.com",345454,"CSE student"])

with open("./Code/csv_module/random_data.csv","r") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)

with open("./Code/csv_module/random_data.csv","r") as f:
    csv_reader = csv.DictReader(f)
    for line in csv_reader:
        print(line)

with open("./Code/csv_module/random_data.csv","w") as f:
    # writing data through dictionary
    data = [{"name": "Shorya","email": "shoryatyagi29@gmail.com", "number":90877,"description":"Hello i am undergrad student"},
            {"name": "Yash","email": "yash@1.com", "number":9879,"description":"12th grade student"},
    {"name": "love","email": "hello@gamil.com", "number":345454,"description":"CSE student"}]

    fields = ["name","email","number","description"]
    writer = csv.DictWriter(f,fieldnames=fields, delimiter='\t')
    writer.writeheader()

    writer.writerows(data)
    print("data inserted successfully")