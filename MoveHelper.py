from DTOs.Move import Move


class MoveHelper:
    @staticmethod
    def check_move(gamestate, move):

        move_condition_to_check = MoveHelper.determine_move_condition(move)

        if move_condition_to_check == 1:
            return MoveHelper.__check_condition_1(gamestate)
        elif move_condition_to_check == 2 or move_condition_to_check == 3:
            return MoveHelper.__check_condition_2_and_3(gamestate, move)

    @staticmethod
    def __check_condition_1(gamestate):
        is_items_in_first_column = gamestate.columns[0].cards.size() != 0
        return is_items_in_first_column

    @staticmethod
    def __check_condition_2_and_3(gamestate, move):
        first_card_deque = gamestate.columns[move.source_column].cards
        second_card_deque = gamestate.columns[move.destination_column].cards

        is_items_in_first_column = first_card_deque.size() != 0
        is_items_in_second_column = second_card_deque.size() != 0

        if is_items_in_first_column and is_items_in_second_column and move.destination_column != 0:
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
            source = int(split_move[0])
            destination = int(split_move[1])
        except ValueError or IndexError:
            raise (ValueError("Invalid Move"))
        else:
            return Move(source, destination)

    @staticmethod
    def determine_move_condition(move):
        is_condition_1 = move.source_column == 0 and move.destination_column == 0
        is_condition_2 = move.source_column == 0 and move.destination_column > 0
        is_condition_3 = move.source_column > 0 and move.destination_column > 0

        if is_condition_1:
            return 1
        elif is_condition_2:
            return 2
        elif is_condition_3:
            return 3
        else:
            raise ValueError("Cannot determine move condition")

    @staticmethod
    def make_move(gamestate, move):
        cards_to_move = MoveHelper.__get_cards_to_move(gamestate, move)
        MoveHelper.__move_cards(gamestate, move, cards_to_move)

    @staticmethod
    def __get_cards_to_move(gamestate, move):
        move_condition = MoveHelper.determine_move_condition(move)
        cards_to_move = []

        if move_condition == 1 or move_condition == 2:
            cards_to_move.append(gamestate.columns[move.source_column].cards.remove_front())
        elif move_condition == 3:
            cards_to_move = gamestate.columns[move.source_column].cards.items
            gamestate.columns[move.source_column].cards.items = []

        return cards_to_move

    @staticmethod
    def __move_cards(gamestate, move, cards_to_move):
        move_condition = MoveHelper.determine_move_condition(move)

        if move_condition == 1:
            gamestate.columns[move.destination_column].cards.add_rear(cards_to_move[0])
        elif move_condition == 2 or move_condition == 3:
            for card in cards_to_move:
                gamestate.columns[move.destination_column].cards.add_front(card)
