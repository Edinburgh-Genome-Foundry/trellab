import trello
import yaml
import box
from fuzzywuzzy import process

class Box(box.Box):
    def __getitem__(self, item):
        keys = list(self.keys())
        if item not in keys:
            raise KeyError(
                item
                + " not found. Did you mean: %s ?"
                % ", ".join(
                    [
                        "%s" % key
                        for (key, p) in process.extract(item, keys)
                        if p > 60
                    ]
                )
            )
        else:
            return box.Box.__getitem__(self, item)


def lists_dict(board):
    return Box({lst.name: lst for lst in board.list_lists()})


setattr(trello.Board, "lists_dict", lists_dict)


def cards_dict(lst):
    return Box({card.name: card for card in lst.list_cards()})


setattr(trello.List, "cards_dict", cards_dict)


class TrellabOrganizationClient(trello.TrelloClient):
    def __init__(
        self,
        organization_id,
        api_key,
        api_secret=None,
        token=None,
        token_secret=None,
    ):
        trello.TrelloClient.__init__(
            self,
            api_key,
            api_secret=api_secret,
            token=token,
            token_secret=token_secret,
        )
        self.org_id = organization_id
        self.organization = self.get_organization(organization_id)
        self._boards = None

    @staticmethod
    def from_yaml(path):
        with open(path, "r") as f:
            config = next(yaml.load_all(f.read()))
        return TrellabOrganizationClient(**config)

    def boards_dict(self):
        return Box(
            {board.name: board for board in self.organization.all_boards()}
        )

    def board_lists_dict(self, board):
        if isinstance(board, str):
            board = self.boards_dict()[board]
        return Box({lst.name: lst for lst in board.lists_list()})

    def new_board_from_template(self, name, template):
        if isinstance(template, str):
            template = self.boards_dict()[template]
        self.add_board(
            name, source_board=template, organization_id=self.organization.id
        )

    def add_ordered_parts_to_board(
        self, part_names, board_name, ordered_list_name="DNA_PARTS_ORDERED"
    ):
        board = self.boards_dict()[board_name]
        board_list = board.lists_dict()[ordered_list_name]
        for part_name in part_names:
            board_list.add_card(part_name)

