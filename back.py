from genericpath import getctime
import shutil
import platform
from datetime import datetime
import os

def backup() :
	indir = # Directory to be zipped!
	loc = open('default.location', 'r');
	loc.seek(0, 0);
	# outdir format has to be like this: D:/path/to/file.zip
	outdir = str(loc.read());
	loc.close();
	if os.path.exists(outdir) == False:
		print('\nUSB NOT found!');
		deb = open('debug.txt', 'w');
		deb.write('%s' %datetime.now());
		deb.write('\nUSB NOT FOUND!\n');
		deb.close();
		print('Default output location: ', end='');
		print('%s'%outdir);
		print('Specify output .zip file (or leave blank for default): ', end='')
		new = input();
		if new:
			nn = open('default.location', 'w');
			nn.seek(0,0);
			nn.write(new);
			nn.close
		return(False);

	print('USB found!');
	print('-------------- Info --------------')
	tempdir = # A basic temporary directory.
	shutil.make_archive(tempdir, 'zip', indir);
	print('\tFolder zipped in temporary location')
	if os.path.exists(outdir) == True:
		os.rename(outdir, outdir[0:outdir.find('.zip')]+'(1).zip')
		print('\tRenamed existing backup zip file')
		mflag = True

	# shutil.move(tempdir+'.zip', outdir.replace(filename, '')) # Replace filename with your actual output filename. E.g., filename='MyZip.zip'
	shutil.move(tempdir+'.zip', outdir[0:outdir.find('.zip')])
	print('\tCopied new backup zip file')
	if mflag == True:
		os.remove(outdir[0:outdir.find('.zip')]+'(1).zip')
		print('\tRemoved old backup zip file')
	print('--------------- End --------------')
	return (True);


while 1:
	if platform.system() == 'Windows':
		os.system('clc') # Assuming that it has been called from cmd
	elif platform.system() == 'Linux':
		os.system('clear')
	temp = backup();
	if temp == True:
		exit();
