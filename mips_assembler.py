#add, sub, and, or, sll，srl，lw, sw, addi,ori,lui,slt,slti,beq, bne,
# j, jal, jr.
#op rs rt rd shamt func
op_dic={'add':'000000',\
		'addi':'001000',\
		'sub':'000000',\
		'and':'000000',\
		'or':'000000',\
		'ori':'001101',\
		'andi':'001100',\
		'nor':'000000',\
		'sll':'000000',\
		'srl':'000000',\
		'lw':'100011',\
		'sw':'101011',\
		'lui':'001111',\
		'slt':'000000',\
		'slti':'001010',\
		'beq':'000100',\
		'bne':'000101',\
		'j':'000010',\
		'jal':'000011',\
		'jr':'000000'}

func_dic={'add':'100000',\
		'sub':'100010',\
		'and':'100100',\
		'or':'100101',\
		'nor':'100111',\
		'sll':'000000',\
		'srl':'000010',\
		'slt':'101010',\
		'jr':'001000'}

reg_dic={'$zero':'00000',\
		'$at':'00001',\
		'$v0':'00010',\
		'$v1':'00011',\
		'$a0':'00100',\
		'$a1':'00101',\
		'$a2':'00110',\
		'$a3':'00111',\
		'$t0':'01000',\
		'$t1':'01001',\
		'$t2':'01010',\
		'$t3':'01011',\
		'$t4':'01100',\
		'$t5':'01101',\
		'$t6':'01110',\
		'$t7':'01111',\
		'$s0':'10000',\
		'$s1':'10001',\
		'$s2':'10010',\
		'$s3':'10011',\
		'$s4':'10100',\
		'$s5':'10101',\
		'$s6':'10110',\
		'$s7':'10111',\
		'$t8':'11000',\
		'$t9':'11001',\
		'$k0':'11010',\
		'$k1':'11011',\
		'$gp':'11100',\
		'$sp':'11101',\
		'$fp':'11110',\
		'$ra':'11111'}
def remove_comma(l):
	"remove ',' "
	newl=[]
	for k in l:
		if ',' in k:
			temp=list(k)
			temp.remove(',')
			k=''.join(i for i in temp)
			newl.append(k)
		else:
			newl.append(k)
	return newl;

def zero_extend(s, num):
	"extend an unsigned number to num's bits"
	while (len(s)<num):
		s = '0' + s
	return s;

def signed_extend(s, num):
	"signed extend"
	while (len(s)<num):
		s= s[0] + s
	return s;


def deci2bin(n):
	"change decimal string to binary"
	return bin(eval(n))[bin(eval(n)).index('b')+1:]


def mips_add(l):
	"add rd, rs, rt | rd=rs+rt"

	l = remove_comma(l);
	op=l[0]
	rd=l[1]
	rs=l[2]
	rt=l[3]
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + reg_dic[rd] + '00000' + func_dic[op]
	result.append(s)
	return;

def mips_sub(l):
	"sub rd, rs, rt | rd=rs-rt"

	l = remove_comma(l);
	op=l[0]
	rd=l[1]
	rs=l[2]
	rt=l[3]
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + reg_dic[rd] + '00000' + func_dic[op]
	result.append(s)
	return;

def mips_and(l):
	"and rd, rs, rt | rd=rs&rt"

	l = remove_comma(l);
	op=l[0]
	rd=l[1]
	rs=l[2]
	rt=l[3]
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + reg_dic[rd] + '00000' + func_dic[op]
	result.append(s)
	return;

def mips_or(l):
	"or rd, rs, rt | rd=rs|rt"

	l = remove_comma(l);
	op=l[0]
	rd=l[1]
	rs=l[2]
	rt=l[3]
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + reg_dic[rd] + '00000' + func_dic[op]
	result.append(s)
	return;

def mips_sll(l):
	"sll rd, rt, sa | rd=rt<<sa"

	l = remove_comma(l);
	op=l[0]
	rd=l[1]
	rt=l[2]
	sa=bin(eval(l[3]))[2:]
	s = op_dic[op] + '00000' + reg_dic[rt] + reg_dic[rd] + sa + func_dic[op]
	result.append(s)
	return;

def mips_srl(l):
	"srl rd, rt, sa | rd=rt>>sa"

	l = remove_comma(l);
	op=l[0]
	rd=l[1]
	rt=l[2]
	sa=bin(eval(l[3]))[2:]
	s = op_dic[op] + '00000' + reg_dic[rt] + reg_dic[rd] + sa + func_dic[op]
	result.append(s)
	return;

def mips_lw(l):
	"lw $rt offset($rs)"

	l = remove_comma(l);
	op=l[0]
	rt=l[1]
	reg_index=l[2].index('$')
	rs=l[2][ reg_index : reg_index+3 ]

	offset = l[2][0:i-1]
	offset = deci2bin(offset)
	offset = zero_extend(offset,16)
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + offset
	result.append(s)
	return;

def mips_sw(l):
	"sw $rt offset($rs)"

	l = remove_comma(l);
	op=l[0]
	rt=l[1]
	reg_index=l[2].index('$')
	rs=l[2][ reg_index : reg_index+3 ]

	offset = l[2][0:i-1]
	offset = deci2bin(offset)
	offset = zero_extend(offset,16)
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + offset
	result.append(s)
	return;

def mips_addi(l):
	"addi rt, rs, imme | rt=rs+imme"

	l = remove_comma(l)
	op=l[0]
	rt=l[1]
	rs=l[2]

	imme=l[3]
	if eval(imme)>0:
		imme=deci2bin(imme)
		imme='0'+imme;
		if (len(imme)>16):
			print('imme of addi is overflow!')
			exit()
		imme=signed_extend(imme, 16)
	else:
		imme=deci2bin(imme)
		imme=signed_extend(imme, 16)

	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + imme
	result.append(s)
	return;

def mips_ori(l):
	"ori rt, rs, imme | rt=rs+imme"

	l = remove_comma(l)
	op=l[0]
	rt=l[1]
	rs=l[2]

	imme=l[3]
	imme=deci2bin(imme)
	imme=zero_extend(imme, 16)

	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + imme
	result.append(s)
	return;

def mips_andi(l):
	"andi rt, rs, imme | rt=rs+imme"

	l = remove_comma(l)
	op=l[0]
	rt=l[1]
	rs=l[2]

	imme=l[3]
	imme=deci2bin(imme)
	imme=zero_extend(imme, 16)

	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + imme
	result.append(s)
	return;

def mips_lui(l):
	"lui $rt imme"

	l = remove_comma(l)
	op=l[0]
	rt=l[1]

	imme=l[3]
	if eval(imme)>0:
		imme=deci2bin(imme)
		imme='0'+imme;
		if (len(imme)>16):
			print('imme of addi is overflow!')
			exit()
		imme=signed_extend(imme, 16)
	else:
		imme=deci2bin(imme)
		imme=signed_extend(imme, 16)

	s = op_dic[op] + '00000' + reg_dic[rt] + imme
	result.append(s)
	return;

def mips_slt(l):
	"slt rd rs rt"

	l= remove_comma(l)
	op=l[0]
	rd=l[1]
	rs=l[2]
	rt=l[3]

	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + reg_dic[rd] +'00000' + func_dic[op]
	result.append(s)
	return;

def mips_slti(l):
	"slti rt rs imme"

	l= remove_comma(l)
	op=l[0]
	rt=l[1]
	rs=l[2]

	imme=l[3]
	if eval(imme)>0:
		imme=deci2bin(imme)
		imme='0'+imme;
		if (len(imme)>16):
			print('imme of addi is overflow!')
			exit()
		imme=signed_extend(imme, 16)
	else:
		imme=deci2bin(imme)
		imme=signed_extend(imme, 16)

	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + imme
	result.append(s)
	return;

def mips_beq(l, bef):
	"beq rs, rt, imme"

	l= remove_comma(l)
	op=l[0]
	rs=l[1]
	rt=l[2]

	temp_imme=l[3]
	if temp_imme in label_list:
		imme = label_queue[label_list.index(temp_imme)] - ( bef + 1 )
	else:
		imme = eval(temp_imme)

	if imme>0:
		imme=deci2bin(str(imme))
		imme='0'+imme;
		if (len(imme)>16):
			print('imme of addi is overflow!')
			exit()
		imme=signed_extend(imme, 16)
	else:
		imme=deci2bin(str(imme))
		imme=signed_extend(imme, 16)

	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + imme
	result.append(s)
	return

def mips_bne(l, bef):
	"bne rs, rt, imme"

	l= remove_comma(l)
	op=l[0]
	rs=l[1]
	rt=l[2]

	temp_imme=l[3]
	if temp_imme in label_list:
		imme = label_queue[label_list.index(temp_imme)] - ( bef + 1 )
	else:
		imme = eval(temp_imme)

	if imme>0:
		imme=deci2bin(str(imme))
		imme='0'+imme;
		if (len(imme)>16):
			print('imme of addi is overflow!')
			exit()
		imme=signed_extend(imme, 16)
	else:
		imme=deci2bin(str(imme))
		imme=signed_extend(imme, 16)

	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + imme
	result.append(s)
	return
def mips_j(l, bef):
	"j target"

	l=remove_comma(l)
	op=l[0]
	temp_target=l[1]

	if temp_target in label_list:
		pass						##remains to be supply
	else:
		target=eval(temp_target)//4

	target=deci2bin(str(target))
	target=zero_extend(target, 26)
	s = op_dic[op] + target
	result.append(s)
	return;

def mips_jal(l, bef):
	"jal target"

	l=remove_comma(l)
	op=l[0]
	temp_target=l[1]

	if temp_target in label_list:
		pass						##remains to be supply
	else:
		target=eval(temp_target)/4

	target=deci2bin(str(target))
	target=zero_extend(target, 26)
	s = op_dic[op] + target
	result.append(s)
	return;

def mips_jr(l):
	"jr rs"

	l=remove_comma(l)
	op=l[0]
	rs=l[1]

	s=op_dic[op] + reg_dic[rs] + '00000' + '00000' + '00000' + func_dic[op]
	result.append(s)
	return; 


#main
fin=open('test.txt','r')

raw=fin.read().lower().split('\n')

label_list=list()
label_queue=list()

for i in range(0, len(raw)):
	sentence=raw[i].split()
	#print(sentence)
	if sentence[0][-1]==':':
		name=sentence[0][0:-1]
		if not (name in label_list):
			label_list.append(name)
			label_queue.append(i)
			raw[i]=raw[i][raw[i].index(':') + 1 : -1 ]
result=[]
for j in range(0, len(raw)):
	sentence=raw[j].split()
	#print(sentence)
	if sentence[0]=='add':
		mips_add(sentence)
	elif sentence[0]=='addi':
		mips_addi(sentence)
	elif sentence[0]=='sub':
		mips_sub(sentence)
	elif sentence[0]=='and':
		mips_and(sentence)
	elif sentence[0]=='or':
		mips_or(sentence)
	elif sentence[0]=='ori':
		mips_ori(sentence)
	elif sentence[0]=='andi':
		mips_andi(sentence)
	elif sentence[0]=='sll':
		mips_sll(sentence)
	elif sentence[0]=='srl':
		mips_srl(sentence)
	elif sentence[0]=='lw':
		mips_lw(sentence)
	elif sentence[0]=='sw':
		mips_sw(sentence)
	elif sentence[0]=='lui':
		mips_lui(sentence)
	elif sentence[0]=='slt':
		mips_slt(sentence)
	elif sentence[0]=='slti':
		mips_slt(sentence)
	elif sentence[0]=='beq':
		mips_beq(sentence,j)
	elif sentence[0]=='bne':
		mips_bne(sentence,j)
	elif sentence[0]=='j':
		mips_j(sentence,j)
	elif sentence[0]=='jal':
		mips_jal(sentence,j)
	elif sentence[0]=='jr':
		mips_jr(sentence)
#for i in result:
#	print(hex(int('0b'+i,2)))
for i in result:
	temp=hex(int(i,2))[2:]
	print(zero_extend(temp,8))