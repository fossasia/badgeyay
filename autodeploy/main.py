import argparse
import logging
import threading
import sys
import yaml

from os.path import join

from auto_updater import AutoUpdater

POLL_SECONDS = 60

logger = logging.getLogger(__name__)
log_format = '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)

parser = argparse.ArgumentParser()
parser.add_argument('--workdir', help='Directory to clone projects in')
parser.add_argument('--config', help='config.yml with project description')

def get_auto_updater(cwd, name, cfg):
    logger.info('project <%s> from <%s> added', name, cfg['url'])
    a = AutoUpdater(
            name, cfg['url'], cwd=join(cwd, name), branch=cfg['branch'])

    #init part

    return a

def start_all_projects(projects):
    for p in projects:
        p.start()

def update_all_projects(projects):
    for p in projects:
        logger.info('updating %s', p.repo)
        p.update()
        p.upgrade()

    logger.info('sleeping %d seconds', POLL_SECONDS)
    threading.Timer(POLL_SECONDS, update_all_projects).start()

if __name__ == '__main__':
    args = parser.parse_args()
    if not args.workdir:
        print('workdir not set. Run `--help` to show options')
        sys.exit(1)
    if not args.config:
        print('config not set. Run `--config` to show options')
        sys.exit(1)

    cwd = args.workdir
    config_file = args.config

    with open(config_file, 'r') as ymlfile:
        config = yaml.load(ymlfile)

    projects = [get_auto_updater(cwd, n, config[n]) for n in config]

    logger.info('starting projects')
    start_all_projects(projects)
    logger.info('starting update threads for projects')
    update_all_projects(projects)
