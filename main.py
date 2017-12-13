import data_manager


def main():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.get_mentor_names_by_first_name('László')
    for row in mentor_names:
        print(row)
        print('Last name: ' + row['last_name'])

if __name__ == '__main__':
    main()