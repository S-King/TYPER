# Functions to build the HTML output page
import os # For gettting the file size and stats

# Clears out any old file and writes the initial/top part of the page
def PageHeader(filename):
    with open(filename, "w") as html:
        heading =   '<!doctype html>\n' \
                    '<html lang="en">\n' \
                    '  <head>\n' \
                    '    <!-- Required meta tags -->\n' \
                    '    <meta charset="utf-8">\n' \
                    '    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n' \
                    '\n' \
                    '    <!-- Bootstrap CSS -->\n' \
                    '    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">\n' \
                    '    <link rel="stylesheet" type="text/css"  href="https://rawgit.com/wenzhixin/bootstrap-table/master/src/bootstrap-table.css">\n' \
                    '\n' \
                    '    <title>Spencer\'s CSV Profiler</title>\n' \
                    '\n' \
                    '<style>\n' \
                    '  /* CSS for profiler report */\n' \
                    '\n' \
                    '  .pageTitle {\n' \
                    '      text-align: center;\n' \
                    '  }\n' \
                    '\n' \
                    '  .top_panel {\n' \
                    '      border-bottom-left-radius: 0px !important;\n' \
                    '      border-bottom-right-radius: 0px !important;\n' \
                    '      /*background-color:red;*/\n' \
                    '  }\n' \
                    '\n' \
                    '  .middle_panel {\n' \
                    '      border-radius: 0px 0px 0px 0px !important;\n' \
                    '      /*background-color:blue;*/\n' \
                    '  }\n' \
                    '\n' \
                    '  .bottom_panel {\n' \
                    '      border-top-left-radius: 0px !important;\n' \
                    '      border-top-right-radius: 0px !important;\n' \
                    '      /*background-color:purple;*/\n' \
                    '  }\n' \
                    '  .row-index { \n ' \
                    '    width: 50px; \n ' \
                    '    display: inline-block; \n ' \
                    '} \n ' \
                    '</style>\n' \
                    '  </head>\n' \
                    '  <body>\n' \
                    '<div class="pageTitle">\n' \
                    '<h1 style="padding-top:15px">CSV Profiler</h1>    \n' \
                    '</div>   <!-- End Header / CSS Declarations -->  \n' 
        html.write(heading)


def OverallReport_Top(filename, row_ct):
    with open(filename, "a") as html:    
        file_size = os.path.getsize("./example.csv")
        OverallReport = '<div class="container" style="padding-bottom:50px"> \n ' \
                        '<div id="accordion" role="tablist"> \n ' \
                        '  <div class="card panel top_panel"> \n ' \
                        '    <div id="panel-overall-head" class="card-header" role="tab" data-parent="#accordion" href="#panel-overall-data">Overall Report</div> \n ' \
                        '    <div id="panel-overall-data" class="card-block panel-collapse" role="tabpanel"> \n ' \
                        '<div class="Overall_Top"> \n ' \
                        '    <div class="row"> \n ' \
                        '    <div class="col-6 pt-2" style="height:100px;"> \n ' \
                        '        <div class="col-12"> \n ' \
                        '            Filename : <b>' + filename + '</b> \n ' \
                        '        </div> \n ' \
                        '        <div class="col-12"> \n ' \
                        '            Size : <b>' + str(file_size) + '</b> \n ' \
                        '        </div> \n ' \
                        '        <div class="col-12"> \n ' \
                        '            Type : <b>CSV</b> \n ' \
                        '        </div> \n ' \
                        '        <div class="col-12"> \n ' \
                        '            Number of Lines : <b>' + str(row_ct) + '</b> \n ' \
                        '        </div> \n ' \
                        '    </div> \n ' \
                        '     \n ' \
                        '    <div class="col-6 pt-2" style="height:100px;"> \n ' \
                        '        <div class="col-12"> \n ' \
                        '            Parameters : <br> \n ' \
                        '            has_header = True, <br> \n ' \
                        '            Delimiter = ",", <br> \n ' \
                        '            Quotes = "Minimal" \n ' \
                        '        </div> \n ' \
                        '    </div> \n ' \
                        '    </div> \n ' \
                        '</div> \n ' \
                        '         \n ' \
                        '    <table id="tableOverall" data-search="true" data-show-columns="true" data-pagination="true" data-height="500"> \n ' \
                        '        <thead> \n ' \
                        '            <tr> \n ' \
                        '                <th data-field="#" data-sortable="true">#</th> \n ' \
                        '                <th data-field="Name" data-sortable="true" width="200">Name</th> \n ' \
                        '                <th data-field="DataType" data-sortable="true">Type</th> \n ' \
                        '                <th data-field="Count" data-sortable="true">Count</th> \n ' \
                        '                <th data-field="Confidence" data-sortable="true">Confidence</th> \n ' \
                        '            </tr> \n ' \
                        '        </thead> \n ' \
                        '    </table>        \n ' \
                        '    </div> \n ' \
                        '  </div> \n '        
        
        
        
        # overallReport = '\n\n<div class="container">\n' \
        #                 '\n' \
        #                 '<div id="accordion" role="tablist">\n' \
        #                 '  <div class="card panel top_panel">\n' \
        #                 '    <div id="panel-1-head" class="card-header" role="tab" data-parent="#accordion" href="#panel-1-data">Overall Report</div>\n' \
        #                 '    <div id="panel-1-data" class="card-block panel-collapse" role="tabpanel">OVERALL REPORT DATA</div>\n' \
        #                 '  </div>\n' \
        #                 '\n' 
        html.write(OverallReport)    
    
    
   
def ColumnReport_Panels(filename, Columns):
    with open(filename, "a") as html:
        for i, Column in enumerate(Columns):
            PanelText = '  <div id="report_panel_' + str(i) + '" class="card panel middle_panel">  \n' \
                        '    <div id="panel-' + str(i) + '-head" class="card-header middle_panel" role="tab" data-toggle="collapse" data-parent="#accordion" href="#panel-' + str(i) + '-data">' + '{} - {}'.format(i, Column.header) + '</div>  \n' \
                        '    <div id="panel-' + str(i) + '-data" class="card-block panel-collapse collapse in middle_panel" role="tabpanel">  \n' \
                        '    <table id="table_report_' + str(i) + '" data-search="false" data-show-columns="false" data-pagination="false" data-height="auto">  \n' \
                        '        <thead>  \n' \
                        '            <tr>  \n' \
                        '                <th data-field="type" data-sortable="true">Type</th>  \n' \
                        '                <th data-field="count" data-sortable="true" width="200">Count</th>  \n' \
                        '                <th data-field="avglength" data-sortable="true">Avg. Length</th>  \n' \
                        '                <th data-field="maxlength" data-sortable="true">Max Length</th>  \n' \
                        '            </tr>  \n' \
                        '        </thead>  \n' \
                        '    </table>          \n' \
                        '    </div>  \n' \
                        '  </div>  \n' 
            html.write(PanelText) 
        
        # Close out the accordion and container divs from top
        PanelText = '\n    </div> <!-- End Accordion -->\n' \
                    '\n</div> <!-- End Container -->\n\n'
        html.write(PanelText) 
    
# def Deprecated_ColumnPanel(filename):
#     with open(filename, "a") as html:
#         panel = '\n  <div class="card panel middle_panel">\n' \
#                 '    <div id="panel-2-head" class="card-header middle_panel" role="tab" data-toggle="collapse" data-parent="#accordion" href="#panel-2-data">Column 2</div>\n' \
#                 '    <div id="panel-2-data" class="card-block panel-collapse collapse in middle_panel" role="tabpanel">Column 2 Data</div>\n' \
#                 '  </div>\n' \
#                 '\n' \
#                 '  <div class="card panel bottom_panel">\n' \
#                 '    <div id="panel-3-head" class="card-header bottom_panel" role="tab" data-toggle="collapse" data-parent="#accordion" href="#panel-3-data">Column 3</div>\n' \
#                 '    <div id="panel-3-data" class="card-block panel-collapse collapse in" role="tabpanel">Column 3 Data</div>\n' \
#                 '  </div>\n' \
#                 '\n' \
#                 '\n' \
#                 '</div>\n' \
#                 '</div>\n' \
#                 '\n'
#         html.write(panel) 




def PageJS(filename):
    with open(filename, "a") as html:
        footer =    '\n    <!-- Begin Footer / Optional JavaScript -->\n' \
                    '    <!-- jQuery first, then Popper.js, then Bootstrap JS -->\n' \
                    '    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>\n' \
                    '    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>\n' \
                    '    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>\n' \
                    '    <script src="https://rawgit.com/wenzhixin/bootstrap-table/master/src/bootstrap-table.js"></script>\n\n'
        html.write(footer)        



import json
def OverallReport_Table(filename, Columns, row_count):
    with open(filename, "a") as html:
        data = 'var OverallData = [ '

        for i, Col in enumerate(Columns):
            print (Col.header)
            data += '\n{ "#": "' + str(Col.col_number) + '", \n' \
                    '"Name": "' + Col.header + '", \n' \
                    '"DataType": "' + Col.predicted_datatype + '", \n' \
                    '"Count": "' + str(Col.pd_count) + '", \n' \
                    '"Confidence": "{:.2f}%'.format(Col.pd_confidence*100) + '" \n }'
            if ( i != len(Columns) - 1):
                data += ", "
        data += "\n ];"
        # print(data)



# The code is cleaner in this one but the other one prints nicely
def OverallReport_TableJS2(filename, Columns, row_count):
    with open(filename, "a") as html:
        html.write("\n<script>\n")
        
        OverallData_JSON = ''
        for i, Col in enumerate(Columns):
            OverallData = { "#" : str(Col.col_number),
                            "Name" : Col.header, 
                            "DataType" : Col.predicted_datatype,
                            "Count" : str(Col.pd_count),
                            "Confidence" : '{:.2f}%'.format(Col.pd_confidence*100)
                            }
            OverallData_JSON += json.dumps(OverallData)
            if ( i != len(Columns) - 1):
                OverallData_JSON += ", "
        OverallData_JSON = "var OverallData = [" + OverallData_JSON + "] ;"
        # print(OverallData_JSON)
        html.write(OverallData_JSON)

        # Add OverallReport JS data link
        OverllReportLink =   "\n        $('#tableOverall').bootstrapTable({ \n " \
                             "         data : OverallData \n " \
                             "        }); \n "            
                            
        html.write(OverllReportLink)
        html.write("\n</script>\n")



# def ColumnSpecificReports(filename, Columns):
#     with open(filename, "a") as html:
        
#         # Write the data for all the data tabs
#         ColumnReportData_JSON = ''
#         ColumnReport_JS = ''
#         for i, Column in enumerate(Columns):
#             ColumnReportData = {    "string_count" : str(Column.string_count),
#                                     "string_avglength" : str(Column.string_avglength), 
#                                     "string_maxlength" : str(Column.string_maxlength),
#                                     "predicted_datatype" : str(Column.predicted_datatype),
#                                     "pd_count" : str(Column.pd_count),
#                                     "pd_confidence" : '{:.2f}%'.format(Column.pd_confidence*100)
#                                     }
#             # ColumnReportData_JSON += json.dumps(ColumnReportData)
#             # ColumnReportData_JSON += "var report_" + Column.header + " = [" + ColumnReportData_JSON + "] ;\n"
#             ColumnReportData_JSON += "var report_" + str(Column.col_number) + " = [" + json.dumps(ColumnReportData) + "];\n"
            
#             # Write the javascript to hook up the data to the tables
#             ColumnReport_JS += "\n\t$('#table_report_" + str(i) + "').bootstrapTable({\n" \
#                               "\t data : report_" + str(Column.col_number) + "\n\t});\n" 
#         ColumnReport_JS = "$(function () {\n" + ColumnReport_JS + "});\n"

#         print(ColumnReportData_JSON)
#         print(ColumnReport_JS)


def PageLoadJS(filename):
    with open(filename, "a") as html:
        html.write("\n<script>\n")        
        DocReadyJS = '\n$(document).ready(function() { \n ' \
                     '    // Set the search bar up (kinda) in the middle, above the table \n ' \
                     '    $(".float-right.search").width("85%"); \n ' \
                     '    $(".columns.columns-right.btn-group.float-right").width("12%"); \n ' \
                     '    $(".keep-open.btn-group").width("100px"); \n ' \
                     '}); \n\n'   
        html.write(DocReadyJS)     
        html.write("\n</script>\n")      





def ColumnReportsJS(filename, Columns):
    with open(filename, "a") as html:
        html.write("\n<script>\n")        
        
        # Write the data for all the data tabs
        ColumnReportData_JSON = ''
        ColumnReport_JS = ''
        Datatypes = ["string", "int", "float"]
        for i, Column in enumerate(Columns):
            ColumnReportData = None
            Column_JSON = ''
            for j, dt in enumerate(Datatypes):
                ColumnReportData = {    "type" : dt,
                                        "count" : eval("str(Column." + dt + "_count)"),
                                        "avglength" : eval("str(Column." + dt + "_avglength)"),
                                        "maxlength" : eval("str(Column." + dt + "_maxlength)")
                                        
                                    }
                                
                Column_JSON += json.dumps(ColumnReportData)
                if ( j != len(Datatypes) - 1):
                    Column_JSON += ", "

            ColumnReportData_JSON += "var report_" + str(Column.col_number) + " = [" + Column_JSON + "];\n"
            
            # Write the javascript to hook up the data to the tables
            ColumnReport_JS += "\n\t$('#table_report_" + str(i) + "').bootstrapTable({\n" \
                               "\t data : report_" + str(Column.col_number) + "\n\t});\n" 
        ColumnReport_JS = "$(function () {\n" + ColumnReport_JS + "});\n"

        # print(ColumnReportData_JSON)
        # print(ColumnReport_JS)
        
        html.write(ColumnReportData_JSON)
        html.write(ColumnReport_JS)
        html.write("\n</script>\n")
        
        


        
        
def PageFooter(filename):
    with open(filename, "a") as html:
        footer =    '\n  </body>\n' \
                    '</html>\n'
        html.write(footer)        
                