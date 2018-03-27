# This file contains subroutines which check for Python
# modules/packages on the system and install them if they
# are missing.


def import(package_list,module_list):
# This subroutine performs flexible python package
# importing for 'package_list'
 for package in package_list:
  
  mirror = find_source(package)
  if mirror != None:
   print("The "+package+" python package is not installed on this computer.")
   importlib.util.find_spec("git") is None:
  import urllib.request
  urllib.request.urlretrieve("https://github.com/gitpython-developers/GitPython",str(os.getcwd()+"GitPython"))
  os.chdir(str(os.getcwd()+"GitPython"))
  subprocess.call(str(sys.executable+' setup.py install'))
found = ml4cf_spec is not None