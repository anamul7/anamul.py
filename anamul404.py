logo="""
'##::::'##:'########:::::::'########:::::'###::::'########:'####:
 ###::'###: ##.... ##:::::: ##.... ##:::'## ##::: ##.....::. ##::
 ####'####: ##:::: ##:::::: ##:::: ##::'##:. ##:: ##:::::::: ##::
  ## ### ##: ########::::::: ########::'##:::. ##: ######:::: ##::
 ##. #: ##: ##.. ##:::::::: ##.. ##::: #########: ##...::::: ##::
  ##:.:: ##: ##::. ##::'###: ##::. ##:: ##.... ##: ##:::::::: ##::
 ##:::: ##: ##:::. ##: ###: ##:::. ##: ##:::: ##: ##:::::::'####:
..:::::..::..:::::..::...::..:::::..::..:::::..::..::::::::....::
      
--------------------------------------------------
  Author   : MR.RAFI
  Github   :  https://github.com/anamul404
  Youtube  :.... 
--------------------------------------------------
  If oppurtunity donot knock, build a door
--------------------------------------------------"""
oks=[]
cps=[]
def main():
    os.system('clear')
    print(logo)
    print('  [1] Crack')
    print('  [2] Create file manual')
    print('  [3] Create file auto')
    print('  [4] Separate ids')
    print('  [l] Login another token')
    print(50*'-')
    option = input('  Select option: ')
    if option =='1':
        crack()
    elif option =='2':
        manual()
    elif option =='3':
        auto()
    elif option =='4':
        sep()
    elif option =='5':
        os.system('rm -rf .chrome.txt .android.txt && python anamul.py')
    elif option =='l' or option =='L':
        print('  Logging you out first')
        time.sleep(1)
        os.system('rm -rf access_token.txt')
        login()
    else:
        print('  Choose valid option ')
        time.sleep(1)
        main()
def manual():
    try:
        token = open('access_token.txt', 'r').read()
    except FileNotFoundError:
        login()
    print('  Checking logged in account ....')
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    print(logo)
    print('  Name: '+uname)
    print(50*'-')
    limit = int(input('  How many ids do you want to add ? '))
    save_file = input('  Save file as: ')
    t = 0
    for u in range(limit):
        t+=1
        try: