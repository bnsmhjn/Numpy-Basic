# import pyoo
# import re
# import argparse
# import os
# import sys
# from string import Template
#
# parser = argparse.ArgumentParser(description="Crosswalk Generator")
# parser.add_argument("-p", "--path", help="Path", type=str)
# parser.add_argument("-t", "--tabNum", help="Tab Number", type=int)
# parser.add_argument("-n", "--rowNum", help="Starting row number", type=int)
# parser.add_argument("-a", "--account", help="Account", type=str)
# parser.add_argument("-c", "--cwName", help="Crosswalk Name", type=str)
#
# args = parser.parse_args()
# path = args.path
# tabNum = args.tabNum
# cwName = args.cwName
# rowNum = args.rowNum
# acc = args.account
#
# CURRENT_DIR = os.getcwd()
# CW_PATH = "/src/main/java/com/deerwalk/das/scrub/account/"
# CW_CSV_PATH = "/src/test/resources/scrub/"
#
#
# def toCamelCaseAfterSpace(ch):
#     temp = []
#     temp = ch.lower().split()
#     result = ""
#     i = 0
#     while i < len(temp):
#         if temp[i] == "_" and temp[i + 1] == "_":
#             continue
#         if i == 0:
#             result = result + temp[i]
#         else:
#             result = result + "_" + temp[i]
#         i = i + 1
#     result = re.sub(r'\W+', '', result)
#     return result
#
#
# def genCwJava(sheet):
#     colCount = 0
#     fields = []
#     startRow = rowNum - 1
#     value = ""
#     variables = ""
#     createTuple = ""
#     crosswalkname = cwName.capitalize()
#
#     while 1 == 1:
#         value = sheet[startRow, colCount].value
#         if not value:
#             value = sheet[startRow - 1, colCount].value
#             if not value:
#                 break
#         fields.append(toCamelCaseAfterSpace(value))
#         colCount = colCount + 1
#
#     package = "com.deerwalk.das.scrub.account." + acc + ".crosswalk;"
#     j = 0
#     for j in range(colCount):
#         variables = variables + '\npublic String ' + fields[j] + ' = "";'
#
#     j = 0
#     for j in range(colCount):
#         createTuple = createTuple + (str(fields[j]) + " = columns[" + str(j) + "].trim();")
#
#     file = open(CURRENT_DIR + "/cwTemplate.txt")
#     src = Template(file.read())
#     sub = {'package': package, 'cName': crosswalkname, 'variables': variables, 'values': createTuple}
#     result = src.substitute(sub)
#     fileName = CURRENT_DIR + CW_PATH + acc + "/crosswalk/" + crosswalkname + ".java"
#     f = open(fileName, "a")
#     f.write(result)
#     f.close()
#
#
# def genCSVfile(sheet):
#     crosswalkname = cwName.lower()
#     colCount = 0
#     rowCount = rowNum - 1
#
#     startRow = rowNum - 1
#     while 1 == 1:
#         value = sheet[startRow, colCount].value
#         if not value:
#             value = sheet[startRow - 1, colCount].value
#             if not value:
#                 break
#         colCount = colCount + 1
#
#     value = ""
#     while 1 == 1:
#         val = sheet[rowCount, 0].value
#         if not val:
#             if rowCount == startRow:
#                 val = sheet[startRow - 1, 0].value
#                 if not val:
#                     break
#             else:
#                 a = 0
#                 count = 0
#                 while a < colCount:
#                     val = sheet[rowCount, a].value
#                     if val:
#                         count = 1
#                     a = a + 1
#                 if count == 0:
#                     break
#         rowCount = rowCount + 1
#
#     rowCount = rowCount - rowNum + 1
#
#     j = rowNum - 1
#     fileName = CURRENT_DIR + CW_CSV_PATH + acc + "/rules/" + crosswalkname + ".csv"
#
#     f = open(fileName, "a")
#
#     while j < rowCount + rowNum - 1:
#         k = 0
#         if j == startRow:
#             f.write("#")
#             while k < colCount:
#                 value = sheet[j, k].value
#                 if not value:
#                     value = sheet[j - 1, k].value
#                 if k == colCount - 1:
#                     f.write(str(value))
#                 else:
#                     f.write(str(value) + ';')
#                 k = k + 1
#         else:
#             while k < colCount:
#                 value = sheet[j, k].value
#                 if k == colCount - 1:
#                     f.write(str(value))
#                 else:
#                     f.write(str(value) + ';')
#                 k = k + 1
#
#         j = j + 1
#         f.write('\n')
#     f.close()
#
#
# def main():
#     try:
#         desktop = pyoo.Desktop('localhost', 2002)
#         doc = desktop.open_spreadsheet(path)
#         sheet = doc.sheets[tabNum - 1]
#     except:
#         print ("File not found")
#         sys.exit(1)
#
#     genCwJava(sheet)
#     genCSVfile(sheet)
#
#
# if __name__ == '__main__':
#     main()
