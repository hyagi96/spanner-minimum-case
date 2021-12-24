# Spanner Minimum Case

Edit: This is an error that occurs only when using google-cloud-spanner v3.12.0.

```sh
❯ git clone git@github.com:hyagi96/spanner-minimum-case.git
Cloning into 'spanner-minimum-case'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
Receiving objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
❯ cd spanner-minimum-case/
❯ ./init.sh
+ export PIPENV_VENV_IN_PROJECT=true
+ PIPENV_VENV_IN_PROJECT=true
+ pipenv --python 3.9
Creating a virtualenv for this project...
Pipfile: /[current_dir]/spanner-minimum-case/Pipfile
Using /usr/local/bin/python3.9 (3.9.9) to create virtualenv...
⠧ Creating virtual environment...created virtual environment CPython3.9.9.final.0-64 in 5046ms
  creator CPython3Posix(dest=/[current_dir]/spanner-minimum-case/.venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/[home]/Library/Application Support/virtualenv)
    added seed packages: pip==21.3.1, setuptools==59.2.0, wheel==0.37.0
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /[current_dir]/spanner-minimum-case/.venv
+ pipenv run python -m pip install -U pip
Requirement already satisfied: pip in ./.venv/lib/python3.9/site-packages (21.3.1)
+ pipenv install
Installing dependencies from Pipfile.lock (3e9586)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 29/29 — 00:00:10
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
❯ pipenv shell
Launching subshell in virtual environment...
 . /[current_dir]/spanner-minimum-case/.venv/bin/activate
❯  . /[current_dir]/spanner-minimum-case/.venv/bin/activate
❯ cp .env.example .env
❯ vi .env  # edit .env file
❯ ./run.py  # Create
found column: None
new column will be created: 2021-12-23 13:54:59.096004
❯ ./run.py &> result.log  # Update, and occur an error
```
