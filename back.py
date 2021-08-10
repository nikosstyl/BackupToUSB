from time import sleep
from _typeshed import OpenTextModeUpdating
from genericpath import getctime
from multiprocessing.context import Process
import shutil
from datetime import datetime
import os
import platform
from pathlib import Path
import progressbar

def backup() :
	"""
	This function zips a folder to a USB and checks for errors.
	In order to work, a file with no space must be created at the directory
	specified by the user on default.location file. 
	For example, if you want to zip a folder into D:/path/to/folder.zip, 
	you must open default.location file and write D:/path/to/folder.zip in it
	( NOTE: YOU MUST WRITE ONLY THIS, OTHERWISE IT WON'T WORK ), and then create a dummy file
	at that directory (in our case the directory is D:/path/to/) with the same name as in
	default.location file (in our case, the filename is folder.zip).
	"""
	print('Welcome to UTh backup!\n');
	indir = 'C:/Users/Nikos Stylianou/OneDrive - ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣΣΑΛΙΑΣ/UTh'
	loc = open('default.location', 'r');
	loc.seek(0, 0);
	# outdir format has to be like this: D:/path/to/Test.zip
	outdir = str(loc.read());
	loc.close();
	mflag = False;
	if os.path.isfile(outdir) == False:
		# print('Insert USB!')
		print('\nUSB NOT found!');
		deb = open('C:/Users/Nikos Stylianou/.backhelp/debug.txt', 'w');
		deb.write('%s' %datetime.now());
		deb.write('\nUSB NOT FOUND!\n');
		# deb.write('Close Notepad and go to python console for instructions!');
		deb.close();
		# os.system("notepad \"C:/Users/Nikos Stylianou/.backhelp/debug.txt\"")
		print('Default output location: ', end='');
		print('%s'%outdir);
		print('Specify output .zip file (or leave blank for default): ', end='')
		new = input();
		mflag = True;
		# print(new);
		if new:
			nn = open('default.location', 'w');
			nn.seek(0,0);
			nn.write(new);
			nn.close
		return(False);

	print('USB found!');
	print('-------------- Info --------------')
	tempdir = 'C:/Users/Nikos Stylianou/.backhelp/UTh'
	root_directory = Path(indir)
	totsize = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())/1e+9
	print ('\tZipping folder in temporary location')
	p = Process(target=finfo(tempdir+'.zip', totsize))
	p.start()
	shutil.make_archive(tempdir, 'zip', indir);
	p.join()
	print('\tFolder zipped in temporary location')
	if mflag == True:
		os.rename(outdir, outdir[0:outdir.find('.zip')]+'(1).zip')
		print('\tRenamed existing backup zip file')
	print('\tCopying new backup zip file')
	p = Process(target=finfo(outdir, os.path.getsize(tempdir+'.zip')))
	p.start()
	shutil.move(tempdir+'.zip', outdir[0:outdir.find('.zip')])
	p.join()
	print('\tCopied new backup zip file')
	if mflag == True:
		os.remove(outdir[0:outdir.find('.zip')]+'(1).zip')
		print('\tRemoved old backup zip file')
	
	print('--------------- End --------------')
	return (True);


def finfo(f, totsize):
	widgets=[
		' [', progressbar.widgets.DataSize(), '] ',
		progressbar.Bar(),
		' (', progressbar.Timer(), ') ',
	]
	i=0
	with progressbar.ProgressBar(max_value=totsize, widgets=widgets) as bar:
		while (1):
			old = os.path.getsize(f)
			sleep(1.5)
			new = os.path.getsize(f)
			if old != new:
				bar.update(new)
			elif old == new and i!=0:
				break
			i+=1;
		

if __name__ ==  '__main__':
	while 1:
		if platform.system() == 'Windows':
			os.system('clc'); # Supposing running from cmd
		elif platform.system() == 'Linux':
			os.system('clear');
		temp = backup();
		if temp == True:
			exit();
