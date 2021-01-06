import os
import tarfile

<<<<<<< HEAD
raw_folder = 'Data/raw_data'

=======
raw_folder = './raw_data/'
os.chdir('Data')
>>>>>>> 375499dc44cc3774237962fff70256cff96b1b9f

for f in os.listdir(raw_folder):
    if f.endswith('.tgz'):
        try:
            tar = tarfile.open(os.path.join(raw_folder, f))
            tar.extractall(raw_folder)
            tar.close()
        except:
            print(f)      
samples = [d for d in os.listdir(raw_folder) if os.path.isdir(os.path.join(raw_folder, d))]
print(len(samples))