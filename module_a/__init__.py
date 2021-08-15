print("Loading module a")
print(f"---> {__name__} __package__:", __package__, "\n")
print("Loading submodule 1 from relative import . in module a")
from . import submodule_1
