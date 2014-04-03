# coding: utf-8
__author__ = 'polly'

'''
Написать функцию-словарик для перевода слов с английского языка.
- слова, например: sun, like, warm, rest..
- У каждого слова:
- транскрипция (русские буквы)
- несколько значений
- значения делятся по типам - глагол, существительное, прилагательное
- по-умолчанию выводить все данные
- должна быть возможность получить только значения по типу (глагол, прилагательное и тп.)
- или только транскрипцию
- или любые сочетания
- возможность задать максимальное количество выводимых значений по типу
'''

simple_dict = {
    'sun': {
        'translate': 'сан',
        'глагол': ['загорать', ],
        'существительное': ['солнце', ],
        'прилагательное': ['солнечный', ],
    },
    'like': {
        'translate': 'лайк',
        'глагол': ['нравиться', ],
        'существительное': ['подобно', ],
        'прилагательное': ['наподобие', ],
    },
    'warm': {
        'translate': 'ворм',
        'глагол': ['греть', ],
        'существительное': ['тепло', ],
        'прилагательное': ['тёплый', ],
    },
    'rest': {
        'translate': 'рэст',
        'глагол': ['отдыхать', 'прерывать'],
        'существительное': ['перерыв', 'отдых'],
        'прилагательное': ['прерванный', 'отдохнувший'],
    },
}


def simpleDict():
    pass


def print_translate(param=None):
    if param == 'None':
        for key in simple_dict:
            print '%s [%s]' % (key, simple_dict[key]['translate'])
    else:
        print '%s [%s]' % (param, simple_dict[param]['translate'])


def print_all():
    for key in simple_dict:
        print '*' * 50
        print 'слово: %s [%s]' % (key, simple_dict[key]['translate'])
        print ''
        for item in simple_dict[key]:
            if not item == 'translate':
                print '%s:' % item
                for value in simple_dict[key][item]:
                    print '     %s' % value


def print_meaning(word, type):
    print '%s' % word
    for item in simple_dict[word][type]:
        print '-%s' % item


def print_word(param):
    print '*' * 50
    print 'word: %s' % param
    for key in simple_dict[param]:
        print ''
        if not key == 'translate':
            print key
            for value in simple_dict[param][key]:
                print '-%s' % value


def main(param=None):
    if not param:
        print_all()
    elif len(param) == 1:
        print_word(param[0])
    elif len(param) == 2:
        if param[1] == 'translate':
            print_translate(param[0])
        else:
            print_meaning(param[0], param[1])


if __name__ == '__main__':
    word = []
    #word = ['sun']
    #word = ['sun', 'translate']
    #word = ['sun', 'глагол']
    main(word)
