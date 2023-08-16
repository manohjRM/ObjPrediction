echo " BUILD START"
objiden/Scripts/activate
python pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
objiden/Scripts/deactivate
echo " BUILD END"