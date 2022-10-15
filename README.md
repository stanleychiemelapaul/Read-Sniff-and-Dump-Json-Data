# Read-Sniff-and-Dump-Json-Data
A Program that Reads a JSON file, Sniffs the schema of the JSON file and Dumps it in another file

## How to Run the Program

**Install Python3, Initialize and activate a virtualenv**
```
python3 -m virtualenv env
source env/bin/activate
```
>**Please note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source env/Scripts/activate
```

>**Info** - You may want to change the json file to be read and where it is dumped. Kindly locate the call of this function on line 19 in main.py:
```
openandwiteFile(Json_File_to_Read, Json_file_to_dump_into)
```
>**Json_File_to_Read** - Json file that you want to read 

>**Json_file_to_dump_into** - Json file that you want the  file to be dumped into. Don't worry if this file does not exist at this time, the program will create and dump the file into it


**Run the Program:**
```
python3 main.py
```

