import pandas as pd


def prepareXML(DataFrame_,AttributeName_,Root_ = False,Tag_ = False ,OutFile_ = False):

    # INITIALIZE THE XML VARIABLE
    xml = ""

    # START ROOT TAG
    if Root_:
        xml += "<"+Root_+">\n"

    # START SEPARATOR TAG
    if Tag_:
        xml += "<"+Tag_+">\n"

    # ITERATE FOR EACH ROW
    for indexNumber,row in DataFrame_.iterrows():

        # SET TAG START
        xml +="\t <"+AttributeName_ + " "

        # ITERATE FOR EACH COLUMN VALUE
        for column in DataFrame_.columns.tolist():

            # REMOVE EMPTY SETS
            if str(row[column]) == 'nan':
                row[column] = "null"


            # SET EACH COLUMN = "VALUE" FORMAT
            xml += '{0}="{1}" '.format(column, row[column])

        # CLOSE CURRENT LINE TAG
        xml += "/>\n"


    # END SEPARATOR TAG
    if Tag_:
        xml += "</"+Tag_+">\n"

    # END ROOT TAG
    if Root_:
        xml += "</"+Root_+">\n"

    # WRITE TO OUTPUT FILE
    if OutFile_:
        output_text_file = open(OutFile_, "a")
        output_text_file.write(xml)
        output_text_file.close()

    return xml

dataset = pd.read_csv('TableStructure.csv')

my_xml = prepareXML(DataFrame_ = dataset,AttributeName_ = 'TableStructure',  Root_ = 'Root', Tag_ = 'Table1')

print(my_xml)
