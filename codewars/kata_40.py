s = (
    "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
    "+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
    "+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
    "+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
    "<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
    "<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
    "<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
    "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
    "<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
    "+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
    "<P Salinge> Main Street, +1-098-512-2222, Denve\n"
)

num = "1-098-512-2222"

result = "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
TEMPLATE = "Phone => {}, Name => {}, Address => {}"

import re


def phone(strng, num):
    phone_book = strng.split("\n")
    str_punc = r"[-()\"#/@;:<>{}`+=~|.!?,_]"
    print(str_punc)
    name = ""
    phone = ""
    address = ""
    res = ""
    num_counter = 0
    print(phone_book)
    for phones in phone_book:
        if num in phones:
            num_counter += 1

            print(phones)
            phone += "+" + num
            print(phone)
            wip_phone_book = phones.replace(phone, "")
            index_1 = wip_phone_book.index("<") + 1
            index_2 = wip_phone_book.index(">")
            name = wip_phone_book[index_1:index_2]
            print(name)
            name_remove = "<" + name + ">"
            print(name_remove)
            wip_phone_book = wip_phone_book.replace(name_remove, "")
            print(wip_phone_book)
            final_phone_book = re.sub(str_punc, " ", wip_phone_book)
            print("final:", final_phone_book)
            final_phone_book = " ".join(final_phone_book.split())
            print("final 2:", final_phone_book)

            address = final_phone_book.strip()
            res = TEMPLATE.format(num, name, address)

    print(res)
    if not res:
        return "Error => Not found: {}".format(num)
    if num_counter > 1:
        return "Error => Too many people: {}".format(num)
    return res


print(phone(s, num))


# Otra solucion: def phone(strng, num):
#     list_data = strng.split('\n')
#     our_data = [i for i in list_data if ('+' + num) in i]
#
#     if our_data == []: return f'Error => Not found: {num}'
#     if len(our_data) > 1: return f'Error => Too many people: {num}'
#
#     people = our_data[0]
#     name = people[people.find('<')+1: people.find('>')]
#     adress = people.replace(('+' + num), '').replace(('<' + name + '>'), '')
#     for i in ':;,/\_|!@#$%^&?*':
#         adress = adress.replace(i, ' ')
#     adress = adress.replace('   ', ' ')
#     adress = adress.replace('  ', ' ').strip()
#
#     return f"Phone => {num}, Name => {name}, Address => {adress}"
