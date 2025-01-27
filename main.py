def countWords(string):
    Words = string.split()
    Count = len(Words)
    return Count

def countChars(string):
    Count = {}
    for char in string.lower():
        if char in Count:
            Count[char] += 1
        else:
            Count[char] = 1
    return Count

def sort_on(dict):
    return dict["num"]

def printNicely(Count, List):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{Count} words found in the document\n')
    for item in List:
        if str(item.get("name")).isalpha():
            print(f"The '{item.get("name")}' character was found {item.get("num")} times")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        Count = countWords(file_contents)
        CountChars = countChars(file_contents)
        CharList = []
        for key in CountChars.keys():
            CharList.append({"name": key,
            "num": CountChars.get(key)})
        CharList.sort(reverse=True, key=sort_on)
        printNicely(Count, CharList)
main()