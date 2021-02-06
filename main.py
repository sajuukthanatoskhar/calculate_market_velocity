
import pyperclip

"""
Little tool for importing market orders by intercepting paste and then calculating that to a 30 day average/10"""


def parse_copy_paste(inputpaste: str) -> str:
    """
    Parses Paste
    :param inputpaste:
    :return: Trello Card
    """
    trello_card_name = str
    total_orders = 0
    formattedlines = inputpaste.split(sep='\n', )
    for index in range(0, len(formattedlines)):
        formattedlines[index] = formattedlines[index].split(sep='\t')

    for line in formattedlines:
        total_orders += int(line[2])


    name = input("Name of Module")
    trello_card_name = "{} {}".format(name, str(total_orders/(300)))
    return trello_card_name

if __name__ == '__main__':

    pasteinput = pyperclip.paste()   #input("Copy Paste 30 day market data of object $ ")
    result = parse_copy_paste(pasteinput)
    print(result)
    pyperclip.copy(result)

    #pyperclip.paste



