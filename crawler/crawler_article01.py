# -*- coding: UTF-8 -*-
# #from urllib3.response import urlopen
import urllib.request
#单文章链接
str0 = '<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102egl0.html">地震思考录</a>'
#从链接找到提取的地址，链接起来
title = str0.find(r'<a title=')
print(title)
href = str0.find(r'href=')
print(href)
html = str0.find(r'.html')
print(html)
#拼接地址
url = str0[href+6:html+5]
print(url)
#将爬取的地址读取到content变量
content = urllib.request.urlopen(url).read().decode("utf-8")
print(content)
print(type(content),"--")

filename = url[-26:]
print(filename)
open(filename,'w').write(str(content))


[
['肖申克的救赎', 'https://movie.douban.com/subject/1292052/', 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg', '9.7', '希望让人自由。'],
['霸王别姬', 'https://movie.douban.com/subject/1291546/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2561716440.jpg', '9.6', '风华绝代。'],
['阿甘正传', 'https://movie.douban.com/subject/1292720/', 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2372307693.jpg', '9.5', '一部美国近现代史。'],
['这个杀手不太冷', 'https://movie.douban.com/subject/1295644/', 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p511118051.jpg', '9.4', '怪蜀黍和小萝莉不得不说的故事。'],
['泰坦尼克号', 'https://movie.douban.com/subject/1292722/', 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p457760035.jpg', '9.4', '失去的才是永恒的。 '],
['美丽人生', 'https://movie.douban.com/subject/1292063/', 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2578474613.jpg', '9.6', '最美的谎言。'],
['千与千寻', 'https://movie.douban.com/subject/1291561/', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2557573348.jpg', '9.4', '最好的宫崎骏，最好的久石让。 '],
['辛德勒的名单', 'https://movie.douban.com/subject/1295124/', 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p492406163.jpg', '9.5', '拯救一个人，就是拯救整个世界。'],
['盗梦空间', 'https://movie.douban.com/subject/3541415/', 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2616355133.jpg', '9.3', '诺兰给了我们一场无法盗取的梦。'],
['忠犬八公的故事', 'https://movie.douban.com/subject/3011091/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2587099240.jpg', '9.4', '永远都不能忘记你所爱的人。'],
['星际穿越', 'https://movie.douban.com/subject/1889243/', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2614988097.jpg', '9.3', '爱是一种力量，让我们超越时空感知它的存在。'],
['楚门的世界', 'https://movie.douban.com/subject/1292064/', 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p479682972.jpg', '9.3', '如果再也不能见到你，祝你早安，午安，晚安。'],
['海上钢琴师', 'https://movie.douban.com/subject/1292001/', 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2574551676.jpg', '9.3', '每个人都要走一条自己坚定了的路，就算是粉身碎骨。 '],
['三傻大闹宝莱坞', 'https://movie.douban.com/subject/3793023/', 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p579729551.jpg', '9.2', '英俊版憨豆，高情商版谢耳朵。'],
['机器人总动员', 'https://movie.douban.com/subject/2131459/', 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p1461851991.jpg', '9.3', '小瓦力，大人生。'],
['放牛班的春天', 'https://movie.douban.com/subject/1291549/', 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p1910824951.jpg', '9.3', '天籁一般的童声，是最接近上帝的存在。 '],
['无间道', 'https://movie.douban.com/subject/1307914/', 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2564556863.jpg', '9.3', '香港电影史上永不过时的杰作。'],
['疯狂动物城', 'https://movie.douban.com/subject/25662329/', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2614500649.jpg', '9.2', '迪士尼给我们营造的乌托邦就是这样，永远善良勇敢，永远出乎意料。'],
['大话西游之大圣娶亲', 'https://movie.douban.com/subject/1292213/', 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2455050536.jpg', '9.2', '一生所爱。'],
['熔炉', 'https://movie.douban.com/subject/5912992/', 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1363250216.jpg', '9.3', '我们一路奋战不是为了改变世界，而是为了不让世界改变我们。'],
['教父', 'https://movie.douban.com/subject/1291841/', 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p616779645.jpg', '9.3', '千万不要记恨你的对手，这样会让你失去理智。'],
['当幸福来敲门', 'https://movie.douban.com/subject/1849031/', 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2614359276.jpg', '9.1', '平民励志片。 '],
['龙猫', 'https://movie.douban.com/subject/1291560/', 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2540924496.jpg', '9.2', '人人心中都有个龙猫，童年就永远不会消失。'],
['怦然心动', 'https://movie.douban.com/subject/3319755/', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p501177648.jpg', '9.1', '真正的幸福是来自内心深处。'],
['控方证人', 'https://movie.douban.com/subject/1296141/', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1505392928.jpg', '9.6', '比利·怀德满分作品。']
]
