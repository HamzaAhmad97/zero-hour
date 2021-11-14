from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    generals = {
        "a" : {
            "name" : "Townes",
            "quote" : "Your weaknesses became obvious when I scanned your tactics.",
            "img" : "https://static.wikia.nocookie.net/cnc_gamepedia_en/images/2/24/GenZH_Townes_Mugshot_1.png/revision/latest/scale-to-width-down/332?cb=20180801164305"
        }, 
        "b" : {
            "name" : "Malcolm Granger",
            "quote" : "Sonic boom, baby! Let's do this thing...",
            "img" : "https://static.wikia.nocookie.net/cnc_gamepedia_en/images/b/b2/GenZH_Granger_Mugshot.png/revision/latest/scale-to-width-down/331?cb=20180801163742"
        },
        "c" : {
            "name" : "Alexis Alexander",
            "quote" : "My greatest superweapon is my brain!",
            "img" : "https://static.wikia.nocookie.net/cnc_gamepedia_en/images/d/dd/GenZH_Alexis_Alexander_Mugshot_1.png/revision/latest/scale-to-width-down/332?cb=20180801164644"
        },
        "d" : {
            "name" : "Ta Hun Kwai",
            "quote" : "Tanks are the key to any victory... as you well know.",
            "img" : "https://static.wikia.nocookie.net/cnc_gamepedia_en/images/3/34/GenZH_Kwai_Mughshot_2.png/revision/latest/scale-to-width-down/332?cb=20180801164004"
        },
        "e" : {
            "name" : "Tsing Shi Tao",
            "quote" : "Melt! Everything must melt!",
            "img" : "https://static.wikia.nocookie.net/cnc_gamepedia_en/images/e/ee/GenZH_Tao_Mugshot.png/revision/latest/scale-to-width-down/332?cb=20180801163711"
        },
        "f" : {
            "name" : "Shin Fai \"Anvil\"",
            "quote" : "I have enough men to crush you without firing a shot!",
            "img" : "https://static.wikia.nocookie.net/cnc_gamepedia_en/images/7/78/GenZH_Fai_Mugshot.png/revision/latest/scale-to-width-down/332?cb=20180801164837"
        },
        "g" : {
            "name" : "Dr. Thrax",
            "quote" : "I've mastered the effects of chemicals on the human body. Want to see?",
            "img" : "https://static.wikia.nocookie.net/cnc_gamepedia_en/images/a/a7/GenZH_Trax_1.png/revision/latest/scale-to-width-down/331?cb=20180801164810"
        },
        "h" : {
            "name" : "Prince Kassad",
            "quote" : "Accept your bitter defeat and remove yourself from my sight, general!",
            "img" : "https://static.wikia.nocookie.net/cnc_gamepedia_en/images/1/15/GenZH_Kassad_1.png/revision/latest/scale-to-width-down/331?cb=20180801163921"
        },
        "i" : {
            "name" : "Rodall Juhziz \"Demo\"",
            "quote" : "It's quiet out there, general...you know what quiet means right? BOOM...HAHAHAHA!!",
            "img" : "https://static.wikia.nocookie.net/cnc_gamepedia_en/images/7/70/GenZH_Rodall_Mugshot.png/revision/latest/scale-to-width-down/331?cb=20180801163820"
        },
    }
    return render(request, 'generals/home.html', context= {"generals":generals})

def about(request):
    return render(request, 'generals/about.html')
