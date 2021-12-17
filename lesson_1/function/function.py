# function  用來收納程式碼的

def wash():
	print ('加水')
	print ('加洗衣精')
	print ('旋轉')
wash()  # 使用wash功能

def say_hi():
	print ('hi')
say_hi()

# 參數
def clean(dry):
	print ('加水')
	print ('加洗衣精')
	print ('旋轉')
	if dry:
		print ('烘衣')
clean (True)
clean (False)


def add(x, y):
	print (x + y)
result = add (3, 4)
print(result)

