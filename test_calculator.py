from calculator import add, subtract, multiply, divide, CircleArea

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_subtract():
	assert subtract(7,3) == 4

def test_multiply():
	assert multiply(5,3) == 15

def test_negative_addition():
	#arrange
	a= 7
	b= -2

	#act
	result = add(a,b)

	#assert
	assert result == 5

def test_circleArea():
	assert CircleArea(-4) == "Error"
