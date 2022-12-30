# use within Dockerfile to run the full flow

pip install -r requirements.txt
pip install -e .
sh scripts/setup_dirs.sh
python scripts/train_model.py
