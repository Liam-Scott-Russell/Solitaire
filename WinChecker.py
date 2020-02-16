class WinChecker:
    @staticmethod
    def check_if_won(gamestate):
        first_column_is_empty = gamestate.columns[0].size() == 0

        column_sizes = [deque.size() for deque in gamestate.columns]
        number_of_empty_columns = column_sizes.count(0)
        only_one_column_has_cards = number_of_empty_columns == len(gamestate.columns) - 1

        return first_column_is_empty and only_one_column_has_cards
