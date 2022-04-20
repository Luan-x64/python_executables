import os

os.chdir("C:\\Users\\Triild\\Desktop\\FOTOS-PERFIL\\proprias")
#print(os.getcwd())


for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "user_pern_" + str(count)
    print("renomeando ", f)
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
print("Ok...")
