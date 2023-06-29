import os
import sys
import shutil
import glob


def create_dir(dir):
    # create 5 text files
    os.mkdir(dir)
    for i in range(5):
        file = open(dir + '/' + str(i) + '.txt', 'w')
        file.write('Hello World')
        file.close()
    # create 5 subdirectories
    for i in range(5):
        os.mkdir(dir + '/' + str(i))
    # create 5 text files in each subdirectory
    for i in range(5):
        for j in range(5):
            file = open(dir + '/' + str(i) + '/' + str(j) + '.txt', 'w')
            file.write('Hello World')
            file.close()


def clear_pip_cache():
    os.system('pip cache remove *')


def clear_conda_cache():
    os.system('conda clean --all')

def stop_sql():
    os.system('mysqladmin -u root shutdown -p')


def clean_temp_files(dir):
    for root, dirs, files in os.walk(dir):
        for f in files:
            try:
                os.unlink(os.path.join(root, f))
            except:
                pass
        for d in dirs:
            try:
                shutil.rmtree(os.path.join(root, d))
            except:
                pass


def clear_all():
    clear_pip_cache()
    clear_conda_cache()
    stop_sql()
    temp_dirs = [r'C:\Users\rajat\AppData\Local\Temp',
                 r'C:\Windows\Temp', r'C:\Users\rajat\AppData\Roaming\Code\Cache']
    for dir in temp_dirs:
        clean_temp_files(dir)


if __name__ == '__main__':
    clear_all()
