import zipfile
import os

if not os.path.isdir('extracted'):
	os.mkdir('extracted')

def unzip(source_filename, dest_dir):
	with zipfile.ZipFile(source_filename) as zf:
		zf.extractall(dest_dir)

for filename in os.listdir(os.getcwd()):
	if filename[-4:] == '.zip':
		unzip(filename, os.path.join(os.getcwd(), 'extracted'))