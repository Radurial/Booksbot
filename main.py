import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_music = types.KeyboardButton(text='Музыка')
    button_books = types.KeyboardButton(text='Книги')
    markup.add(button_music, button_books)
    bot.send_message(message.chat.id, 'Привет! Меня зовут Сирин. Я бот, который облегчит тебе жизнь в плане подготовки к путешествию. Всем людям лень скачивать в дорогу музыку, книги и тому подобное и я создана, чтобы помочь вам с этим. Выбери то, что тебе нужно, и я покажу тебе, что у меня есть.', reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == 'Музыка')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Рок')
    button2 = types.KeyboardButton(text='Рэп')
    button3 = types.KeyboardButton(text='Инди')
    button4 = types.KeyboardButton(text='Ретро')
    button5 = types.KeyboardButton(text='Джаз')
    button6 = types.KeyboardButton(text='Спокойная музыка')
    button7 = types.KeyboardButton(text='Барокко-поп')
    button8 = types.KeyboardButton(text='Музыка из аниме')
    button9 = types.KeyboardButton(text='Назад')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
    bot.send_message(message.chat.id, 'Выбери жанр!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Рок')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Русский рок')
    button2 = types.KeyboardButton(text='Зарубежный рок')
    button3 = types.KeyboardButton(text='Вернуться к музыкальным жанрам')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери поджанр!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Рэп')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Подборка русских песен')
    button2 = types.KeyboardButton(text='Подборка зарубежных песен')
    button3 = types.KeyboardButton(text='Вернуться к музыкальным жанрам')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери поджанр!', reply_markup=markup)



@bot.message_handler(func=lambda m: m.text == 'Книги')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Фантастические романы')
    button2 = types.KeyboardButton(text='Детектив')
    button3 = types.KeyboardButton(text='История')
    button4 = types.KeyboardButton(text='Манга')
    button5 = types.KeyboardButton(text='Романы')
    button6 = types.KeyboardButton(text='Приключения')
    button7 = types.KeyboardButton(text='Назад')
    markup.add(button1, button2, button3, button4, button5, button6, button7)
    bot.send_message(message.chat.id, 'Выбери жанр!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Фантастические романы')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Жюль Верн. Таинственный остров')
    button2 = types.KeyboardButton(text='Дюна. Френк Герберт')
    button3 = types.KeyboardButton(text='Вернуться к жанрам книг')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери книгу!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Детектив')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Убийство в Восточном экспрессе. Агата Кристи')
    button2 = types.KeyboardButton(text='Мальтийский сокол. Хэммет Дэниел')
    button3 = types.KeyboardButton(text='Вернуться к жанрам книг')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери книгу!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'История')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Цари.Романовы.История династии')
    button2 = types.KeyboardButton(text='История Российского государства')
    button3 = types.KeyboardButton(text='Вернуться к жанрам книг')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери книгу!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Манга')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='3-ий удар Хонкая')
    button2 = types.KeyboardButton(text='Монолог фармацевта')
    button3 = types.KeyboardButton(text='Вернуться к жанрам книг')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери книгу!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Романы')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Метро 2033')
    button2 = types.KeyboardButton(text='Пикник на обочине')
    button3 = types.KeyboardButton(text='Вернуться к жанрам книг')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери книгу!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Приключения')
def list(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Остров сокровищ')
    button2 = types.KeyboardButton(text='Путешествие к центру Земли')
    button3 = types.KeyboardButton(text='Вернуться к жанрам книг')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выбери книгу!', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def send(message):

    if message.text == 'Русский рок':
        bot.send_audio(message.chat.id, (open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Music\\5_02_Bi_2_Пора_возвращаться_домой_feat_Oxxxymiron.m4a", 'rb')))

    elif message.text == 'Зарубежный рок':
        bot.send_audio(message.chat.id, (open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Music\\The Cranberries - Zombie.mp3", 'rb')))

    elif message.text == 'Подборка русских песен':
        bot.send_audio(message.chat.id, (open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Music\\Markul   Oxxxymiron - Fata Morgana.mp3",'rb')))

    elif message.text == 'Подборка зарубежных песен':
        bot.send_audio(message.chat.id, (open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Music\\4 27_Eminem_Godzilla (feat. Juice WRLD).m4a",'rb')))

    elif message.text == 'Инди':
        bot.send_audio(message.chat.id, (open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Music\\474499119_456770562.mp3", 'rb')))

    elif message.text == 'Ретро':
        bot.send_audio(message.chat.id, (open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Music\\Modern Tolking - Chery Chery Lady.mp3", 'rb')))

    elif message.text == 'Джаз':
        bot.send_audio(message.chat.id, (open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Music\\BILLY GILMAN - WARM & FUZZY (+).mp3", 'rb')))

    elif message.text == 'Спокойная музыка':
        bot.send_audio(message.chat.id, (open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Music\\1_58_Ирина_Мельник_Эндинг_ко_2_сезону_благословение_небожителей.m4a", 'rb')))

    elif message.text == 'Барокко-поп':
        bot.send_audio(message.chat.id,(open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Music\\3 48_Green Apelsin_Парфюмер.m4a", 'rb')))

    elif message.text == 'Музыка из аниме':
        bot.send_audio(message.chat.id, (open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Music\\3 38_Ryokuoushoku Shakai_Be a flower.m4a", 'rb')))

    elif message.text == 'Жюль Верн. Таинственный остров':
        bot.send_document(message.chat.id, open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Books\\Верн_Жюль_Таинственный_остров_перевод_Н_Немчиновой_и_А_Худадовой.zip", 'rb'))

    elif message.text == 'Дюна. Френк Герберт':
        bot.send_document(message.chat.id, open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Books\\89413564.a4.zip", 'rb'))

    elif message.text == 'Цари.Романовы.История династии':
        bot.send_document(message.chat.id, open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Books\\60216506.a4.pdf", 'rb'))

    elif message.text == 'История Российского государства':
        bot.send_document(message.chat.id, open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Books\\1.pdf", 'rb'))

    elif message.text == 'Убийство в Восточном экспрессе. Агата Кристи':
        bot.send_document(message.chat.id, open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Books\\preview6802.pdf", 'rb'))

    elif message.text == 'Мальтийский сокол. Хэммет Дэниел':
        bot.send_document(message.chat.id, open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Books\\Хэммет_Дэниел_Мальтийский_сокол_royallib_com_doc.zip", 'rb'))

    elif message.text == '3-ий удар Хонкая':
        bot.send_document(message.chat.id, open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Books\\Honkai_Impact_3rd_Second_Eruption_Том_1_Глава_3_mangalib_me.zip", 'rb'))

    elif message.text == 'Монолог фармацевта':
        bot.send_document(message.chat.id, open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Books\\Kusuriya no Hitorigoto Том 1 Глава 1 [mangalib.me].zip", 'rb'))

    elif message.text == 'Остров сокровищ':
        bot.send_document(message.chat.id, open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Books\\27373645.a4.zip", 'rb'))

    elif message.text == 'Путешествие к центру Земли':
        bot.send_document(message.chat.id, open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Books\\Верн_Жюль_Путешествие_к_центру_Земли_royallib_com_doc.zip", 'rb'))

    elif message.text == 'Метро 2033':
        bot.send_document(message.chat.id, open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Books\\[litmore_ru]-128391.zip", 'rb'))

    elif message.text == 'Пикник на обочине':
        bot.send_document(message.chat.id, open("C:\\Users\\alexe\\PycharmProjects\\booksbot\\Books\\85837715.a4.zip", 'rb'))

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_music = types.KeyboardButton(text='Музыка')
        button_books = types.KeyboardButton(text='Книги')
        markup.add(button_music, button_books)
        bot.send_message(message.chat.id, 'Выбирай!', reply_markup=markup)


    elif message.text == 'Вернуться к музыкальным жанрам':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = types.KeyboardButton(text='Рок')
        button2 = types.KeyboardButton(text='Рэп')
        button3 = types.KeyboardButton(text='Инди')
        button4 = types.KeyboardButton(text='Ретро')
        button5 = types.KeyboardButton(text='Джаз')
        button6 = types.KeyboardButton(text='Спокойная музыка')
        button7 = types.KeyboardButton(text='Барокко-поп')
        button8 = types.KeyboardButton(text='Музыка из аниме')
        button9 = types.KeyboardButton(text='Назад')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
        bot.send_message(message.chat.id, 'Выбери жанр!', reply_markup=markup)

    elif message.text == 'Вернуться к жанрам книг':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = types.KeyboardButton(text='Фантастические романы')
        button2 = types.KeyboardButton(text='Детектив')
        button3 = types.KeyboardButton(text='История')
        button4 = types.KeyboardButton(text='Манга')
        button5 = types.KeyboardButton(text='Романы')
        button6 = types.KeyboardButton(text='Приключения')
        button7 = types.KeyboardButton(text='Назад')
        markup.add(button1, button2, button3, button4, button5, button6, button7)
        bot.send_message(message.chat.id, 'Выбери жанр!', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Я такой команды не знаю!')

if __name__ == '__main__':
    bot.polling()

