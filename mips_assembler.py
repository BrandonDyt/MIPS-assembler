#add, sub, and, or, sll，srl，lw, sw, addi,ori,lui,slt,slti,beq, bne,
# j, jal, jr.
#op rs rt rd shamt func

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
dis_reg_dic={'00000':'$zero',\
			'00001':'$at',\
			'00010':'$v0',\
			'00011':'$v1',\
			'00100':'$a0',\
			'00101':'$a1',\
			'00110':'$a2',\
			'00111':'$a3',\
			'01000':'$t0',\
			'01001':'$t1',\
			'01010':'$t2',\
			'01011':'$t3',\
			'01100':'$t4',\
			'01101':'$t5',\
			'01110':'$t6',\
			'01111':'$t7',\
			'10000':'$s0',\
			'10001':'$s1',\
			'10010':'$s2',\
			'10011':'$s3',\
			'10100':'$s4',\
			'10101':'$s5',\
			'10110':'$s6',\
			'10111':'$s7',\
			'11000':'$t8',\
			'11001':'$t9',\
			'11010':'$k0',\
			'11011':'$k1',\
			'11100':'$gp',\
			'11101':'$sp',\
			'11110':'$fp',\
			'11111':'$ra'}
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

dis_op_dic={'001000':'addi',\
			'001101':'ori',\
			'001100':'andi',\
			'001010':'slti',\
			'001111':'lui',\
			'100011':'lw',\
			'101011':'sw',\
			'000100':'beq',\
			'000010':'j',\
			'000011':'jal',\

			'0x20':'add',\
			'0x22':'sub',\
			'0x24':'and',\
			'0x25':'or',\
			'0x27':'nor',\
			'0x2a':'slt',\
			'0x0':'sll',\
			'0x2':'srl',\
			'000101':'bne',\
			'0x8':'jr'
			}

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
	return bin(int(eval(n)))[bin(int(eval(n))).index('b')+1:]


def mips_add(l):
	"add rd, rs, rt | rd=rs+rt"


	op=l[0]
	rd=l[1]
	rs=l[2]
	rt=l[3]
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + reg_dic[rd] + '00000' + func_dic[op]
	result_1.append(s)
	return;

def mips_sub(l):
	"sub rd, rs, rt | rd=rs-rt"


	op=l[0]
	rd=l[1]
	rs=l[2]
	rt=l[3]
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + reg_dic[rd] + '00000' + func_dic[op]
	result_1.append(s)
	return;

def mips_and(l):
	"and rd, rs, rt | rd=rs&rt"


	op=l[0]
	rd=l[1]
	rs=l[2]
	rt=l[3]
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + reg_dic[rd] + '00000' + func_dic[op]
	result_1.append(s)
	return;

def mips_or(l):
	"or rd, rs, rt | rd=rs|rt"


	op=l[0]
	rd=l[1]
	rs=l[2]
	rt=l[3]
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + reg_dic[rd] + '00000' + func_dic[op]
	result_1.append(s)
	return;

def mips_sll(l):
	"sll rd, rt, sa | rd=rt<<sa"


	op=l[0]
	rd=l[1]
	rt=l[2]
	sa=bin(eval(l[3]))[2:]
	sa=zero_extend(sa,5)
	s = op_dic[op] + '00000' + reg_dic[rt] + reg_dic[rd] + sa + func_dic[op]
	result_1.append(s)
	return;

def mips_srl(l):
	"srl rd, rt, sa | rd=rt>>sa"


	op=l[0]
	rd=l[1]
	rt=l[2]
	sa=bin(eval(l[3]))[2:]
	sa=zero_extend(sa,5)
	s = op_dic[op] + '00000' + reg_dic[rt] + reg_dic[rd] + sa + func_dic[op]
	result_1.append(s)
	return;

def mips_lw(l):
	"lw $rt offset($rs)"


	op=l[0]
	rt=l[1]
	l[2]=l[2].replace('(',' ').replace(')',' ').split()
	rs=l[2][1]
	offset=l[2][0]
	offset = deci2bin(offset)
	offset = zero_extend(offset,16)
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + offset
	result_1.append(s)
	return;

def mips_sw(l):
	"sw $rt offset($rs)"


	op=l[0]
	rt=l[1]
	l[2]=l[2].replace('(',' ').replace(')',' ').split()
	rs=l[2][1]
	offset=l[2][0]
	offset = deci2bin(offset)
	offset = zero_extend(offset,16)
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + offset
	result_1.append(s)
	return;

def mips_addi(l):
	"addi rt, rs, imme | rt=rs+imme"

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
	result_1.append(s)
	return;

def mips_ori(l):
	"ori rt, rs, imme | rt=rs+imme"

	op=l[0]
	rt=l[1]
	rs=l[2]

	imme=l[3]
	imme=deci2bin(imme)
	imme=zero_extend(imme, 16)

	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + imme
	result_1.append(s)
	return;

def mips_andi(l):
	"andi rt, rs, imme | rt=rs+imme"

	op=l[0]
	rt=l[1]
	rs=l[2]

	imme=l[3]
	imme=deci2bin(imme)
	imme=zero_extend(imme, 16)

	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + imme
	result_1.append(s)
	return;

def mips_lui(l):
	"lui $rt imme"

	op=l[0]
	rt=l[1]

	imme=l[2]
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
	result_1.append(s)
	return;

def mips_slt(l):
	"slt rd rs rt"
	op=l[0]
	rd=l[1]
	rs=l[2]
	rt=l[3]
	s = op_dic[op] + reg_dic[rs] + reg_dic[rt] + reg_dic[rd] +'00000' + func_dic[op]
	result_1.append(s)
	return;

def mips_slti(l):
	"slti rt rs imme"
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
	result_1.append(s)
	return;

def mips_beq(l, bef):
	"beq rs, rt, imme"

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
	result_1.append(s)
	return

def mips_bne(l, bef):
	"bne rs, rt, imme"

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
	result_1.append(s)
	return
def mips_j(l, bef):
	"j target"	
	op=l[0]
	temp_target=l[1]

	if temp_target in label_list:
		target = label_queue[label_list.index(temp_target)]					
	else:
		target=eval(temp_target)//4

	target=deci2bin(str(target))
	target=zero_extend(target, 26)
	s = op_dic[op] + target
	result_1.append(s)
	return;

def mips_jal(l, bef):
	"jal target"	
	op=l[0]
	temp_target=l[1]

	if temp_target in label_list:
		target = label_queue[label_list.index(temp_target)]						
	else:
		target=eval(temp_target)/4

	target=deci2bin(str(target))
	target=zero_extend(target, 26)
	s = op_dic[op] + target
	result_1.append(s)
	return;

def mips_jr(l):
	"jr rs"	
	op=l[0]
	rs=l[1]

	s=op_dic[op] + reg_dic[rs] + '00000' + '00000' + '00000' + func_dic[op]
	result_1.append(s)
	return; 

def mips_dis_i(l):
	"i format, op rs rt imme"
	rs= dis_reg_dic[l[6:11]]
	rt= dis_reg_dic[l[11:16]]
	imme= str(int(l[16:], 2))
	op= dis_op_dic[l[:6]]
	s= op +' '+ rt + ', '

	if op=='sw' or op=='lw':
		s=s + '{:d}({:s})'.format(int(imme),rs)
	elif op=='lui':
		s=s+ imme
	else:
		s=s+rs+', '+imme
	result_2.append(s)
	return

def mips_dis_r(l):
	"r format, op rd rs rt/sa"
	rs=dis_reg_dic[l[6:11]]
	rt=dis_reg_dic[l[11:16]]
	rd=dis_reg_dic[l[16:21]]
	sa=l[21:26]
	func=str(hex(int(l[26:],2)))
	op=dis_op_dic[func]

	if op=='sll' or op=='srl':
		s=op + ' ' + rd + ', ' + rt + ', '+str(int(sa,2))
	elif op=='jr':
		s=op + ' ' + rs
	else:
		s=op + ' ' + rd + ', ' + rs + ', '+ rt
	result_2.append(s)
	return

def mips_dis_j(l):
	"j format, op target"
	op=dis_op_dic[l[:6]]
	target=str(int(l[6:],2)*4)

	s=op+' '+target

	result_2.append(s)
	return
#main
mode=input('''please input the program mode:
1: assembler
2: disassembler
''')
if mode=='1':
	fin_name=input('please input the file name to assemble: ')
	fin=open(fin_name,'r')
	fout_name=input('please input the file name to store the result')
	fout=open(fout_name,'w')
	row=fin.read().lower().split('\n')

	label_list=list()
	label_queue=list()

	for i in range(0, len(row)):
		if i =='' or i is None:
			continue
		row[i]=row[i].replace(',',' ').replace(':',' ').split()
		#print(sentence)
		name=row[i][0]
		if (not name in op_dic) and (not name in label_list):
			label_list.append(name)
			label_queue.append(i)
			row[i]=row[i][1:]
	result_1=[]
	for j in range(0, len(row)):
		sentence=row[j]
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
			mips_slti(sentence)
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
#for i in result_1:
#	print(hex(int('0b'+i,2)))
	for i in result_1:
		#fout.write(i+'\n')
		temp=hex(int(i,2))[2:]
		fout.write(zero_extend(temp,8)+'\n')



elif mode=='2':
	fin_name=input('please input the file name to disassemble: ')
	fin=open(fin_name,'r')
	fout_name=input('please input the file name to store the result')
	fout=open(fout_name,'w')
	row=fin.read().split('\n')
	result_2=[]
	for i in row:
		if i is None or i=='':
			continue
		i=zero_extend(bin(int(i,16))[2:],32)
		op=i[:6]
		if op=='001000' or op=='001101' or op=='001100' or op=='001010' or op=='001111' or op=='100011' or op=='101011' or op=='000100' or op=='000101':
			mips_dis_i(i)
		elif op=='000010' or op=='000011':
			mips_dis_j(i)
		elif op=='000000':
			mips_dis_r(i)

	for i in result_2:
		fout.write(i+'\n')