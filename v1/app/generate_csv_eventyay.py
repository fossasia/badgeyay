#!usr/bin/python3
try:
    from urllib.request import urlopen
except Exception:
    from urllib2 import urlopen
import json
import os
import sys

# Get root folder
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# Get Upload Folder
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/badge_backgrounds')
MAX_STRING = "chaftsladen Potsdam (F"


def tocsv(url_eventyay, filename):
    """
    Function to convert to csv format
    :param `url_eventyay` - Eventyay url
    :param `filename` - Destination file name
    """
    with urlopen(url_eventyay) as url:
        # load json, parse it using the utf charset
        data = json.loads(url.read().decode(url.info().get_param('charset') or 'utf8'))
        # get list of speakers in separate vatiable
        speakers = data['speakers']
        with open(os.path.join(UPLOAD_FOLDER, filename), "w+") as f:
        # iterate list one by one
            for speaker in speakers:
                fields = [speaker[field] for field in "name organisation website twitter facebook github linkedin position".split() if speaker[field]]
                i = 0
                while i < len(fields):
                    field = fields[i]
                    for s in ["http://", "https://", "www.", ""]:
                        if field.startswith(s):
                            field = field[len(s):]
                    # remove the / from end
                    field = field.strip("/")
                    t = "twitter.com/"
                    g = "github.com/"
                    # if it's a twitter url
                    if field.startswith(t):
                        # get the @username
                        field = "@" + field[len(t):]
                    # if it's a gituhb url
                    if field.startswith(g):
                        # get the username
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
                # write the file
                f.write("{},{},{},{}\n".format(*fields[:4]))
            # close the file
            f.close()


if __name__ == '__main__':
    tocsv(sys.argv[1], sys.argv[2])
