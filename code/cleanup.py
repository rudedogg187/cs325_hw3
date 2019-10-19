import os



def pyc():
  cwd = os.getcwd()

  files = os.listdir(cwd)


  for f in files:
    if f.split(".")[-1] == "pyc":
      os.remove(f)

def main():
  pyc()

if __name__ == "__main__":
  main()
