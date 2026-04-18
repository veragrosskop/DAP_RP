# Creating a venv and installing packages

This assumes you already cloned a repository, please check out [Cloning a repository](cloning.md)
for how to do so.

## Creating venv

We start by going into project dir.

```bash
cd <repo_path>
python3 -m venv .raspi-venv
```

## Activate the venv

`source .raspi-venv/bin/activate`

You should now see a commandline along these lines:

```bash
(.raspi-venv) pizero@rapsberrypi:~/projects/<project_name> $
```

This tells you, you've successfully activated the venv. To now install
dependencies you can install the requirements:

```bash
pip install -r requirements.txt
```

And you're done!

> [!IMPORTANT]
> The raspberry pi has `/tmp` as the temporary directory which by default is only about 200MB. 
> This can become a problem especially when trying to install larger packages like pyside6
> as pip will use the `/tmp` partition for all intermediate data.
> To mitigate this we can tell linux to use a different tmp dir such as `/var/tmp` for these
> caches.
> Below you can find the full command for install pip packages like this.
> ```bash
> export TMPDIR=/var/tmp
> pip --cache-dir /var/tmp install -r requirements.tx
> ```