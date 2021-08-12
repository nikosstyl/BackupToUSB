from time import sleep
from genericpath import getctime
from multiprocessing.context import Process
import shutil
from datetime import datetime
import os
import platform
from pathlib import Path
import progressbar
from progressbar.bar import ProgressBar
from six import assertRegex

def backup() :
	"""
	This function zips a folder to a USB and checks for errors.
	In order to work for the first time, a file with no space must be created at the directory
	specified by the user on default.location file. 
	For example, if you want to zip a folder into D:/path/to/folder.zip, 
	you must open default.location file and write D:/path/to/folder.zip in it
	( NOTE: YOU MUST OLNY WRITE THIS, OTHERWISE IT WON'T WORK ), and then create a dummy file
	at that directory (in the above case the directory is D:/path/to/) with the same name as in
	default.location file (again in the above case, the filename is folder.zip).
	"""
	print('Welcome to my backup!\n');
	indir = # Directory to be zipped
	loc = open('default.location', 'r');
	loc.seek(0, 0);
	# outdir format has to be like this: D:/path/to/Test.zip
	outdir = str(loc.read());
	loc.close();
	if os.path.isfile(outdir) == False:
		print('\nUSB NOT found!')
		print('Default output location: ', end='');
		print('%s'%outdir);
		print('Specify output file location (or leave blank for default): ', end='')
		new = input();
		if new:
			nn = open('default.location', 'w');
			nn.seek(0,0);
			nn.write(new);
			nn.close
		return(False);

	print('USB found!');
	print('-------------- Info --------------')
	tempdir = # A basic temporary directory. If on Linux, mktemp -d should do the trick.
	root_directory = Path(indir)
	totsize = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())
	print ('\tZipping folder in temporary location')
	p = Process(target=finfo, args=(tempdir+'.zip', totsize,))
	p.start()
	w = Process(target=zip,args=(tempdir,indir,))
	w.start();
	w.join();
	p.join()
	print('\tFolder zipped in temporary location')
	mflag = os.path.isfile(outdir)
	if mflag == True:
		os.rename(outdir, outdir[0:outdir.find('.zip')]+'_old.zip')
		print('\tRenamed existing backup zip file')
	print('\tCopying new backup zip file')
	p = Process(target=finfo, args=(outdir, os.path.getsize(tempdir+'.zip',)))
	p.start()
	w = Process(target=cp, args=(tempdir+'.zip', outdir,))
	w.start()
	w.join()
	p.join()
	print('\tCopied new backup zip file')
	if mflag == True:
		os.remove(outdir[0:outdir.find('.zip')]+'_old.zip')
		print('\tRemoved old backup zip file')
	
	print('--------------- End --------------')
	return (True);

def cp(start, out):
	shutil.move(start, out)

def zip(tempdir, indir):
	shutil.make_archive(tempdir, 'zip', indir);

def finfo(f, totsize):
	widgets=[
		' [', progressbar.widgets.DataSize(), '] ',
		progressbar.Bar(),
		' (', progressbar.Timer(), ') ',
	]
	i=0
	while os.path.exists(f) == False:
		sleep(1)
	with progressbar.ProgressBar(max_value=totsize, widgets=widgets) as bar:
		while (1):
			old = os.path.getsize(f)
			sleep(1)
			new = os.path.getsize(f)
			if old != new:
				bar.update(new)
			elif old == new and new>0.8*totsize:
				break
			i+=1;
		

if __name__ ==  '__main__':
	while 1:
		if platform.system() == 'Windows':
			os.system('cls'); # Supposing running from cmd
		elif platform.system() == 'Linux':
			os.system('clear');
		temp = backup();
		if temp == True:
			exit();
