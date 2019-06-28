import csv
import glob
import os
import argparse
cwd = os.getcwd()

csvfile_path = cwd + "/androidx-class-mapping.csv"
csvfile = open(csvfile_path)
to_include_replacement_patterns = [
 "android.support.annotation",
 "android.support.annotation.RequiresPermission",
 "android.support.design",
 "android.support.v4",
] 
search_string = "**/src/main/java/**/*.java"

"""
1. Looks at the csv file 
2. Looks for the patterns
3. Returns a dictionary of old import and new import
"""
def get_replacements():
    replacements = {} 
    for row in csv.reader(csvfile):
        for pattern in to_include_replacement_patterns:
            if row[0].find(pattern) == 0:        
                replacements[row[0]] = row[1]
    return replacements


"""
1. Looks for all the files that fall into the pattern
2. It searches for the old imports in each of the file and replaces 
   with the new imports 
3. Saves the files after replacing
"""
def search_files(file_path):
    i = 0
    replacements = get_replacements()
    file_names = glob.glob(file_path + search_string,recursive=True)
    for file_name in file_names:
        file_data = open(file_name, 'r').read()
        for k,v in replacements.items():
            if file_data.find(k) != -1:
                i = i + 1
                print(file_name,k,v)
                file_data = file_data.replace(k,v)
                open(file_name, 'w').write(file_data)
                print("== Migrated ",i+1, " files to AndroidX imports ==\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Migrate your React-Native app to use AndroidX')
    parser.add_argument('--node_modules', dest='node_modules_path', help='Node Modules folder location')
    args = parser.parse_args()
    if args.node_modules_path:
        search_files(args.node_modules_path)
    else:
        print("Invalid arguments. Use -h to see help on how to use this script")
