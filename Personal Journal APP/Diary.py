import journal                      # retain namespace
# from journal import load, save    # get individual entities
# from journal import *             # import all direct


def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------------------------')
    print('             JOURNAL APP')
    print('-------------------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = 'Empty'
    journal_name = 'default'
    journal_data = journal.load(journal_name)  # []  # list()
    # by using import journal I have to use journal.load
    # by using from journal import load, save I have to use just method load or save

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        # setting character rules
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))

    print('Done, thank you come again :)')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    # setting the order from the newest entry to the oldest
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)
    # data.append(text)  # append -> adding new item


print("__file__ " + __file__)
print("__name__ " + __name__)

if __name__ == '__main__':
    main()
