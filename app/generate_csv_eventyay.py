#!usr/bin/python3
try:
    from urllib.request import urlopen
except Exception:
    from urllib2 import urlopen
import json
import os
import sys

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
MAX_STRING = "chaftsladen Potsdam (F"


def tocsv(url_eventyay, filename):
    with urlopen(url_eventyay) as url:
        data = json.loads(url.read().decode(url.info().get_param('charset') or 'utf8'))
        speakers = data['speakers']
        with open(os.path.join(UPLOAD_FOLDER, filename), "w+") as f:
            for speaker in speakers:
                fields = [speaker[field] for field in "name organisation website twitter facebook github linkedin position".split() if speaker[field]]
                i = 0
                while i < len(fields):
                    field = fields[i]
                    for s in ["http://", "https://", "www.", ""]:
                        if field.startswith(s):
                            field = field[len(s):]
                    field = field.strip("/")
                    t = "twitter.com/"
                    g = "github.com/"
                    if field.startswith(t):
                        field = "@" + field[len(t):]
                    if field.startswith(g):
                        field = field[len(g):]

                    if len(field) > len(MAX_STRING):
                        if i < 3:
                            huge_field = field.split()
                            if any(len(sf) > len(MAX_STRING) for sf in huge_field):
                                del fields[i]
                            else:
                                print(huge_field)
                                fields[i:i + 1] = [" ".join(huge_field[:len(huge_field) // 2]), " ".join(huge_field[len(huge_field) // 2:])]
                        else:
                            del fields[i]
                    elif field in fields[i + 1:]:
                        del fields[i]
                    else:
                        fields[i] = field
                        i += 1
                fields += [""] * 4
                f.write("{},{},{},{}\n".format(*fields[:4]))
            f.close()


if __name__ == '__main__':
    tocsv(sys.argv[1], sys.argv[2])
