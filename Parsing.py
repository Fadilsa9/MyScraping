print("#" * 100 ) 
#🔴🔴🔴🔴🔴🔴🔴🔴🔴 30-55  141  **********************************************
#🔴🔴🔴🔴🔴🔴🔴🔴🔴 30 33 36 37 38 41-55  141  *******************************
print("#" * 100 ) 

# ---------------------------------------------------
# -- Web Scraping => Control Browser With Selenium --
# ---------------------------------------------------
# - Get Cryptocurrencies
# - Control Browser With Selenium For Automated Testing
# - Download File From The Internet
# - Subtitle Download And Add On Your Movies [ Many Modules ]
# - Get Quotes From Websites
# - Get Gold and Currencies Rate
# - Get News From Websites
# - --------------------------------------------

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://elzero.org")

browser.find_element_by_css_selector(".search-field").send_keys("Front-End Developer")

browser.find_element_by_css_selector(".search-submit").click()

browser.find_element_by_css_selector(".all-search-posts .search-post:first-of-type h3 a").click()

browser.implicitly_wait(5)

views_count = browser.find_element_by_css_selector(".z-article-info .z-info:last-of-type span:last-child")

browser.implicitly_wait(5)

print(views_count.get_attribute('innerHTML'))

browser.quit()
 

# string = "string$$$1324&&&"
# for char in string:
#   if char.isalnum():
#     print(f"{char} is alphnumeric, good")
#   else:
#     print(f"{char} is not alphnumeric, bad") 
    
# Forward Slash /
# Backslash \

# format on save
# preferences - settings - format on save
# هذا اذا مثلا سويت سطرين طباعة
# وحطيت بينهم فارزه منقوطه
# ثم سويت حفظ عن طريق كنترول أس
# فراح يلغي الفارزه المنقوطه
# وينزلهم جوه بعض
# وسوي تشغيل وينطيني النتيجه صح
# يعني يرتبلي الكود وكلشي تمام

# SYNTAX OF PYTHON
# السينتاكس مال بايثون يعتمد على المسافه الفارغه
# indentation المسافة الفارغة
# مسافات أسطر الأكواد لازم تكون مرتبه


# ----------------------------------
# type()
# All Data in Python is Object كائن
# ----------------------------------

# print(type(10)) # int => Integer
# print(type(100))
# print(type(-76))

# print(type(111.9)) # float => Floating Point Number
# print(type(1.4523234))
# print(type(-11.1111))
# print(type(-321.75348395))

# print(type("Hello Python")) # str => String

# print(type([1, 2, 3, 4, 5])) # list => List
# # Here We Use Squar Brackets

# print(type((1, 2, 3, 4, 5))) # tuple => Tuple 
# # Here We Use Parenthesis

# print(type({"One": 1, "Two": 2, "Three": 3})) # dict => Dictionary
# print({1:11, 2:22, 3:33, 4:44}) 
# print(type({1:11, 2:22, 3:33, 4:44, 5:55})) 
# print('\n') 


# print(type(2 == 2)) # bool => Boolean
# print(2 == 2) 


# print({1,2,3,4,5}) 
# print(type({1,2,3,4,5,6}))  # set 
# Is {} a set in Python?
# In Python, we create sets by placing all the elements inside curly braces {} ,
# separated by comma. A set can have any number of items 
# and they may be of different types (integer, float, tuple, string etc.). 
# But a set cannot have mutable elements like lists, sets or dictionaries as its elements


# compilation: translate code before run time
# compilation: translate code before run time 
# compilation: translate code before run time 



# [1,2,3,4,5,6,7,8,9,0] #list
# (1,2,3,4,5,6,7,8,9,0) #tuple
# {11:111, 22:222, 33:333, 44:444} #dic
# {1,2,3,4,5,6,7,8,9,0} #set


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# sep ==> разделитель между данными(по умолчанию это пробель)
# end ==> завершающий символ или строка(по умолчаню новая строка)

# # sep
# a, b, c = 11, 22, 33
# print(a, b, c) 
# print(a, b, c, sep=' | ') 
# # at least must be two elements then (sep) will work

# # end
# print("hello")
# print("world")

# print("hello", end=" ") 
# print("world") 

# print('hello', end='&&&') 
# print('world') 


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# --------------------------------------
# -- Variables --
# ---------------
# Syntax => [Variable Name] [Assignment Operator] [Value]
#
# Name Convention and Rules
# [1] Can Start With (a-z A-Z) Or Underscore
# [2] You Cannot With Num Or Special Characters
# [3] Can Include (0-9) Or Underscore
# [4] Cannot Include Special Characters
# [5] Name is Not Like name [ Case Sensitive ]
# --------------------------------------

# name = "Osama Elzero"  # Single Word => Normal
# myName = "Osama Elzero"  # Two Words => camelCase
# my_name = "Osama Elzero"  # Two Words => snake_case

# print(name)
# print(myName)
# print(my_name)



##### Lesson 8 ################################################


# ---------------
# -- Variables --
# ---------------
# Source Code : Original Code You Write it in Computer
# Translation : Converting Source Code Into Machine Language
# Compilation : Translate Code Before Run Time
# Run-Time : Period App Take To Executing Commands
# Interpreted : Code Translated On The Fly During Execution
# --------------------------------------------------------

# Reserved Words
# help("keywords")

# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)

# f, s, d, k, = 9, 8, 7, 6
# print(f, s, d, k)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Escape Secuences Characters
# on google ==> python escape secuence characters
# \b => back space يحذف الحرف اللي قبله

# print("HelloWor\bld") #will remove r
# print('Hi I\braq')
# print(45\b89) #it don't remove numbers

# print("Hello, \
# i love escape \
# new line \
# Dany")

# print("i love escape back slash \\")
# print('i love you \\')

# print('i love escape single quotes \'test\'')
# print("i love escape double quotes \"TEST\"")
# print("i love 'you'")
# print('i love "you"')

# print("i love line feed\nIt is new line")

# carriage return 
# print("1234567\rAbcd")
# print('abcd\rABC')
# هاي تجيب الاحرف بالبداية
# وتشيل من الأرقام اللي قبلها
# بكبر عدد الأحرف اللي وراها
# وتحط الأعداد الباقيه ورا الأحرف بالناتج

# 🔴 \t HOW MANY SPACES IS A \B
# print("Hello\tPython") #horizental tab ==> HERE 3 TABS
# print('howmany\tspaces') # ==> HERE 1 TAB
# print("howmany\tspaces") # ==> HERE 1 TAB
# print("Howmany\tSpaces") # ==> HERE 1 TAB

# \xhh ==> character hex value
# on google ==> letter hex value
# \x
# print("\x46\x61\x64\x68\x65\x6C")


# \b 
# \
# \\
# \'\'
# \"\"
# \n        لازم يكون بداخل كووتس
# \r        يحط الخانات الوراه كدامه والخانات البقن من كدامه يحطهن ورا الجابهن من وراه
# \t        #🔴 \t HOW MANY SPACES IS A \t ??
# \x


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# LESSON 11
# بالتربل كووتس اطبع النص كل سطر على حده
# \ بدل ما استخدم الباك سلاش
# # triple quotes ==> تحط الناتج مثل ما كاتبه.. كلمه جوه كلمه


# x = '''first
# second "test" 'test' 
# third'''
# print(x)

# y = """first
# second 'test' "test"
# third"""
# print(y)

# y = """first
# second 'test' "test" \
# third"""
# print(y)

# y = """first
# second 'test' \ "test"
# third"""
# print(y)

# print('''one tow
# three four \
# five six 
# seven eight \
# nine ten''')  

# y = """first
# second 'test' \\ "test"
# third"""
# print(y)

# y = """first
# second 'test' \\\ "test"
# third"""
# print(y)
# واحد ايسوي ايسكايب للسطر الوراه
# اثنين سويلي ايسكايب لواحد منهن والثاني طلعه بالناتج
# ثلاثه اول اثنين الاول سويلي ايسكايب للثاني وطلعه بالناتج
# والثالث سويلي ايسكايب للسطر الوراه
# وهكذاااا
# الزوج سوي ايسكايب واحد للثاني
# والفرد سويلي ايسكايب للسطر الوراك وجيبه 

# print(x+"\n"+y)
# # triple quotes ==> تحط الناتج مثل ما كاتبه.. كلمه جوه كلمه

# print("""one tow 
#              three""") 
#             #  🔴يشتغل بنفس الترتيب


# print("""one two \
# three""")
# # حتى لو اكو تربل كووتس 🔴
# # اذا احط الباك سلاش بالأخير
# # راح يسوي إسكايب ويحطهن على سطر واحد


# print('11 22 33 \ 
#     44 55 66')

# print(11 22 \ 44) #error

# print('''11 22 33 44 
# 66 77 88 99 00''') 

# print('''11 22 33 \ 
# 44 55 66 \\
#     88 99 00''')
# باك سلاش بالأخير وفراااااغ
# طلعلي الباك سلاش بالناتج
# لأن الفراغ يعتبر نص
# والباك سلاش لما يكون بداخل نص راح يطلع بالناتج


# print("""one two \ three""")
# print("""one two \\ three""")
# print("""one two \\\ three""")
# print("""one two \\\\ three""")
# # اذا اكثر من باك سلاش وحده
# # فألولى راح تسوي إسكايب
# # والثانيه تطلع بالناتج
# # كل اثنين يطلع منهن واحد بس 


# print('''first 1 1 \ second 2 2''')
# print('''third 3 3 \\ fourth 4 4''') 
# print('''fifth 5 5 \\\ sixth 6 6''')
# print('''seventh 7 7 \\\\ eighth 8 8''')
# print(''' 5 \\\\\ ''')
# print(''' 6 \\\\\\ ''')
# print(''' 7 \\\\\\\ ''') 
# print(''' 8 \\\\\\\\ ''') 


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Strings Indexing and Slicing

# # ---------------------------------
# # Strings Indexing & Slicing
# # [1] All Data in Python is Object
# # [2] Object Contain Elements
# # [3] Every Element Has Its Own Index
# # [4] Python Use Zero Based Indexing ( Index Start From Zero )
# # [5] Use Square Brackets To Access Element
# # [6] Enable Accessing Parts Of Strings, Tuples or Lists
# # ---------------------------------

# y = 'where are yoou yoo?'
# #    0123456789    14
# print(y[2:7:1]) 
# #🔴 The plus include the start but not include the end
# it's include 2 but not include 7


# x = 'i love you bro'
#    012345678910 11 12 13
#    <----- -5 -4 -3 -2 -1 
# i  l o v e   y o u   b r o 
#         -9-8-7-6-5-4-3-2-1
# print(x[::])
# print(x[0:5])
# print(x[0:13:2])
# print(x[-1])
# print(x[-6:-2]) 
# i  l o v e   y o u   b r o 
#         -9-8-7-6-5-4-3-2-1
# #🔴 The minus not include the start but include the end 
# it's not include -2 but include -6 ==> from -6 to -2



# -------------------------------------------------------------------------------------------------------------

# # Indexing ( Access Single Item )

# myString = "I Love Python"

# print(myString[0])  # Index 0 => I
# print(myString[9])  # Index 9 => t

# print(myString[-1])  # Index -1 => First Character From End
# print(myString[-6])  # Index -6 => 6th Character From End

# # Slicing ( Access Multiple Sequence Items )
# # [Start:End] End Not Included
# # [Start:End:Steps]

# print(myString[8:11])  # yth
# print(myString[3:5])  # ov

# print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
# print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)
# print(myString[:])  # Full Data

# print(myString[0::1])  # Full Data
# print(myString[::1])  # Full Data

# print(myString[::2])
# print(myString[::3])


# print([start:end:steps])
# print([22:33:4]) 

# x = 'i love python'
# print(x[-3]) 
# print(x[-9]) 
# print(x[-9:-3]) 
# # print(x[-3:-9]) # ==> No value
# print(x[2:15:2]) 
# print(x[::]) 


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# len(x)
# strip() lstrip(*) rstrip(*%)
# title()
# capitalize()
# zfill(5)
# upper()
# lower()



# x = "i love python"
# y = "    i love python    "
# print(len(x))
# print(len(y))
# # len احسبلي عدد أحرف أو خانات المحتوى
# # 🔴 حتى الفراغات تحسبها
# # Count all elements of the object 

# a = "    i love python    "
# print(a)
# print(a.strip())  #يشيل الفراغات من اليمين واليسار
# print(a.rstrip()) #يشيل الفراغات من اليمين
# print(a.lstrip()) #يشيل الفراغات من اليسار
# # 🔴 ()لااااااااااااازم أقواس 
# print(len(a.rstrip()))
# # Remove the spaces or the symbols 
# # From the left and the right, or only from the left, or only from the right

# a = ("****I love Python****")
# print(a.strip())
# print(a.strip("*"))
# print(a.rstrip("*"))
# print(a.lstrip("*"))

# x = "%^&%^&%^&i love Allh%^&%^&%^&"
# print(x)
# print(x.rstrip())
# print(x.rstrip("%^&"))
# print(x.rstrip("%"))#don't work, must write all the symbols#🔴#

# y = "i love my Family 9i so Much 5g"
# print(y.title()) 
# print(y.capitalize()) #Only first letter


# # zfill => zerofill
# a, b, c = "1", "11", "111"
# print(a.zfill(3), b.zfill(3), c.zfill(3))
# print(a)
# print(b)
# print(c)
# print('\n')
# print(a.zfill(3))
# print(b.zfill(3))
# print(c.zfill(3))

# a, b, c, d = "1", "11", "111", "1111"
# print(a)
# print(b)
# print(c)
# print(d)
# print('\n')
# print(a.zfill(4))
# print(b.zfill(4))
# print(c.zfill(4))
# print(d.zfill(4))

# print("-------------")

# g = "Fadhil"
# print(g.upper())

# h = "FADHil"
# print(h.lower())

# print(x.upper())
# print(x.lower())


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ---------------------
# -- Strings Methods --
# ---------------------

# -------------------------------------------------------------------------------------------------------------

# split
# center
# count
# swapcase
# startswith
# endswith

# split rsplit center count swapcase startswith endswith
# split rsplit center count swapcase starstwith endswith
# split rsplit center count swapcase startswith endswith 


# split ==> قسملي كالقائمه 
# rsplit 
# يقتسـم - يتشقـق - يتصـدع

#🔴# center ==> ضيفلي بكد هالعدد فراغات أو هذا الرمز من اليمين واليسار
# والعدد هذا يضم عدد حروف النص أيضاً

# count ==> احسبلي كم مره موجوده هاي الكلمه او الحرف او الرقم بالنص 

# swapcase ==> بدلي الاحرف الكبتل بصمول والصمول بكبتل
# حالة التبادل

# startswith ==> كولي هل يبدأ النص بهذا الحرف 
# endswith ==> كولي هل ينتهي النص بهذا الحرف
# او هل يبدأ او ينتهي من الأيندكس هذا الى الأندكس هذا
# -----------------------------------------------------------------------------------------------------------



# split() rsplit()
# a = "I Love Python and PHP and MySQL"
# print(a.split())

# b = "I-Love-Python-and-PHP-and-MySQL"
# print(b.split("-"))

# c = "I-Love-Python-and-PHP-and-MySQL"
# print(c.split("-", 3))
# print(c.split(" ", 3))

# d = "I-Love-Python-and-PHP-and-MySQL"
# print(d.rsplit("-", 3))

# x = ('do you know Python or php and css')
# print(x)
# print(x.split())
# print(x.split(' ', 3))
# print(x.rsplit(' ', 4))
# print(len(x.rsplit(' ', 5)))
# print(type(x.rsplit(' ', 6)))


# # center()
# e = "Osama"
# print(e.center(9))  # Spaces
# print(e.center(9, "#"))  # Hashes
# print(e.center(15, "@"))  # @

# v = 'Fadhilsa'
# print(v.center(11, '*'))
# print(v.center(100, "^"))


# # count()
# f = "I Love Python and PHP Because PHP is Easy"
# print(f.count("PHP"))  # 2 PHP Words
# print(f.count("PHP", 0, 25))  # Only One PHP Word

# jj = 'i like you because you this is really you'
# print(jj.count('you')) 
# print(jj.count('this is really'))

# dd = 1, 2, 3, 4, 5, 1, 1, 1, 1 
# print(dd.count(1)) 


# # swapcase()
# g = "I Love Python"
# h = "i lOVE pYTHON"

# print(g.swapcase())
# print(h.swapcase())


# startswith()
# i = "I Love Python"
# print(i.startswith("I"))
# print(i.startswith("S"))
# print(i.startswith("P", 7, 12))

# # endswith()
# j = "I Love Python"
# print(j.endswith("n"))
# print(j.endswith("S"))
# print(j.endswith("e", 2, 6))



# x = 'how are you bro'
# print(x.split())   
# print(x.rsplit())
# x = 'how$$are$$you$$bro'
# print(x.split('$$')) 
# print(x.center(40, '%')) 
# print(len(x.center(40, '$')))
# print(len(x))  
# print(x.count('are'))
# print(x.swapcase())
# print(x.startswith('how'))
# print(x.endswith('bro'))


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# index   
# find    
# center
# rjust
# ljust
# split
# splitlines
# expandtabs
# istitle
# isspace
# islower
# isupper
# isalpha
# isalnum


# index(SubString, Start, End)
# a = 'i love coding'
# print(a.index("v"))
# print(a.index('d', 2, 11)) 
# print(a.index('g', 3, 9)) #error ==> because not found

# b = "it's really good"
# print(b.find("'")) 
# print(b.find('g', 5, 9)) # -1 ==> because not found
# Q\\ Waht's the deference between index and find??

# rjust
# # right-justified ==> the string in the right + spaces or the symbole that i write
# ljust
# # left-justified ==> the string in the left
# m = 'Fadhil'
# print(m.rjust(9)) #By default spaces
# print(m.rjust(10, '%')) 
# print(m.ljust(15))
# print(m.ljust(15, '&'))


# # splitlines
# it's make the string like a list 
# every line is one element
# h = '''first step
# second step
# third step'''
# print(h.splitlines()) 
# print(h.split()) 


# # expandtabs
# # إكسباند يعني توسيع
# y = 'hi\tpeople\twe\tare\there'
# print(y.expandtabs())
# print(y.expandtabs(2))  

# k = "hello\tworld\tI\tlove\tpython"
# print(k.expandtabs(5)) 


# l = 'I Love Pythonofo Yoo 5G'
# print(l.istitle()) 
# r = 'I Love Her Yoo 5g'
# print(r.istitle()) 

# p = ' '
# o = ''
# i = '@'
# print(p.isspace()) 
# print(o.isspace()) 
# print(i.isspace()) 

# first = 'hello iraq'
# print(first.islower())
# second = 'hello irAq'
# print(second.islower()) 

# third = 'HELLO IRAQ'
# print(third.isupper()) 
# fourth = "HELLO IrAQ"
# print(fourth.isupper())


# q = 'ahmed_fadhil'
# w = 'AhmedFadhil999'
# v = '999AhmedFadhil'
# s = 'Ahmed%-*Fadhil'
# print(q.isidentifier()) 
# print(w.isidentifier()) 
# print(v.isidentifier()) 
# print(s.isidentifier()) 

# isalpha
# isalnum
# f = 'AaaBbbZzz'
# print(f.isalpha()) 
# # The alpha is all letters(smalls and captitals) without numbers 
# print(f.isalnum()) 
# # isalnum is all letters(smalls and capitals) and numbers
# c = 'AaaaZzzz12345'
# print(c.isalpha()) 
# print(c.isalnum()) 


# ////////////////////////////////////////////////////////////////////
######## LESSON 16 ###################################################

# # replace(old value, new value, count)
# A = 'hi first second third first first first'
# print(A)
# print(A.replace('first', '1')) 
# print(A.replace('first', 'one', 3))

# join (iterable)
# the join takes list or tuple or etc..., and return string
# MyList = ['ahmed', 'fadhil', 'mahmood', 'ali'] 
# print(MyList)
# print(type(MyList)) 
# print('_'.join(MyList)) 
# print('-'.join(MyList)) 
# print(' '.join(MyList)) 
# print(type(' '.join(MyList))) 


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Strings Formatting
# placeholder

# %s ==> String
# %d ==> Number decimal
# %f ==> Float


# 🔴    "".    ''.  ==> يطلع هواي أنواع


# x = 'hello world'
# y = 'hiii world'
# print('%s, %s' % (x,y))

# MyName = 'Fadhil'
# MyAge = 25
# MyRank = 4
# print('my name is: ' + 'Fadhil')
# print("my name is: " + MyName)
# # print("my name is: " + MyName + "and my age is: " + MyAge)  # Type Error
# print('my name is: %s' % 'Fadhil')
# print('my name is: %s' % MyName)
# print('my name is: %s and my age is: %d' % (MyName, MyAge))
# print('my name is: %s and my age is: %d and my rank is: %f' % (MyName, MyAge, MyRank))
# print('my name is: %s and my age is: %d and my rank is: %.0f'%(MyName,MyAge,MyRank))

# # Control Floating Number
# print('my name is: %s and my age is: %d and my rank is: %.19f' % (MyName, MyAge, MyRank))
# print('my name is: %s and my age is: %d and my rank is: %.2f' % (MyName, MyAge, MyRank))

# # Truncate String
# # cut some of the string
# ThisIsMyVeryLongString = 'Assalamu Alaykum, how are you all today? is every thing ok?'
# print('The letter is %s' % ThisIsMyVeryLongString)
# print('The letter is %.11s' % ThisIsMyVeryLongString)

# # The formatting string is without errors when strings with integers
# # So, it's better


# x="i'm here all the day today"
# print('%.3s'%x)
# print('%.19s'%x)
# print('{}'.format(x))
# print('{:s}'.format(x))
# print('{:.3s}'.format(x))
# # print('{:_s}'.format(x)) #error


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# name = 'Fadhil'
# age = 68
# rank = 9
# print('my name is: ' + name)
# print('my name is: ' + "Fadhil") 
# print('my name is: %s' % name)
# print('my name is: %s' % 'Fadhil') 
# print('my name is: {}' .format(name)) 
# print('my name is: {}'.format('Fadhil')) 
# print('name: {} age: {} rank: {}'.format(name, age, rank))
# print('name: {:s} age: {:d} rank: {:f}' .format(name, age, rank))

# # Control floating point number
# # Truncate string
# print('name: {:.3s} age: {:d} rank: {:.2f}' .format(name, age, rank))

# {:s}
# {:d}
# {:f}


# # Format money
# myMoney = 745456789987
# print('my money in bank is: {}'.format(myMoney))
# print('my money in bank is: {:d}'.format(myMoney))
# print('my money in bank is: {:_}'.format(myMoney))
# print('my money in bank is: {:_d}'.format(myMoney))
# print('my money in bank is: {:,d}'.format(myMoney))
# print('my money in bank is: {:.d}'.format(myMoney)) # error
# # print('my money in bank is: {:&d}'.format(myMoney)) # error


# # ReArrange items
# a, b, c = 'one', 'two', 'three'
# print('Hii {} {} {}'.format(a, b, c))
# print('Hii {2} {1} {0}'.format(a,b,c))

# x, y, z = 100, 200, 300
# print("Welcome: {1} {2} {0}".format(x, y, z))
# print("Welcome: {1:d} {2:d} {0:d}".format(x, y, z))
# print("Welcome {2:f} {1:f} {0:f}".format(x,y,z))
# print("Welcome {2:.4f} {1:.8f} {0:.12f}".format(x, y, z)) 


# # Format in version 3.6+
# myName = 'Ahmed'
# myAge = 25
# print('my name is : {myName} and my age is : {myAge}')
# print(f'my name is : {myName} and my age is : {myAge}')

# name = 'ahmed'
# age = 25
# print('my name is: {name} and my age is: {age}')
# print(f'my name is: {name} and my age is: {age}')

# j = "hello, how are you"
# print(f"{j}") 


# numbers = [1, 2, 3, 4, 5]
# print("The numbers are " + str(numbers))

# value = 42
# print("The value is %d" % value)
#🔴with ("%") we can concatinate int with str without any errors

# ll = 42
# print("The value is {}" .format (ll)) 
# with ("{}" .format) we also can concatinate int with str without any errors

# value = 42
# print(f"The value is {value}")
# with (f"{}") we also can concatinate int with str without any errors


# # range 
# numbers = range(1, 5)
# print(numbers)  # ===> range(1, 5)
# print(list(numbers)) # ===> [1, 2, 3, 4] ===> Here stops before the stop argument


# dict 


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# # Integer
# print(type(0))
# print(type(1))
# print(type(100))
# print(type(-0))
# print(type(-110))

# # Float
# print(type(0.0))
# print(type(0.000))
# print(type(1.1))
# print(type(1.5000))
# print(type(999.77777777))
# print(type(-0.0))
# print(type(-0.000000000000))
# print(type(-1.1))
# print(type(-34.3843948))

# Complex
# Complex number ==> Real part + Imaginary part
# my_Complex_Number = 5+6j
# print(my_Complex_Number) #it puts the result in parentheses => (5+6j)
# print(type(my_Complex_Number))
# print('{}' .format(my_Complex_Number)) 
# print('{}' .format(my_Complex_Number.real)) # => 5.0 ----------------
# print('{}' .format(my_Complex_Number.imag)) # => 6.0 ----------------
# print('The whole complex number is: {}'.format(my_Complex_Number))
# print('Real part is: {}'.format(my_Complex_Number.real))
# print('Imaginary part is: {}'.format(my_Complex_Number.imag))

# [1] You can convert from int to float or complex
# [2] You can convert from float to int or complex
# [3] But you cannot convert from complex to any type ==> error

# print(111)
# print(float(111))
# print(complex(111))

# # print(11.111)
# print(int(11.111))
# print(complex(11.111))

# print(42+9j)
# # print(int(42+9j)) #==> error
# # print(float(42+9j)) #==> error


# x = 11
# y = 11.1
# z = 11+1j
# print(float(x)) 
# print(complex(x)) # => 11+0j
# print(int(y)) 
# print(complex(y))  
# print(complex(888.44444444)) 
# # print(int(z)) 
# # print(float(z)) 



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# # Addition +
# print(2 + 2)
# print(-5 + 8)
# print(7.4 + 99.2) 
# print(-31.6 + 45.3)
# print(-5 + -6) 

# # Subtraction
# print(10 - 1)
# print(-10 - 6) 
# print(-5 - -4)
# print(5.0 - 2) 
# print(8.3 - 11.1)

# # Multiplication
# print(22 * 11)
# print(4 + 5 * 9)
# print((5 + 4) * 9)

# # Division
# print(100 / 20) # 5.0 ==> with point
# print(1 / 1) 
# # print(0 / 0) #error
# print(7 / 7) 
# print(int(7 / 7)) 
# print(int(100 / 20)) # 5

# # Modulus
# print(8 % 2) 
# print(9 % 2) 
# print(20 % 5)
# print(23 % 5) 
# print(11 % 3) 
# print(79 % 9) 

# # Exponent
# print(2 ** 5) 
# print(2 * 2 * 2 * 2 * 2) 
# print(5 ** 4)  
# print(9 ** 5) 
# print(9 * 9 * 9 * 9 * 9) 

# # Floor division
# # division without a reminder
# # القسمه بدون باقي
# print(100 // 20)
# print(119 // 20)
# print(17 // 9) 

# a = b = c = 7
# print(a, b, c)
# print( id(a), id(b), id(c)


# بالعكس
# a , b = 1, 2
# print(a,b)

# a , b = b , a
# print(a,b)

# a = b = c = 7
# print(a, b, c)
# print( id(a), id(b), id(c)


# print(-7 // 2) #🔴


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

# myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

# print(myAwesomeList)  # Whole List
# print(myAwesomeList[1])  # "Two"
# print(myAwesomeList[-1])  # True
# print(myAwesomeList[-3])  # 1

# print(myAwesomeList[1:4])  # ['Two', 'One', 1]
# print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
# print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]

# print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
# print(myAwesomeList[::2])  # ['One', 'One', 100.5]

# print(myAwesomeList)
# myAwesomeList[1] = 2
# myAwesomeList[-1] = False
# myAwesomeList[0:3] = ["A"]
# print(myAwesomeList)


# print(myAwesomeList[0::]) 
# print(myAwesomeList[220]) # => Error, Out of rage 


# myAwesomeList = ["One", "Two", "One", 1, 100.5, True]
# print(myAwesomeList) 

# myAwesomeList[4] = "iraq"
# print(myAwesomeList) 

# myAwesomeList[0:4] = [] # Complex edit => Did these elements impty or delete them
# print(myAwesomeList) 

# myAwesomeList[0:3] = ["X", "Y", "Z"] 
# print(myAwesomeList) 

# myAwesomeList[:] = [1] #Take all list and return just one element equale 1
# print(myAwesomeList) 
# # so i can add, delete or edit... List Are Mutable => Add, Delete, Edit


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# -------------------
# -- Lists Methods --
# -------------------

# append()
# ألحقَ-زادَ
# add the element in the end of the list

# myFriends = ["Osama", "Ahmed", "Sayed"]
# myOldFriends = ["Haytham", "Samah", "Ali"]

# myFriends.append("Alaa")
# myFriends.append(100)
# myFriends.append(150.200)
# myFriends.append(True)
# myFriends.append(myOldFriends)  # It's a list, but like one element

# print(myFriends)
# print(myFriends[2]) # Returne the index number 2, which is "Sayed"
# print(myFriends[6])
# print(myFriends[7])
# print(myFriends[7][2])


# extend()
# يمتد

# a = [1, 2, 3, 4] 
# b = ["A", "B", "C"]
# c = ["One", "Two"]

# # a.extend() # list.extend() takes exactly one argument (0 given) => error
# a.extend(a) # Extened itself
# a.extend(b) 
# a.extend(c)

# print(a)


# remove()

# x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
# x.remove("Osama") # Removed the first "Osama" 
# print(x)



# sort()

# y = [120, 2, 1, 100, -10, 17, 29]
# y = [1, 2, 100, 120, -10, 17, 29, 'hh'] # error, because different data types, and `sort` don't accept different types
# y = ['A', 'B', 'C']
# y = [True, False, True, False] # return [False, False, True, True]  ... i think because False is 0 and it's smaller than True which is 1 
# y.sort()
# y.sort(reverse=True)  # order numbers by reverse
# y.sort(reverse=False) # by defaulte False
# print(y) 
# sort make numbers in order from the smaller to the bigger
#### all elements must be one type of data


# reverse()

# z = [10, 1, 9, 80, 100, "Osama", 100]
# z.reverse()
# print(z)
# reverse, just reverse the list


# x = ['ff', 'jj', 'mm', 'ss']
# x.append("www")  
# x.append(23) 
# x.append(False) 
# y = [1, 2, 3, 4, [11, 22, 33]]  
# x.append(y) 
# print(x) 
# print(x[7][3]) 
# print(x[7][4][2]) 

# ll = [1, 2, 3, 4, 5, 'aa', 'b'] 
# ll.remove('aa') 
# print(ll) 


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# # clear
# k = [' "" ', 'ii', 'oo']
# k.clear() # => []
# print(k) 


# # copy
# x = [11, 22, 33, 44, 55]
# y = x.copy()
# print(x) # Main list
# print(y) # Copied list

# x.append(88) 
# print(x) 
# print(y) # Without 88 because `copy` takes the main list not the append list and do copy to it
# # use it when i want to return the list without any changed or append


# # count
# rr = [9, 8, 7, 9, 6, 9, 5, 4, 9, 3, 2, 9, 1] 
# print(rr.count(9)) 


# # index
# ii = ['sjf', 'we', 'they', 'our', 'sos', 'we']
# print(ii.index('we')) 
# print(ii.index("sos")) 



# insert

# oo = [5, "nnn", 8, True, 23]

# print(oo.insert(3, "pp")) # => None 
# In Python, if a function or a method does not return any value, 
# it is considered to have a return value of None. 
# So, in this case, oo.insert(3, "pp") returns None 
# and that's why print(oo.insert(3, "pp")) outputs None.

# oo.insert(3, 'pp') # Put 'pp' before index 3   # positive index from start
# oo.insert(-4, False) # Put False before index -4  # negative index from end 
# print(oo) 



# # pop
# q = ["vpn", 75, "Urban", 39, True, 8.22, "Iraq\\"]  
# print(q) 
# print(q.pop(4)) # Take the index and give me the value of this index


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# print(['ahmed', 'fadhil', 'ali', 'mahmood'])
# print(type(['ahmed','fadhil','ali','muhammad']))

# print((1,2,3,4,5))
# print(type((1,2,3,4,5)))

# print({1,2,3,4,5})
# print(type({1,2,3,4,5,7}))

# [1,2,3,4,5,6,7,8,9,0] #list
# (1,2,3,4,5,6,7,8,9,0) #tuple
# {11:111, 22:222, 33:333, 44:444} #dic
# {1,2,3,4,5,6,7,8,9,0} #set


# print('''one tow
# three four \
# five six
# seven eight \\\
# nine ten''')

# print('11 22 33 \ 
#     44 55 66')

# print(11 22 \ 44) #error

# print('''11 22 33 44 
# 66 77 88 99 00''') 

# print('''11 22 33 \ 
# 44 55 66 \\
#     88 99 00''')
# باك سلاش بالأخير وفراااااغ
# طلعلي الباك سلاش بالناتج
# لأن الفراغ يعتبر نص
# والباك سلاش لما يكون بداخل نص راح يطلع بالناتج

# print('''first 1 1 \ second 2 2''')
# print('''third 3 3 \\ fourth 4 4''') 
# print('''fifth 5 5 \\\ sixth 6 6''')
# print('''seventh 7 7 \\\\ eighth 8 8''')
# print(''' 5 \\\\\ ''')
# print(''' 6 \\\\\\ ''')
# print(''' 7 \\\\\\\ ''') 
# print(''' 8 \\\\\\\\ ''')

# a = b = c = 7
# print(a, b, c)
# print( id(a), id(b), id(c)


# بالعكس
# a , b = 1, 2
# print(a,b)

# a , b = b , a
# print(a,b)

# a = b = c = 7
# print(a, b, c)
# print( id(a), id(b), id(c)


# print(-7 // 2) #🔴
# print(2 * 4.5) #
# print(-9 % 5) #==> 1
# print(9 % -5)
# print(-9 % -5) 

# a = 2
# a += 2
# a *= 2
# a /= 2
# print(a)  



# abs

# x = -5
# print(abs(x)) #reverse this number from - to +
# # تعكس السالب موجب
# # والموجب تبقيه مثل ما هوا

# y = abs(-41.99) #also we can do it in this way
# print(y) 
# #and of course the value must be + 


# # min

# print(min(5,3,9,2,19,-11))
# # it takes the smallest number


# # max

# print(max(11,12,22,44,199)) 
# # it takes the bigger number


# # pow

# print(pow(6, 2)) #it's like **
# # 6 to the power 2
# print(pow(5, 8)) #==> 5 to the power 8
# print(5 ** 8) # the same value 

# print(pow(78, 0.5))   
# print(pow(27, 1/3)) 


# # round
# # Округление
# print(round(0.5)) #==> 0
# print(round(1.5)) #==> 2 
# # قربلي هذا الرقم
# # النص مرات يقرب للأصغر ومرات للأكبر
# print(round(10.5))  

# # abs() min() max() pow() round()
# print(max(1, 2, abs(-3), -10)) 
# print(max(1, 2, abs(min(10, 5, -3)), -10))  


# import math #==========> this library alow us to use these functions 

# # math.  ==> #show me all math library functions

# x = 'ahmed'
# y = 25
# g = 777
# print("%s %s" % (x,y)) 
# print("%s %d" % (x,y)) 
# print("%s %d %f" % (x, y, g)) 
# print("%.2f" % g) #Controle floating point 
# print("%.3s" % x) #Controle string - truncate string

# a = 'ahmed fadhil'
# b = 25
# c = 777
# print('{}' .format(a))  
# print('{:s}' .format(a))  
# print('{:.9s}' .format(a))   
# print('{} {}' .format(x, y)) 
# print("{}{}{}" .format(x,y,g)) 
# print("{} {} {}" .format("ahmed", 25, 778)) 


# numbers = [1, 2, 3, 4, 5]
# print("The numbers are " + str(numbers))

# value = 42
# print("The value is %d" % value)
#🔴with ("%") we can concatinate int with str without any errors

# ll = 42
# print("The value is {}" .format (ll)) 
# with ("{}" .format) we also can concatinate int with str without any errors

# value = 42
# print(f"The value is {value}")
# # with (f"{}") we also can concatinate int with str without any errors


# x = ['ff', 'jj', 'mm', 'ss']
# x.append("www")  
# x.append(23) 
# x.append(False) 
# y = [1, 2, 3, 4, [11, 22, 33]]  
# x.append(y) 
# print(x) 
# print(x[7][3]) 
# print(x[7][4][2]) 


# ll = [1, 2, 3, 4, 5, 'aa', 'b'] 
# ll.remove('aa') 
# print(ll) 

# # index
# ii = ['sjf', 'we', 'they', 'our', 'sos', 'we']
# print(ii.index('we')) 
# print(ii.index("sos")) 



# # insert

# oo = [5, "nnn", 8, True, 23]

# # print(oo.insert(3, "pp")) # => None 
# # In Python, if a function or a method does not return any value, 
# # it is considered to have a return value of None. 
# # So, in this case, oo.insert(3, "pp") returns None 
# # and that's why print(oo.insert(3, "pp")) outputs None.

# oo.insert(3, 'pp') # Put 'pp' before index 3   # positive index from start
# oo.insert(-4, False) # Put False before index -4  # negative index from end 
# print(oo) 



# # pop
# q = ["vpn", 75, "Urban", 39, True, 8.22, "Iraq\\"]  
# print(q) 
# print(q.pop(4)) # Take the index and return the value of this index 
# ---------------------------------------------------------------------------------------------------------------


# -----------------------------
# -- Tuple --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# -----------------------------

# # Tuple Syntax & Type Test

# myAwesomeTupleOne = ("Osama", "Ahmed")
# myAwesomeTupleTwo = "Osama", "Ahmed"

# print(myAwesomeTupleOne)
# print(myAwesomeTupleTwo)

# print(type(myAwesomeTupleOne))
# print(type(myAwesomeTupleTwo))

# # Tuple Indexing

# myAwesomeTupleThree = (1, 2, 3, 4, 5)
# print(myAwesomeTupleThree[0])
# print(myAwesomeTupleThree[-1])
# print(myAwesomeTupleThree[-3])

# # Tuple Assign Values

# myAwesomeTupleFour = (1, 2, 3, 4, 5)
# # myAwesomeTupleFour[2] = "Three"
# # print(myAwesomeTupleFour)  # 'tuple' object does not support item assignment

# # Tuple Data

# myAwesomeTupleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)
# print(myAwesomeTupleFive[1])
# print(myAwesomeTupleFive[-1])
# -------------------------------------------------------------------------------------------------------------


# -----------
# -- Tuple --
# -----------

# # Tuple With One Element

# myTuple1 = ("Osama")
# myTuple2 = "Osama"

# print(myTuple1)
# print(myTuple2) 

# print(type(myTuple1)) # str  .. becauese without ,
# print(type(myTuple2)) # str  .. becauese without ,

# print(len(myTuple1))
# print(len(myTuple2)) 
# # --------------


# myTuple1 = ("Osama",)
# myTuple2 = "Osama",

# print(myTuple1)
# print(myTuple2)

# print(type(myTuple1)) # tuple  .. becauese with ,
# print(type(myTuple2)) # tuple   .. becauese with ,

# print(len(myTuple1)) # 1 .. because tuple, and here there is only 1 tuple
# print(len(myTuple2)) # 1 .. because tuple, and here there is only 1 tuple
# # ---------------


# # # Tuple Concatenation

# a = (1, 2, 3, 4)
# b = (5, 6)

# c = a + b
# d = a + ("A", "B", True) + b

# print(c) 
# print(d)
# ----------------- 


# # Tuple, List, String Repeat (*)

# myString = "Osama"
# myList = [1, 2]
# myTuple = ("A", "B")

# print(myString * 6)
# print(myList * 6)
# print(myTuple * 6)

# # Methods => count()

# a = (1, 3, 7, 8, 2, 6, 5, 8)
# print(a.count(8))

# # # Methods => index()

# b = (1, 3, 7, 8, 2, 6, 5)
# print(b.index(7))  
# # print("The Position of Index Is: " + b.index(7))  # Error  .. can only concatenate str (not "int") to str
# print("The Position of Index Is: {:d}".format(b.index(7)))
# print(f"The Position of Index Is: {b.index(7)}")



# # # Tuple Destruct

# a = ("A", "B", "C")
# a = ("A", "B", 4, "C")
# # error .. because there are 4 elements and i want just 3
# # the selousion is _,  

# # x, y, z = "A", "B", "C" 
# # x, y, z = a
# x, y, _, z = a  # _, ignore 4

# print(x)
# print(y)
# print(z)


# --------------------------------------------------------------------------------------------------------------
# ### 28


# difference
# difference_update
# intersection()

# -----------------
# -- Set Methods --
# -----------------

# # difference()

# a = {1, 2, 3, 4}
# b = {1, 2, 3, "Osama", "Ahmed"}
# print(a)
# print(a.difference(b))  # a - b
# # Return the difference of two or more sets as a new set.
# # print(a - b) # doing the same 
# print(a)

# print("=" * 40)  # Separator
# # ------------------


# # difference_update()

# c = {1, 2, 3, 4}
# d = {1, 2, "Osama", "Ahmed"}
# print(c)
# c.difference_update(d)  # c - d
# # Remove all elements of another set from this set.
# print(c)

# print("=" * 40)  # Separator
# # ----------------------------------

# # intersection()

# e = {1, 2, 3, 4, "X", "Osama"}
# f = {"Osama", "X", 2}
# print(e)
# print(e.intersection(f))  # e & f ==> doing the same
# # Return the intersection of two sets as a new set.
# # المتداخلات
# print(e)

# print("=" * 40)  # Separator
# # ------------------------------


# # intersection_update()

# g = {1, 2, 3, 4, "X", "Osama"}
# h = {"Osama", "X", 2}
# print(g)
# g.intersection_update(h)  # g & h
# print(g)

# print("=" * 40)  # Separator
# # ----------------------------


# symmetric_difference()
# ^ between elements doing the same

# i = {1, 2, 3, 4, 5, "X"}
# j = {"Osama", "Zero", 1, 2, 4, "X"}
# print(i)
# print(i.symmetric_difference(j))  # i ^ j
# # return the elements which not repeated in both sets
# # Return the symmetric difference of two sets as a new set.
# # ` ^ ` doing the same 
# print(i)

# print("=" * 40)  # Separator
# # -----------------------------------


# symmetric_difference_update()

# k = {1, 2, 3, 4, 5, "X"}
# l = {"Osama", "Zero", 1, 2, 4, "X"}
# print(k)
# k.symmetric_difference_update(l)  # k ^ l ==> doing the same thing
# # return the elements which not exist in both sets
# # دورلي العناصر المش موجوده بالاثنين
# print(k)

# print("-" * 100) 




# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

# uName = "Osama"
# # uCountry = "Egypt" 
# uCountry = "Kuwait" 
# # uCountry = "KSA" 
# cName = "Python Course"
# cPrice = 100

# if uCountry == "Khalid":
#   print(f"Hello {uName} Because You Are From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

# elif uCountry == "KSA":
#   print(f"Hello {uName} Because You Are From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

# elif uCountry == "Kuwait":
#   print(f"Hello {uName} Because You Are From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

# else:
#   print(f"Hello {uName} Because You Are From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")
# -------------------------------------------------------------------------------------------------------------


# # ---------------
# # -- Nested If -- 42
# # ---------------

# uName = "Osama"
# isStudent = "Yes"
# uCountry = "Egypt"
# cName = "Python Course"
# cPrice = 100

# if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":

#   if isStudent == "Yes":

#     print(f"Hi {uName} Because U R From {uCountry} And Student")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")

#   else:

#     print(f"Hi {uName} Because U R From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")


# elif uCountry == "Kuwait" or uCountry == "Bahrain":

#   print(f"Hi {uName} Because U R From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

# else:

#   print(f"Hi {uName} Because U R From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")
# -----------------------------------------------------------------------------------------------------------------------------------


# # ----------------------------------
# # -- Ternary Conditional Operator -- 43
# # ----------------------------------

# country = "A"

# if country == "Egypt" : print(f"The Weather in {country} Is 15")
# elif country == "KSA" : print(f"The Weather in {country} Is 30")
# else : print("Country is Not in The List")

# # Short If

# movieRate = 18
# age = 18

# if age < movieRate :

#   print("Movie S Not Good 4U") # Condition If True

# else :

#   print("Movie S Good 4U And Happy Watching") # Condition If False

# print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")

# # Condition If True | If Condition | Else | Condition If False

# print("#" * 111) 


# con = "jj"
# if con == "jj": print("lao")  
# elif con == "kk": print("amal") 

# print("this is" if con == "jj" else "this is not")  


# format on save ==>>> settings - performance - formate on save 

# -------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --  44
# -------------------------------------------------

# # # Write A Very Beautiful Note
# # print("#" * 80)
# # print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(80, '#'))
# # print("#" * 80)

# # Collect Age Data
# age = input("Please Write Your Age").strip()

# # Collect Time Unit Data
# unit = input("Please Choose Time Unit: Months, Weeks, Days ").strip().lower()

# # Get Time Units
# months = int(age) * 12
# weeks = months * 4
# days = int(age) * 365

# if unit == 'months' or unit == 'm':

#   print("You Choosed The Unit Months")
#   print(f"You Lived For {months:,} Months.")

# elif unit == 'weeks' or unit == 'w':

#   print("You Choosed The Unit Weeks")
#   print(f"You Lived For {weeks:,} Weeks.")

# elif unit == 'days' or unit == 'd':

#   print("You Choosed The Unit Days")
#   print(f"You Lived For {days:,} Days.")



# x = {
#     "ss" : "kk",
#     "jj" : "mm" 
#       }
# print(x) 


# # Create Dictionary From Variables

# frameworkOne = {
#   "name": "Vuejs",
#   "progress": "80%"
# }

# frameworkTwo = {
#   "name": "ReactJs",
#   "progress": "80%"
# }

# frameworkThree = {
#   "name": "Angular",
#   "progress": "80%"
# }

# allFramework = {
#   "one": frameworkOne,
#   "two": frameworkTwo,
#   "three": frameworkThree
# }

# print(allFramework)

# # ----------------------------------------------------------------------------------------


# d = {'apple': 1, 'banana': 2, 'cherry': 3}
# print(d.popitem()) # ('cherry', 3)
# print(d) # {'apple': 1, 'banana': 2}



# # --------------------------
# # -- Comparison Operators --
# # --------------------------
# # [ == ] Equal
# # [ != ] Not Equal
# # [ > ] Greater Than
# # [ < ] Less Than
# # [ >= ] Greater Than Or Equal
# # [ <= ] Less Than Or Equal
# # --------------------------

# # Equal + Not Equal

# print(100 == 100)
# print(100 == 200)
# print(100 == 100.00)

# print("#" * 50)

# print(100 != 100)
# print(100 != 200)
# print(100 != 100.00)

# print("#" * 50)

# # Greater Than + Less Than

# print(100 > 100)
# print(100 > 200)
# print(100 > 100.00)
# print(100 > 40)

# print("#" * 50)

# print(100 < 100)
# print(100 < 200)
# print(100 < 100.00)
# print(100 < 40)

# print("#" * 50)

# # Greater Than Or Equal + Less Than Or Equal

# print(100 >= 100)
# print(100 >= 200)
# print(100 >= 100.00)
# print(100 >= 40)

# print("#" * 50)

# print(100 <= 100)
# print(100 <= 200)
# print(100 <= 100.00)
# print(100 <= 40)

# print("#" * 50)




# # --------------------------
# # -- Assignment Operators --
# # --------------------------
# # =
# # +=
# # -=
# # *=
# # /=
# # **=
# # %=
# # //=
# # --------------------------

# x = 10  # Var One
# y = 20  # Var Two

# # Var One = Self [Operator] Var Two
# # Var One [Operator]= Var Two

# # x += y
# x -= y

# print(x)


# # -----------------------

# # -- Boolean Operators --
# # -----------------------
# # and
# # or
# # not
# # -----------------------

# age = 36
# country = "Egypt"
# rank = 10

# print(age > 16 and country == "Egypt" and rank > 0)  # True
# print(age > 16 and country == "KSA" and rank > 0)  # False

# print(age > 40 or country == "KSA" or rank > 20)  # False
# print(age > 40 or country == "Egypt" or rank > 20)  # True

# print(age > 16)  # True
# print(not age > 16)  # Not True = False


# import requests

# url = "https://api.example.com/endpoint"

# headers = {
#     "Authorization": "Token my_token",
#     "Content-Type": "application/json",
# }

# payload = {
#     "param1": "value1",
#     "param2": "value2",
# }

# response = requests.get(url, headers=headers, params=payload)

# if response.status_code == 200:
#     data = response.json()
#     # Do something with the response data
# else:
#     print("Request failed")


#     %APPDATA%\Code\User\settings.json

from bs4 import BeautifulSoup

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser") 
    
    result = doc.find("option")  
    result = doc.find_all("option") #return all `option` tags  
    print(result) 
    
    Modify attributes of tags
    tag = doc.find("option")
    
    tag['value'] = 'sssss' #chang the content of the attribute `option`
    tag['selected'] = 'ffffff'
    
    tag['color'] = 'blue'   #add new attribute 
    print(tag) 
    
    # Get all attributes (will give them in a dictionary)
    tag = doc.find("option")    
    print(tag.attrs) #return them in a dictionary
    print(tag) 
    
##

    from bs4 import BeautifulSoup
with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser") 