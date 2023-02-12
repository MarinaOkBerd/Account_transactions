import datetime as dt

from study_project.src import loader
from study_project.src.formatters import OperationFormatter

URL = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676299637005&signature=3nYMm1hPOoKmqMyKv9THm4RpvhZZLyz8rh50ibDP20M&downloadName=operations.json'


INITIAL_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
EXECUTED_OPERATION_STATE = 'EXECUTED'

DISPLAYED_OPERATION_COUNT = 5

RESULT_DATE_FORMAT = '%d.%m.%Y'
CARD_NUMBER_FORMAT = 'XXXX XX** **** XXXX'
NUMBER_OF_DIGITS_DISPLAYED_IN_ACCOUNT = 4


def convert_date_strings(operations):
    for operation in operations:
        date_string = operation.get('date')

        if date_string is not None:
            timestamp = dt.datetime.strptime(date_string, INITIAL_DATE_FORMAT)
            operation['date'] = timestamp


def get_last_executed_operations(operations):

    operations_with_date = filter(
        lambda operation: (
                'date' in operation and operation['state'] == EXECUTED_OPERATION_STATE
        ),
        operations
    )
    return sorted(
        operations_with_date,
        key=lambda operation: operation['date'],
        reverse=True,
    )[:DISPLAYED_OPERATION_COUNT]


def main():
    operations = loader.load_operations(URL)

    convert_date_strings(operations)
    last_executed_operations = get_last_executed_operations(operations)
    formatter = OperationFormatter(
        date_format=RESULT_DATE_FORMAT,
        card_number_format=CARD_NUMBER_FORMAT,
        number_of_digits_displayed_in_account=(
            NUMBER_OF_DIGITS_DISPLAYED_IN_ACCOUNT
        ),
    )

    formatted_operations = []
    for operation in last_executed_operations:
        formatted_operations.append(formatter.format(operation))

    print('\n\n'.join(formatted_operations))


if __name__ == '__main__':
    main()
    