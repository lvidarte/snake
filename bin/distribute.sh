#!/bin/bash

PY_ENV="env"

rm -rf build dist

python3 setup.py sdist bdist_wheel

whl_file=$(ls dist/*.whl)

# Create env if not exist
if [[ ! -d "$PY_ENV" ]]; then
  echo "Python environment ${PY_ENV} does not exist! creating..."
  python3 -m venv $PY_ENV
  source $PY_ENV/bin/activate
  pip install --upgrade pip
  pip install --no-cache-dir twine
else
  source $PY_ENV/bin/activate
fi

echo
echo -n "Do you want to upload the ${whl_file} file? (y/n): " 
read answer
if [[ "$answer" == "y" ]]; then
    twine upload $whl_file
else
    echo "Aborted"
fi