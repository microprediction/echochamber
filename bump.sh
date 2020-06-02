cp /Users/pcotton/github/echochamber-fake-config/config_private.py /Users/pcotton/github/echochamber/echochamber
cd /Users/pcotton/github/echochamber/
rm /Users/pcotton/github/echochamber/dist/*
python setup.py sdist bdist_wheel
twine upload dist/*
cp /Users/pcotton/github/echochamber-real-config/config_private.py /Users/pcotton/github/echochamber/echochamber

