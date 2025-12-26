# DAP_RP


## Install instructions

To set up and install the venv (including dev tools), copy and paste the 
following into your command line that was previously `cd`'d to the root 
of this repository.
```
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .[dev]
```

Once that is done, modify the default interpreter of your IDE to point
to the venv