from dtu import setup

# see 'module available' on server for newest python version
setup(
  f"https://github.com/MrCogito/Deep_learning_2023.git",
  python="3.10.12",
  packages=[
    "torch", 
    "torchvision", 
  ]
)