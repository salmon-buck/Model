import glob
import os
from openpyxl import load_workbook

input_path = os.getcwd()                                                        # 현재 디렉토리 위치를 불러온다
print('test')
DB_path=os.path.join(input_path, '../Data_Preprocessing/recipeProcess/DB.xlsx')

load_wb=load_workbook(DB_path, data_only=True)

db={}
load_ws=load_wb['DB']


for row in load_ws.rows :
    dic={}
    dic['name'] = row[0].value
    dic['description'] = row[1].value
    dic['country'] = row[2].value
    dic['ingredient'] = row[3].value
    dic['recipe'] = row[4].value
    dic['time'] = row[5].value
    dic['ImageUrl'] = row[6].value
    db[row[0].value] = dic

#    dec_and_ing = dic['description'] + dic['ingredient']

#    total_word = total_word.union(dec_and_ing.split())
    #print(db[row[0].value])

load_ws=load_wb['P(t|C)']
collection_prob={}
for row in load_ws.rows :
    collection_prob[row[0].value]=row[1].value

load_ws=load_wb['Smoothing']
smoothing_prob={}
for row in load_ws.rows :
    if row[0].value :
        name=row[0].value
        food={}
        smoothing_prob[name]=food
    if row[1].value:
        food[row[1].value] = row[2].value

for i in smoothing_prob.keys() :
    print(len(smoothing_prob[i]))
print(smoothing_prob)
'''
for input_file in glob.glob(os.path.join(input_path, '../Data_Preprocessing/processedRecipe/*.txt')):                 # path 지정한 곳에서 txt파일 모두뒤짐
    a=os.path.basename(input_file)

    if a==' Asian Quinoa salad .txt':
        with open(input_file, 'r') as doc:
            print("성공")
            list=doc.readlines()
            print(list)

print(db)
'''