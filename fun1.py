import codecs,re,urllib
import urllib.request


txtpath = 'C:/Users/24608/Desktop/python/image/test/qqfriends.txt'  #你从QQ邮箱中粘贴的文件
savepath = 'C:/Users/24608/Desktop//python/image/touxiang/'  #头像存储位置

resultSavePath = 'C:/Users/24608/Desktop//python/image/result2.png'   #结果存储位置
modePath = 'C:/Users/24608/Desktop//python/image/leno.jpg'    #模板存储位置

friends_count = 0   #好友数量
all_mean_rgbs = []   #存储计算出的所有平均rgb值

def gettouxiang(txtpath):#输入你的txt文件存储位置
	file = codecs.open(txtpath,'rb','utf-8')
	s = file.read()
	pattern = re.compile(r'\d+@qq.com')
	all_mail = pattern.findall(s)  #正则表达式匹配所有的qq号
	all_link = []  #用于存储需要访问的链接
	url = 'http://qlogo.store.qq.com/qzone/'
	for mail in all_mail:
		qq = mail.replace('@qq.com','')
		l = url + qq +'/'+qq+'/100'
		all_link.append(l)
	i = 1
	for link in all_link:   #遍历链接，下载头像
		saveurl = savepath+str(i)+'.png'
		savaImg(link,saveurl)
		#print('当前QQ：' +str(i)+'是'+ link)
		print('已下载',i)
		i +=1
	friends_count = len(all_link) #获取朋友头像数量
	return True

def savaImg(picurl,saveurl):  #存储图片函数，picurl是图片的URL，saveurl是本地存储位置
	try:
		
		bytes = urllib.request.urlopen(picurl)
		file = open(saveurl,'wb')
		file.write(bytes.read())
		file.flush()
		file.close()
		return True
	except:
		print('worry')
		savaImg(picurl,saveurl)



gettouxiang(txtpath)   #获取头像，如果已经获取就可以给注释掉了