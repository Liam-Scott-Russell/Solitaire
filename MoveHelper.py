class MoveHelper:
    @staticmethod
    def check_move(column1, column2, gamestate):

        should_check_condition_1 = column1 == 0 and column2 == 0
        should_check_condition_2 = column1 == 0 and column2 > 0
        should_check_condition_3 = column1 > 0 and column2 > 0

        if should_check_condition_1:
            return MoveHelper.check_condition_1(gamestate)
        elif should_check_condition_2:
            return MoveHelper.check_condition_2_and_3(gamestate, 0, column2)
        elif should_check_condition_3:
            return MoveHelper.check_condition_2_and_3(gamestate, column1, column2)
        else:
            return False

    @staticmethod
    def check_condition_1(gamestate):
        is_items_in_first_column = gamestate.columns[0].size() != 0
        return is_items_in_first_column

    @staticmethod
    def check_condition_2_and_3(gamestate, column1, column2):
        first_card_deque = gamestate.columns[column1]
        second_card_deque = gamestate.columns[column2]

        is_items_in_first_column = first_card_deque.size() != 0
        is_items_in_second_column = second_card_deque.size() != 0

        if is_items_in_first_column and is_items_in_second_column and column2 != 0:
            first_card_in_second_column = second_card_deque.peek_front()
            first_card_in_first_column = first_card_deque.peek_front()

            first_card_is_one_less_than_second = first_card_in_first_column.number == first_card_in_second_column.number - 1
            return first_card_is_one_less_than_second

        else:
            return is_items_in_first_column

    @staticmethod
    def format_move(possible_move):
        move_without_whitespace = possible_move.replace(" ", "")
        try:
            split_move = move_without_whitespace.split(",")
            column1 = int(split_move[0])
            column2 = int(split_move[1])
        except ValueError or IndexError:
            raise(ValueError("Invalid Move"))
        else:
            return column1, column2
