import requests

url = input("请输入源链:")
jpglist = input("请输入页数:")
jpglist = int(jpglist)

n=1
for each in range(jpglist):
    print('第'+str(n)+'页抓取中')
    pic = url+str(n)+'.jpg'
    #print(pic)
    try:
        response = requests.get(pic)
    except:
        print('第'+str(n)+'页抓取失败！')
        continue
    img = response.content
    with open( './output/'+str(n)+'.jpg','wb' ) as f:
        f.write(img)
    n+=1

print('抓取完毕')