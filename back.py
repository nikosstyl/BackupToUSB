from genericpath import getctime
import shutil
from datetime import datetime
import os

def backup() :
	print('Welcome to backup!\n');
	indir = # Directory to be zipped!
	loc = open('default.location', 'r');
	loc.seek(0, 0);
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
	tempdir = # A basic temporary directory
	shutil.make_archive(tempdir, 'zip', indir);
	if os.path.exists(outdir) == True:
		os.rename(outdir, outdir[0:6]+'(1).zip')
		os.remove(outdir[0:6]+'(1).zip')

	shutil.move(tempdir+'.zip', 'D:/') # This has to be fixed
	return (True);


while 1:
	temp = backup();
	if temp == True:
		exit();
