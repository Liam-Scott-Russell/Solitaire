class MoveChecker:
    @staticmethod
    def check_move(column1, column2, gamestate):
        column1 = str(column1)
        column2 = str(column2)
        should_check_condition_1 = column1 == "0" and column2 == "0"

        if should_check_condition_1:
            return MoveChecker.check_condition_1(gamestate)
        else:
            return False

    @staticmethod
    def check_condition_1(gamestate):
        is_items_in_first_column = gamestate.columns[0].size() != 0
        return is_items_in_first_column
