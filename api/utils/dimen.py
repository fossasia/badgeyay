class Dimen(object):
    def __init__(self, badges, badgeSize, paperSize):
        self.badges = badges
        self.badgeSize = badgeSize
        self.paperSize = paperSize


badge_config = {}


def init_dimen():
    paper_sizes = ['A2', 'A3', 'A4']
    for paper in paper_sizes:
        if paper == 'A2':
            badge_config.__setitem__(paper, {'4x3': Dimen(18, '4x3', paper)})
        elif paper == 'A3':
            badge_config.__setitem__(paper, {'4x3': Dimen(8, '4x3', paper)})
        elif paper == 'A4':
            badge_config.__setitem__(paper, {'4x3': Dimen(6, '4x3', paper)})
