import fitz
import re
import csv

def extract_answers_from_pdfs(pdf_files):
    for i, pdf_file in enumerate(pdf_files):
        answers = []

        with fitz.open(pdf_file) as doc:
            page_number = 5  # 6th page, starting from 0
            page = doc.load_page(page_number)
            text = page.get_text()
# r'^(?:[1-9]|[1-4][0-9]|52)\s[A-D]$
            # Extract answers using regular expressions
            answer_matches = re.findall(r'\b(?:[1-9]|[1-4][0-9]|52)\s[A-D]\b', text)

            # Add the extracted answers to the list
            answers.extend(answer_matches)

        # Write the extracted answers to the output text file
        output_file = f'ANSWERS/ANSWERS{i+1}.txt'
        with open(output_file, 'w') as file:
            for answer in answers:
                file.write(answer + '\n')





def group_answers_to_csv(input_file, ranges, output_files):
    with open(input_file, 'r') as file:
        answers = file.readlines()

    for i, (start, end) in enumerate(ranges):
        grouped_answers = answers[start-1:end]
        output_file = output_files[i]

        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for answer in grouped_answers:
                writer.writerow([answer.strip()])



def Concat_Reading_Ans(file1,file2,v): 
    header=[f"TEST{v}"]
    newfile1 = re.sub(r'\.', '', file1)
    newfile2 = re.sub(r'\.', '', file2)
    with open(file1, 'r') as file1:
        csv_reader1 = csv.reader(file1)
        data1 = list(csv_reader1)

    with open(file2, 'r') as file2:
        csv_reader2 = csv.reader(file2)
        data2 = list(csv_reader2)

    concatenated_data = data1 + data2
    output_file=f'READINGANSWERS/Reading{v}.csv'

    with open(output_file, 'w', newline='') as output:
        csv_writer = csv.writer(output)
        csv_writer.writerow(header)
        csv_writer.writerows(concatenated_data)
    
    

 
pdf_files = ['answersheetpdfs/s1.pdf','answersheetpdfs/s2.pdf','answersheetpdfs/s3.pdf','answersheetpdfs/s4.pdf','answersheetpdfs/s5.pdf','answersheetpdfs/s6.pdf','answersheetpdfs/s7.pdf']
pdf_files2 = [if x in pdf_files: r]
extract_answers_from_pdfs(pdf_files2)
input_file = 'ANSWERS/ANSWERS1.txt'
ranges = [(1, 33), (34, 48), (49, 65), (66, 109), (110, 139)]
ranges2 = [(1, 33), (95, 109), (34,50), (51, 94), (110, 139)]
output_CSV_1 = ['READING1&2/Reading1P1.csv', 'NOCALC/NoCalc1.csv','READING1&2/Reading1P2.csv','WRITING/Writing1.csv','CALC/Calc1.csv']
output_CSV_2 = ['READING1&2/Reading2P1.csv', 'NOCALC/NoCalc2.csv','READING1&2/Reading2P2.csv','WRITING/Writing2.csv','CALC/Calc2.csv']
output_CSV_3 = ['READING1&2/Reading3P1.csv', 'NOCALC/NoCalc3.csv','READING1&2/Reading3P2.csv','WRITING/Writing3.csv','CALC/Calc3.csv']
output_CSV_4 = ['READING1&2/Reading4P1.csv', 'NOCALC/NoCalc4.csv','READING1&2/Reading4P2.csv','WRITING/Writing4.csv','CALC/Calc4.csv']
output_CSV_5 = ['READING1&2/Reading5P1.csv', 'NOCALC/NoCalc5.csv','READING1&2/Reading5P2.csv','WRITING/Writing5.csv','CALC/Calc5.csv']
output_CSV_6 = ['READING1&2/Reading6P1.csv', 'NOCALC/NoCalc6.csv','READING1&2/Reading6P2.csv','WRITING/Writing6.csv','CALC/Calc6.csv']
output_CSV_7 = ['READING1&2/Reading7P1.csv', 'NOCALC/NoCalc7.csv','READING1&2/Reading7P2.csv','WRITING/Writing7.csv','CALC/Calc7.csv']

group_answers_to_csv('ANSWERS/ANSWERS1.txt', ranges, output_CSV_1)
group_answers_to_csv('ANSWERS/ANSWERS2.txt', ranges, output_CSV_2)
group_answers_to_csv('ANSWERS/ANSWERS3.txt', ranges, output_CSV_3)
group_answers_to_csv('ANSWERS/ANSWERS4.txt', ranges, output_CSV_4)
group_answers_to_csv('ANSWERS/ANSWERS5.txt', ranges, output_CSV_5)
group_answers_to_csv('ANSWERS/ANSWERS6.txt', ranges, output_CSV_6)
group_answers_to_csv('ANSWERS/ANSWERS7.txt', ranges2, output_CSV_7)


Concat_Reading_Ans("READING1&2/Reading1P1.csv", 'READING1&2/Reading1P2.csv',1)
Concat_Reading_Ans("READING1&2/Reading2P1.csv", 'READING1&2/Reading2P2.csv',2)
Concat_Reading_Ans("READING1&2/Reading3P1.csv", 'READING1&2/Reading3P2.csv',3)
Concat_Reading_Ans("READING1&2/Reading4P1.csv", 'READING1&2/Reading4P2.csv',4)
Concat_Reading_Ans("READING1&2/Reading5P1.csv", 'READING1&2/Reading5P2.csv',5)
Concat_Reading_Ans("READING1&2/Reading6P1.csv", 'READING1&2/Reading6P2.csv',6)
Concat_Reading_Ans("READING1&2/Reading7P1.csv", 'READING1&2/Reading7P2.csv',7)


