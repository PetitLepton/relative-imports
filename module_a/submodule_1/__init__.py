print(f"---> {__name__} __package__:", __package__, "\n")
print("Loading submodules 2 and 3 from relative import .. in submodule 1")
from .. import submodule_2, submodule_3

