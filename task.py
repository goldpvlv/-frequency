from sqlite import create_connection, execute_query
import string

text = list()
alph = list()

with open("text.txt") as file:
    for items in file:
        text += list(items.lower())

with open("alph.txt") as file:
    for items in file:
        alph += list(items.lower())


current_dict = {}
length = 0


def n_grams(n):
    global length
    length = 0
    ngram = []

    def text2ngrams(n):
        ngrams = []
        flag = False
        ban = set("0123456789 .,!?:;«»%-+=/\n()–'xi’")
        for i in range(len(text) - n + 1):
            k = 0
            while k != n:
                if text[i+k] in ban:
                    flag = True
                k += 1
            if (flag):
                flag = False
                continue
            else:
                ngram.append("".join(text[i:i + n]))

    text2ngrams(n)

    length = len(ngram)

    for key in ngram:
        current_dict[key] = current_dict.get(key, 0) + 1

    for key in text:
        if key in current_dict:
            current_dict[key] += 1

def one_gram():
    global length
    length = 0

    for key in alph:
        current_dict[key] = current_dict.get(key, 0.0)

    for i in text:
        if i in alph:
            length += 1

    for key in text:
        if key in current_dict:
            current_dict[key] += 1



def write_sql():

    connection = create_connection("/home/zlata/dataBase.sglite")

    create_table = """
    CREATE TABLE IF NOT EXISTS task (
      id INTEGER PRIMARY KEY,
      n_gram TEXT NOT NULL,
      number_of_n_gram INTEGER,
      number_of_all_n_gram INTEGER,
      procent FLOAT
    );
    """
    params = ()
    execute_query(connection, create_table, params)

    for key in current_dict:
        create_task = """
        INSERT INTO
          task (n_gram, number_of_n_gram, number_of_all_n_gram, procent)
        VALUES
          (?,?,?,?);
        """
        params = (str(key).upper(), current_dict.get(key), length, "%.3f" % ((current_dict.get(key) / length) * 100))
        execute_query(connection, create_task, params)



for n in range(1,4):
    if n == 1:
        one_gram()
        write_sql()
        current_dict.clear()
    else:
        n_grams(n)
        write_sql()
        current_dict.clear()

print("f")