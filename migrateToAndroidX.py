import csv
import glob
import os
cwd = os.getcwd()

csvfile_path = cwd + "/androidx-class-mapping.csv"
csvfile = open(csvfile_path)
to_include_replacement_patterns = [
 "android.support.annotation",
 "android.support.annotation.RequiresPermission",
 "android.support.design",
 "android.support.v4",
] 
search_string = cwd + "/node_modules/**/src/main/java/**/*.java"
def get_replacements():
    replacements = {} 
    for row in csv.reader(csvfile):
        for pattern in to_include_replacement_patterns:
            if row[0].find(pattern) == 0:        
                replacements[row[0]] = row[1]
    return replacements


if __name__ == '__main__':
    i = 0
    replacements = get_replacements()
    file_names = glob.glob(search_string,recursive=True)
    for file_name in file_names:
        file_data = open(file_name, 'r').read()
        for k,v in replacements.items():
            if file_data.find(k) != -1:
                i = i + 1
                print(file_name,k,v)
                file_data = file_data.replace(k,v)
                open(file_name, 'w').write(file_data)
                print("=======",i+1)

           
            
