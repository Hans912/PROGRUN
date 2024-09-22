# PROGRUN

## Python code:

### How it works:
You will manuallly input a path to your specific csv file. Then the code I created will go trough each row of this file and append all the rows that are NOT empty into a list. Once this has been done you can go into the list and find any piece of information by writting data[row][column]. I personally chose one of the rows that was full of information and added it into specific varibales, like the athletes name, run time and meet name. I made sure to print all my variables just to check everything worked correctly. Now that you have all the information saved into variables, the code will write those specific variables into the parts of your html you have specified with {} (The html code is saved as a separate varible and has an f infront of the '' so that whatever variable name is inside {} will be filled with said variable). Lastly, the variable with all the html code (now filled with the data from each variable used) will be created into a html file with the name of your choosing (just change the var called output_file) and can be used as normal.


### Warning:
For now the python code is manual and not automated. What this means is that you will have to manually find the path of the csv file you want to use as well as manually write which column and row your variable is in (for example in the code we can see that the first name of the athlete was under row 5 column 0 so I had to write data[5][0]. I do plan to make the code more automated in the future so that it will pass through the entire file row by row and append the right information to the right variable. To do this I will need to clean the data since the biggest problem is that there are some empty columns and some information is in the wrong column.
