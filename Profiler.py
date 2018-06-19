#!/usr/bin/env python3
import csv, sys, re, os, argparse
# GLOBALS # They suck, but its a small program so whatever
columns = []
global row_count
###########
from ColumnClass import *
from htmlHelpers import *


# Stuff for plotting #
import matplotlib 
matplotlib.use('Agg') # so that you can save images out
import matplotlib.pyplot as plt
import matplotlib as mpl
######################

#### Improvements ####
# - Calculate missing/empty/blank and NULL/null fields
# - Would like to be able to sample a certain % of the file (helpful for large files)
# - Look out for fixed width 



def Initialize(filename, newline='\n', delimiter=',', quotechar='"', has_header=True):   
    with open(filename, 'r', newline=newline) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        global row_count
        row_count = sum(1 for row in csvreader) # May take a while for long files?
        if has_header == True: row_count -= 1
        #ROW_CT = row_count
        print("Row Count {}".format(row_count))


def Profiler(filename, newline='\n', delimiter=',', quotechar='"', has_header=True):    
    Initialize(filename, newline, delimiter, quotechar)
    # Read CSV
    with open(filename, 'r', newline=newline) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)

        for i, row in enumerate(csvreader):
            # Get the number of headers and initialize the column objects for each
            if (i == 0 and has_header == True):
                num_headers = len(row)
                for position, header in enumerate(row):
                    column = Column(header, position)
                    columns.append(column)
            # Start creating the stats for each column

            else:
                for j, datum in enumerate(row):
                    # Make sure calculations are done float
                    
                    # Figure out what data type this datum/cell is
                    DetermineDataType(j, datum)
            ProgressBar(i+1, row_count, status='{}/{}'.format(i+1, row_count))
            
    # for i, col in enumerate(columns):
    #     print(i)
    #     print("OVERALL LEN {}".format(col.overallavg_length))
    #     print("INTCT {}".format(col.int_count))
    #     print("INTLEN {}".format(col.int_avglength))
        
    #     print("STRCT {}".format(col.string_count))
    #     print("STRLEN {}".format(col.string_avglength))        
        
        
        


def DetermineDataType(index, datum):
    # if type(mean) !="<class 'float'>": return False
    # Want to figure out length to know fixed width fields but also trim for regex

    #columns[index].overallavg_length = iterative_mean(columns[index].overallavg_length, index, datum)
    if (columns[index].overallavg_length == None):
        columns[index].overallavg_length = len(datum)
    else:
        columns[index].overallavg_length = iterative_mean(columns[index].overallavg_length, index, datum)    

    # Figure out the data types #
    #if (datum.isnumeric()): columns[index].int_count += 1
    
    # Regex Data Types
    # Trim before regex-ing
    datum = datum.strip()
    
    # Going to assume that if it doesn't fall into integer or float it's a string
    if (re.match(r'^\d+$', datum)): 
        columns[index].int_count += 1
        if (columns[index].int_avglength == None):
            columns[index].int_avglength = len(datum)
        else:
            columns[index].int_avglength = iterative_mean(columns[index].int_avglength, index, datum)

        # Max Length        
        if (columns[index].int_maxlength == None):
            columns[index].int_maxlength = len(datum)
        else:
            if len(datum) > columns[index].int_maxlength: columns[index].int_maxlength = len(datum)


    # FLOAT [-+]?[0-9]*\.?[0-9]+
    elif (re.match(r'[-+]?[0-9]*\.?[0-9]+', datum)): 
        columns[index].float_count += 1
        if (columns[index].float_avglength == None):
            columns[index].float_avglength = len(datum)
        else:
            columns[index].float_avglength = iterative_mean(columns[index].float_avglength, index, datum)
            
        # Max Length        
        if (columns[index].float_maxlength == None):
            columns[index].float_maxlength = len(datum)
        else:
            if len(datum) > columns[index].float_maxlength: columns[index].float_maxlength = len(datum)


    # STRING
    else: 
        # Here we will keep track of trimmed strings
        columns[index].string_count += 1
        if (columns[index].string_avglength == None):
            columns[index].string_avglength = len(datum)
        else:
            columns[index].string_avglength = iterative_mean(columns[index].string_avglength, index, datum)

        # Max Length        
        if (columns[index].string_maxlength == None):
            columns[index].string_maxlength = len(datum)
        else:
            if len(datum) > columns[index].string_maxlength: columns[index].string_maxlength = len(datum)
        

def CreateTableStatement():
    CreateSQL = "Create table " + args.TableName + " (\n"
    
    
    for i, column in enumerate(columns):
        CreateSQL += column.header + " " + column.predicted_datatype 
        
        if (column.predicted_datatype == "strings") : CreateSQL += " " + str(column.pd_max_length)
        if (i != len(columns) - 1) : CreateSQL += ", \n"
    CreateSQL += "\n) DISTRIBUTE ON RANDOM;"
    print (CreateSQL);
    

def iterative_mean(mean, num_items, value):
    new_mean = mean + ( float(1/(num_items+1)) * (float(len(str(value))) - mean))
    return new_mean


# output results
    # Progress Bar
    # sys.stdout.write('\r')
    # sys.stdout.write("Alphabet Pages: {}/{}".format(j+1, len(alphabetic_index)))
    # sys.stdout.flush()            
def ProgressBar(count, total, status=''):
    bar_len = 50

    if count == total:
        sys.stdout.write('[%s] %s%s ...%s\n' % ('=' * bar_len, 100, '%', "Processing Complete"))
    else:
        # filled_len = int(round(bar_len * count / float(total)))
        # percents = round(100.0 * count / float(total), 1)
        # bar = '=' * filled_len + '-' * (bar_len - filled_len)
        #sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.write('%s/%s\r' % (count, total))
        sys.stdout.flush()      




# MAIN
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-TableName", help="Add desired table name for create table output.", default="<INSERT TABLENAME>")
    args = parser.parse_args()

    Profiler("./example.csv")
    PageHeader("./test.html")
    OverallReport_Top("./test.html", row_count)

    
    # Calculate the statistics for each column
    print ( "{}      {}    {}                 {}".format("Pos", "DataType", "Counts", "%"))
    for col in columns:
        col.DatatypeConfidence(row_count)
        print ( "{}        {}        {}/{}         {:.2f}%".format(col.col_number, col.predicted_datatype, col.pd_count, row_count, col.pd_confidence*100))
        # print ( "{}   {}    {}".format(col.string_count, col.int_count, col.float_count))
    #OverallReport_Table("./test.html", columns, row_count)

    ColumnReport_Panels("./test.html", columns)
    
    # JS #
    PageJS("./test.html")
    OverallReport_TableJS2("./test.html", columns, row_count)
    PageLoadJS("./test.html")
    ColumnReportsJS("./test.html", columns) # Create the table data and the javascript links to data<->table
    
    # HTML # 
    PageFooter("./test.html")
    CreateTableStatement()
    
    