import copy


def worker(need_words_list: list) -> list:
    answer_list = []
    with open("allwords.txt", encoding="cp1251") as words_file:
        for word_in_file in words_file:
            word_in_file = word_in_file.replace("\n", "")
            list_word_in_file = list(word_in_file)
            letter_count = 0
            copy_need_words_list = copy.copy(need_words_list)
            for one_letter in list_word_in_file:
                if one_letter in copy_need_words_list:
                    letter_count += 1
                    copy_need_words_list.remove(one_letter)
                else:
                    break
            # else:
            if len(list_word_in_file) == letter_count and letter_count != 1:
                answer_list.append(word_in_file)
    return answer_list
