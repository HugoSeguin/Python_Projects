

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d/)')
mo = phoneNumREgex.search(input())

areaCode, mainNumber = mo.groups()

