# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 13:41:47 2022

@author: dganguli
This script will copy SRR*.fastq files from directory 00_SRA_fastq and paste in the new directory 01_raw_reads_fastq 
and subsequently rename the files with custom names. 
"""

import os
import shutil

source_directory_path = r'/home/deep/Analysis/practice_script/snakemake_copy_move_rename_script/00_SRA_fastq'
destination_directory_path = r'/home/deep/Analysis/practice_script/snakemake_copy_move_rename_script/01_raw_reads_fastq'

# This will list all the files present in the source folder into the variable.
source_files = os.listdir(source_directory_path) 

# This will print files names of all the files present in the source directory.
print("\nThe source directory contains:\n", source_files, '\n')

# This will print full file path & names of all the files present in the source directory.
print('The full file_path_name is as under:\n')

# This for looop will go through the list of files present in the source folder. 
for file_name in source_files:
    
    # This will ensure that only files with specific extension will be selected for copying.
    if file_name.endswith('fastq'):
        
        # This step will join the path and file name and save it temporarily in a variable for further usage.
        full_file_name = os.path.join(source_directory_path, file_name)
        
        print(full_file_name)
        
        # copying and saving specific files into another directory.
        shutil.copy2(full_file_name, destination_directory_path)

print("\nThe destination directory contains:\n", os.listdir(destination_directory_path), '\n')

"""
These two lists will be subsequently used for renaming step. Order of the elements in the two list 
is critical as this will determine which old and it's corresponding new file name.  
"""

old_file_name = ['SRR11580509_1.fastq', 'SRR11580509_2.fastq', 'SRR11580503_1.fastq', 'SRR11580503_2.fastq']
print('The old_file_name list contains\n', old_file_name, '\n')


new_file_name = ["2021HRS_PECseq_iPSC_Input_Rep1_R1.fastq", "2021HRS_PECseq_iPSC_Input_Rep1_R2.fastq", "2021HRS_PECseq_iPSc_BRN2IP_Rep1_R1.fastq", "2021HRS_PECseq_iPSc_BRN2IP_Rep1_R2.fastq"]
print('The new_file_name list contains\n', new_file_name, '\n')
print('number of elements in new_file_name list = ', len(new_file_name), '\n')


current_working_directory_path = r'/home/deep/Analysis/practice_script/snakemake_copy_move_rename_script/01_raw_reads_fastq'
print('The destination directory path is as under:\n', destination_directory_path)

# This will ensure that python script works within the desired current working directory.
os.chdir(r'/home/deep/Analysis/practice_script/snakemake_copy_move_rename_script/01_raw_reads_fastq')

print('\nThe current working directory is as under:\n', os.getcwd(), '\n')

print("The following shows which copied old files were selected, correct order of re-naming and it's corresponding desired new customised name.\n")

# This step will help iterate through the current directory to select copied files with old names. 
for old_file in os.listdir():
    print(old_file)

    # index to iterate through the new name list.
    i = 0

    while i < len(new_file_name):
        print('new_file_name List element index i =', i)
        
        if old_file == old_file_name[i]: # The next 3 steps will ensure that each copied file with old name gets it's corresponding new name.
            print(old_file, old_file_name[i], new_file_name[i], '\n')
            os.rename(old_file, new_file_name[i]) # renaming step
            break

        else:
            i = i+1

print('\nThe current working directory contains re-named files as under:\n')
print(os.listdir(r'/home/deep/Analysis/practice_script/snakemake_copy_move_rename_script/01_raw_reads_fastq'))
