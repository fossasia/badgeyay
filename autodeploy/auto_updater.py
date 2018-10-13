import logging
from os import makedirs
from os.path import exists

from docker import DockerCompose, DockerComposeError
from git import Git

logger = logging.getLogger(__name__)

class AutoUpdater():
    def __init__(self, name, repo, cwd='.', branch='master'):
        self.name = name
        self.repo = repo
        self.cwd = cwd
        self.docker = DockerCompose(cwd)
        self.git = Git(repo, cwd, branch)

        if not exists(cwd):
            logger.info('<%s> creating missing directory %s', self.name, cwd)
            makedirs(cwd)
            self.git.clone_if_necessary()
            try:
                self.first_startup()
            except DockerComposeError as e:
                logger.error('<%s> could not start docker-compose: %s',
                        self.name, e.errors)

    def build(self):
        try:
            self.docker.build()
        except DockerComposeError as e:
            logger.warning('<%s> build threw an error: %s', self.name,
                    e.errors)
    
    def start(self):
        try:
            self.docker.start()
        except DockerComposeError as e:
            logger.warning('<%s> start threw an error: %s', self.name,
                    e.errors)

    def update(self):
        if self.git.changed_files() > 0:
            running_commit_date = self.git.last_commit_date()
            self.git.pull()
            latest_commit_date = self.git.last_commit_date()
            self.docker.update()
            logger.info('<%s> update finished, %s to %s', self.name,
                    running_commit_date, latest_commit_date)
        else:
            logger.info('<%s> no update needed', self.name)
