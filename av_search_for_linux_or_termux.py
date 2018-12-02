import urllib.request
import urllib.parse
import json
import os
import time

def url_search(code, x=5):
    url_search = 'https://api.avgle.com/v1/jav/{}/{}?limit={}'
    query = str(code)
    page = 0
    limit = str(x)
    #respond = json.load(urllib.request.urlopen(url.format(urllib.parse.quote_plus(query), page, limit)).read().decode())
    response = json.loads(urllib.request.urlopen(url_search.format(urllib.parse.quote_plus(query), page, limit)).read().decode())
    if response['success']:
        videos = response['response']['videos']
        return videos

    else:
        print('Pls connect internet or Host is down !!!!')

def main():
    os.system('clear')
    print('==============================================')
    print('+                                            +')
    print('+                How to use                  +')
    print('+                                            +')
    print('+  1.input your code                         +')
    print('+  2.input your limit to search (Default = 5)+')
    print('+                                            +')
    print('+                       Was made by B4RCODE  +')
    print('==============================================')
    print('')
    code = str(input('Code : '))
    limit = str(input('Limit to search :'))
    videos = url_search(code, limit)
    os.system('clear')
    print('Result of "', code,'"',)
    print('')
    round = 0
    for video in videos:
        round += 1
        url_video = video['video_url']
        hd_video = video['hd']
        if hd_video == True:
            hd_video = 'This video is high definition or HD'
            print(str(round)+'.'+ str(hd_video), ',Duration is',str(int(video['duration'])//60),'minutes')
            print('')
            print(str(video['video_url']))
            print('')
        else:
            hd_video = 'This video is SD'
            print(str(round)+'.'+ str(hd_video), ',Duration is',str(int(video['duration'])//60),'minutes')
            print(str(video['video_url']))
            print('')
    ans_for_search_again = input('would you like to search agin?? (Y/N)')
    if ans_for_search_again == 'Y' or ans_for_search_again == 'N'or ans_for_search_again == 'y'or ans_for_search_again == 'n':
        if ans_for_search_again == 'Y' or ans_for_search_again == 'y':
            main()
        else:
            os.system('clear')
            print('Good Bye')
            time.sleep(2)
            os.system('clear')
    else:
        os.system('clear')
        print('Please use only Y or N')
        again()

def again():
    ans_for_search_again = input('would you like to search agin?? (Y/N)')
    if ans_for_search_again == 'Y' or ans_for_search_again == 'N' or ans_for_search_again == 'y'or ans_for_search_again == 'n':
        if ans_for_search_again == 'Y' or ans_for_search_again == 'y':
            main()
        else:
            os.system('clear')
            print('Good Bye')
            time.sleep(2)
            os.system('clear')
    else:
        print('pls use (Y/N)')
        again()

if __name__ == '__main__':
    main()
