from logic import worker


if __name__ == '__main__':
    letter_list = list(input())
    answer = worker(letter_list)
    print(answer)
