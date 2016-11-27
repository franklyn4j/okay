import shutil
import datetime
import os
index=1
bk_path="/tmp"
def do_remove_line(line):
	if len(line) > 1:
		count = 0
		while line[-2-count] == " " or line[-2-count]=="	":
			count += 1
			if -2-count <= -len(line)-1: 
				break
		return line[0:-1-count]+line[-1]
	else:
		return line
def do_backup(meat,src_file,dest_path):
	now = datetime.datetime.now()	
	str_now = now.strftime("%H%M%S")+"_"+str(index)
	line="\""+src_file+"\"::"+str_now+"\n"
	
	dest_file = os.path.join(dest_path,str_now)
	shutil.copy(src_file,dest_file)
	meat.write(line)
	
def test_backup():
	file=open("meta","w")
	do_backup(file,"h1","bk")
	file.close()	

def do_remove(filename):
	bk_file=os.path.join(bk_path,"tmp_back_now")
	file=open(filename,"r")
	file2 = open(bk_file,"w")
	cnt=0
	blank_line_count = 0
	for line in file.readlines():
		if len(line) > 1:
			if line[-2]=="	" or line[-2]==" ":
				line = do_remove_line(line)
		if len(line) > 1:
			for i in range(0,blank_line_count):
				file2.write(line[-1])
			file2.write(line)
			blank_line_count = 0
		else:
			blank_line_count += 1
		cnt += 1
	file.close()
	file2.close()
	os.remove(filename)
	shutil.copy(bk_file,filename)
	os.remove(bk_file)

def remove(files):
	if os.path.exists(bk_path) and os.path.isdir(bk_path):
		
		time_now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")	
		bk_dir = os.path.join(bk_path,time_now)
		os.mkdir(bk_dir)
		meta=os.path.join(bk_dir,"meta")
		print meta
		file_meta = open(meta,"w")
		for file in files:
			if os.path.exists(file) and os.path.isfile(file):
				do_backup(file_meta,file,bk_dir)
				do_remove(file)
			else:
				print "file : "+file+" does not exist"
		file_meta.close()
	else:
		print "buckup dir does not exist:  "+bk_path
def remove_tail_space():
	file = os.path.abspath("data")
	remove((file,))
remove_tail_space()
