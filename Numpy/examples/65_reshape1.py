# Knihovna Numpy
#
# Změna tvaru pole

# běžná matice se dvěma řádky a třemi sloupci
a = array([[1, 2, 3], [4, 5, 6]])

# změna tvaru matice na 3x2 prvky
b = reshape(a, (3, 2))

# tisk původní matice
print(a)

# tisk nové matice
print(b)
