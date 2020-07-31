import os
from aip import AipOcr

range = 169     # number of images you want to convert

# fill in your APP_ID. API_KEY and SECRET_KEY
APP_ID = '00000000'
API_KEY = '00000000'
SECRET_KEY = '00000000'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# Read Images
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

os.chdir('/Users/mingpei/Desktop/OCR/allpics/')
options = {}
options["language_type"] = "CHN_ENG"


output = open('OCRresult.txt','a',encoding='utf-8')

for i in range(range):
    str2 = str(i+1)
    name = 'pic'+str2+'.jpg'
    image = get_file_content(name)
    print(name)

    # ans = client.basicAccurate(image, options);        # accurate OCR
    ans = client.basicGeneral(image, options)    # basic OCR
    
    output.write(name)
    output.write('\n')
    for item in ans['words_result']:
        print(item['words'])
        output.write(item['words'])
        output.write('\n')
    output.write('\n')

print('Output done.')
output.close()