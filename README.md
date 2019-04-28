This repo is a submission to the Insight Data Engineering Coding Challenge. Here is the link to the challenge description and instructions: [https://github.com/InsightDataScience/pharmacy_counting](https://github.com/InsightDataScience/pharmacy_counting)

# Intro
I use python3 in my submission. My script aggregates unique prescribers and total costs per drug separately in a dict of sets and a simple dict of integers respectively. The length of the sets of unique prescribers is taken, and the aggregatted information is written to a text file line by line. I wrote this script in only a few hours; as a result it is a work in progress.


# Key Notes
Here are important notes about my code:
* My run.sh file expects EITHER (a) one argument passed to the python script. That argument must either be an absolute path to the input data or a relative path to the input data file from the challenge root directory where run.sh is executed. Or (b) no argument following the script path/name. In this case the script chooses the first .txt file in the ./input folder and runs on that.
*  I didn't use the csv parsing module integrated into python because I wasn't sure if it was accepted under the rules. The module would have made my code faster and much simpler because it would have automatically dealt with the problem of commas (and \n's and other special symbols for that matter) inside of data cells. I did use the re module to parse quoted data cells containing commas to get around the absence of the csv module.
* I use defaultdict from collections module to make life ever so slightly easier
* I included some potential warning messages to stderr that highlight possible failures of the script without aborting the program entirely.
* I know my script has a bug where is fails to parse/read in rows with empty cells. I unfortunately do not have time to fix this problem.


# Assumptions
Here are some key assumptions made by my code. I assume that:
1. there are no \n's within data cells in this data
2. the test data will have same number, names, and order of columns
3. there is a header row
4. the script is run from with the current directory set to the root of challenge directory structure
5. any data cells containing commas are quoted using the quote char ""




