Tree structure

```
.
├── __main__.py
├── module_a
│   ├── __init__.py
│   ├── submodule_1
│   │   └── __init__.py
│   ├── submodule_2
│   │   └── __init__.py
│   └── submodule_3.py
└── README.md
```

Result

```
Loading module a
---> module_a __package__: module_a 

Loading submodule 1 from relative import . in module a
---> module_a.submodule_1 __package__: module_a.submodule_1 

Loading submodules 2 and 3 from relative import .. in submodule 1
---> module_a.submodule_2 __package__: module_a.submodule_2
---> module_a.submodule_3 __package__: module_a 
```