from google.colab import drive
drive.mount('/content/drive')

#next() 헤더 출력하는 함수 

f = open('/content/drive/My Drive/seoul.csv','r', encoding = 'cp949')
data = csv.reader(f)
header = next(data)
max_temp = -999
max_date = ''

for row in data:
  if row[-1] == '':
    row[-1] = -999
  row[-1] = float(row[-1])
  if max_temp < row[-1]:
    max_date = row[0]
    max_temp = row[-1]

f.close()
print('기상 관측상 기온이 가장 높았던 날은',max_date+'로 ',max_temp,'도 였습니다.')

# 생일 기온 변화를 그래프로 그리기

result = []

f = open('/content/drive/My Drive/seoul.csv','r', encoding = 'cp949')
data = csv.reader(f)
next(data)
for row in data:
  if row[-1] != '':
    if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '10':
      result.append(float(row[-1]))

# 그래프 사이즈 조절 plt.figure(figsize = (10,2))
plt.figure(figsize = (8,2), dpi = 100)
plt.plot(result)
plt.show()

f.close()


#히스토그램  - 8월 최고기온 

f = open('/content/drive/My Drive/seoul.csv','r', encoding = 'cp949')
data = csv.reader(f)
next(data)

aug = []

for row in data:
  month = row[0].split('-')[1]
  if row[-1] != '':
    if month == '08':
      aug.append(float(row[-1]))

plt.hist(aug, bins = 100)
plt.show()

f.close()

# 상자 그림 plt.boxplot

plt.boxplot(aug)
plt.show()


