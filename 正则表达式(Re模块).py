# 正则表达式的常用操作符
'''
操作符          说明                                实例
================================================================================================
.               表示任何单字符             
[]              字符集，对单个字符给出取值范围        [abc]表示a、 b、 c, [a-z]表示 a 到 z 单字符
[^]             非字符集，对单个字符给出排除范围      [^abc]表示 非a或b或c的单个字符
*               前一个字符0次或无限次扩展             abc* 表示ab、 abc  abcc  abccc等
+               前一个字符的1次或无限次扩展           abc+ 表示abc  abcc  abccc  等
？              前一个字符0次或1次扩展                abc? 表示 ab  abc
|               左右表达式任意一个                    abc|def 表示 abc  def
================================================================================================
{m}             扩展前一个字符m次                     ab{2}c 表示abbc
{m, n}          扩展前一个字符m至n次（含n）            ab{1, 2}c 表示 abc  abbc
^               匹配字符串开头                        ^abc 表示 abc且在一个字符串的开头
$               匹配字符串的结尾                      abc$ 表示 abc且在一个字符串的结尾
()              分组标记， 内部只能使用 | 操作符       (abc) 表示 abc, (abc | def) 表示 abc def
\d              数字， 等价于[0 -9]             
\w              单词字符， 等价于[A -Z a-z 0-9_]
==================================================================================================

'''

# Re库主要功能函数
'''
函数                              说明
=====================================================================================================
re.search()                       在一个字符串中搜索匹配正则表达式的第一个位置， 返回match对象
re.match()                        从一个字符串的开始位置起匹配正则表达式， 返回match对象
re.find_all()                     搜索字符串， 以列表类型返回全部能匹配的子串
re.split()                        将一个字符串按照正则表达式匹配的结果进行分割，返回列表类型
re.finditer()                     搜索字符串，返回一个匹配结果的迭代类型， 每个迭代元素是match对象
re.sub()                          在一个字符串中替换所有匹配正则表达式的子串， 返回替换后的字符串   

'''

# Re的限定
'''
修饰符                             描述
=====================================================================================================
re.l                              使匹配对大小写不敏感
re.L                              做本地化识别(locale - aware)匹配
re.M                              多行匹配，影响^和$
re.S                              使.匹配包括换行在内的所有字符
re.U                              根据Unicode字符集解析字符。这个标志影响 \w  \W  \b  \B
re.X                              该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解

'''

# 代码
# 正则表达式：字符串模式  （判断字符串是否符合一定的标准）
import re

# (1). 创建模式对象
pat = re.compile('AA')       # 此处的AA， 是正则表达式， 用来去验证其他的字符串; complie是创建正则方法
# m = pat.search('CBA')        # search字符串被校验的内容，  也可以跟对象

m = pat.search('CBAABBCAAAA')        # search方法， 进行比反查找


print(m)    # <re.Match object; span=(2, 4), match='AA'>


# (2). 没有模式对象
m = re.search('ab', 'csbhjabcabbbab')    # 前面的字符串（参数1）是规则(模板)， 后面的字符串（参数2）是被校验的对象
print(m)


# (3). re.findall() 
print(re.findall('a', 'asdAdfgabAa'))   # 前面的字符串是规则（正则表达式），后面的字符串是被校验字符串(对象)

print(re.findall('[A-Z]', 'asdAdfFGAbAa'))  # ['A', 'F', 'G', 'A', 'A'] 利用正则表达式，将所有大写字母返回到列表里

print(re.findall('[A-Z]+', 'asdAdfFGAbAa'))  # ['A', 'FGA', 'A'] 利用正则表达式，将所有大写字母返回到列表里



# (4). re.sub('', '', '')   -- 第一个参数是：被替换对象； 第二个参数是：替换值； 第三个对象是：在哪里替换
print(re.sub('a', 'A', 'abcdcasdabmnb'))  # 找到a用A替换， 在第三个字符串中查找

# 注意：
# 建议在正则表达式中， 被比较的字符串前面加上r -- 不用担心转义字符的问题
a = r'\abc\-\"'
print(a)    # \abc\-\"