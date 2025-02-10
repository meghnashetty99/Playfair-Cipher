def gen_mat(key):
	key=key.upper().replace("J","I")
	key="".join(dict.fromkeys(key))
	alpha="ABCDEFGHIKLMNOPQRSTUVWXYZ"
	matrix=[c for c in key if c in alpha]
	for c in alpha:
		if c not in matrix:
			matrix.append(c)
	return [matrix[i:i+5] for i in range(0,25,5)]

def getpos(matrix,char):
	for row in range(5):
		for col in range(5):
			if matrix[row][col]==char:
				return row,col
	return None

def encryptplain(text,key):
	matrix=gen_mat(key)
	text=text.upper().replace("J","I").replace(" ","")
	pairs=[]
	i=0
	while i<len(text):
		a=text[i]
		b=text[i+1] if i+1<len(text) else 'X'
		if a==b:
			pairs.append((a,'X'))
			i=i+1
		else:
			pairs.append((a,b))
			i=i+2
	et=""
	for a,b in pairs:
		r1,c1=getpos(matrix,a)
		r2,c2=getpos(matrix,b)
		if r1==r2:
			et+=matrix[r1][(c1+1)%5]+matrix[r2][(c2+1)%5]
		elif c1==c2:
			et+=matrix[(r1+1)%5][c1]+matrix[(r2+1)%5][c2]
		else:
			et+=matrix[r1][c2]+matrix[r2][c1]
	return et

def decryptcip(cip,key):
	matrix=gen_mat(key)
	cip=cip.upper().replace(" ","")
	pairs=[(cip[i],cip[i+1]) for i in range(0,len(cip),2)]
	dt=""
	for a,b in pairs:
		r1,c1=getpos(matrix,a)
		r2,c2=getpos(matrix,b)
		if r1==r2:
			dt+=matrix[r1][(c1-1)%5]+matrix[r2][(c2-1)%5]
		elif c1==c2:
			dt+=matrix[(r1-1)%5][c1]+matrix[(r2-1)%5][c2]
		else:
			dt+=matrix[r1][c2]+matrix[r2][c1]
	return dt


key="Monarchy"
plaintext="Instruments"
ciphertext=encryptplain(plaintext,key)
print("Encrypted text is :\n",ciphertext)
detext=decryptcip(ciphertext,key)
print("Decrypted text is :\n",detext)
