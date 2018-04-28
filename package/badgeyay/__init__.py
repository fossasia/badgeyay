"""
Main Source Code for the library : badgeyay
Organisation : FOSSASIA
Author : @yashLadha
"""
import os
import shutil
import tempfile
import traceback

import click

from .utils.custom_color import do_svg2png
from .utils.generate_badges import GenerateBadges
from .utils.merge_badges_class import MergeBadges

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
APP_ROOT = os.getcwd()
LIB_ROOT = os.path.dirname(os.path.abspath(__file__))
GENERATED = os.path.join(APP_ROOT, 'generated')
TEMP_DIR = tempfile.gettempdir() + "/"


def empty_directory():
    """
    Empty the already present directory, and creates new
    directory if not present.
    """
    # Creates 'generated' directory if not exists
    if not os.path.exists(GENERATED):
        os.mkdir(GENERATED)

    for file in os.listdir(TEMP_DIR):
        if file.lower().endswith('.csv') or file.lower().endswith('.png'):
            os.unlink(TEMP_DIR + file)
    if os.path.exists(TEMP_DIR + 'static'):
        shutil.rmtree(TEMP_DIR + 'static')

    # emptying previous files and folders inside the badges folder
    for file in os.listdir(GENERATED):
        file_path = os.path.join(GENERATED, file)
        try:
            if os.path.isfile(file_path):
                # removes the file
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                # removes the directory
                shutil.rmtree(file_path)
        except Exception:
            traceback.print_exc()


def check_config(config):
    joined_path = os.path.join(APP_ROOT, config)
    if os.path.exists(joined_path):
        return True
    else:
        click.echo('Config not exists at the designated path')
        return False


def check_names(names):
    if os.path.isfile(os.path.abspath(os.path.join(APP_ROOT, names))):
        if names.endswith('.csv'):
            return True
        else:
            return False
    else:
        return False


def extract_image_name(img):
    """
    Extracts image name from the absolute path to the
    image file.
    :param img: Absolute path to the image file
    :return: image name at the passed absolute path.
    """
    addr_bits = img.split('/')
    for bit in addr_bits:
        if bit.endswith('.png') or bit.endswith('.jpg') or bit.endswith('.jpeg'):
            image_arr = bit.split('.')
            if len(image_arr) > 2:
                click.echo('Image name is not valid')
                return None, None
            else:
                return image_arr[0], image_arr[1]
    return None, None


def save_temp_image(img):
    """Save Image for temporary processing.
    Image will be saved in the temporary directory of the System
    :param img: Path to the image file to be used from working directory
    """
    img_name, img_extension = extract_image_name(img)
    if img_name is not None:
        img_path = os.path.join(APP_ROOT, img)
        if os.path.exists(img_path):
            shutil.copyfile(img_path, TEMP_DIR + img_name + '.' + img_extension)
        else:
            click.echo('File not found at the designated location.')
    else:
        click.echo('Unable to save to temp directory.')


def extract_file_name(names_path):
    """
    Extract file name that send the information about the names
    to be used for the badge generation.
    :param names_path: Absolute path to the names file
    :return: file name at the passed absolut path
    """
    path_arr = names_path.split('/')
    for item in path_arr:
        if item.endswith('.csv'):
            item_arr = item.split('.')
            return item_arr[0]
    return None


def save_temp_name(names):
    """Save Temporarily the csv file holding the data.
    The file will be saved in the temporary directory of the
    operating system
    :param names: Path to the names file from the working directory
    """
    names_path = os.path.join(APP_ROOT, names)
    if os.path.exists(names_path):
        if names_path.endswith('.csv'):
            file_name = extract_file_name(names_path)
            shutil.copyfile(names_path, TEMP_DIR + file_name + '.csv')
        else:
            click.echo('File is not a valid csv file.')
    else:
        click.echo('File not found at the designated location.')


@click.version_option(version='1.0.0')
@click.command()
@click.option('--img', '-i', default=None, help='Path to the svg for background.')
@click.option('--font', '-f', default=None, help='Font name to be used.')
@click.option('--config', '-c', default=None, help='Configuration file to be used.')
@click.option('--names', '-n', default=None, help='Path to the file containing'
                                                  'names (must be csv).')
@click.option('--custom_color', '-cust', default=None, help='Choose custom '
                                                            'colour for the background'
                                                            'and must be without the `#`.')
def main(img, font, config, names, custom_color):
    """
    CLI application for badge generation.
    An open source alternative for generating awesome badges
    for your awesome Organisation created by FOSSASIA.
    """
    font_ = None
    img_ = None
    config_ = None
    names_ = None
    empty_directory()
    if img is not None:
        if custom_color is None:
            img_ = img
            save_temp_image(img)
        else:
            click.echo('Custom colour can only be used with'
                       'default background option. Please pass parameters accordingly.')
    else:
        if custom_color is not None:
            CUST = custom_color
            do_svg2png('user_defined.png', 1, '#' + CUST)
        else:
            click.echo('No image or custom color is selected.')
    if font is not None:
        font_ = font
    if config is not None:
        if check_config(config):
            config_ = os.path.abspath(os.path.join(APP_ROOT, config))
    if names is not None:
        if check_names(names):
            names_ = names
            save_temp_name(names)

    badge_generator = GenerateBadges()
    badge_generator.override_param(font_, img_, config_, names_)
    badge_generator.run_generator()
    merger = MergeBadges(TEMP_DIR)
    merger.mergePDFS()
    shutil.copyfile(TEMP_DIR + 'static/badges/all-badges.pdf', GENERATED + '/badge.pdf')
