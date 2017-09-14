# Local

## Dependencies required to run BadgeYay

* Python 3
```sh
sudo apt-get update
sudo apt-get install librsvg2-bin pdftk
```

## Steps

Make sure you have the dependencies mentioned above installed before proceeding further.

*Clone the BadgeYay repository (from the development branch) and ```cd ``` into the directory.
```sh
git clone -b development https://github.com/fossasia/badgeyay
cd badgeyay
```

*Install python requirements. You need to be present in the root directory of the project.

```sh
sudo -H pip install -r requirements.txt
```

*To run the project on a local machine.
```sh
python app/main.py
```


