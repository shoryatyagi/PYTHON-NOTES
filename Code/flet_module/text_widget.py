import flet
from flet import *

def main(page:Page):
    page.title = "Flet App" # adding the title of the app
    page.bgcolor = colors.AMBER #adding the bg color
    #page.padding = 70 #giving the padding from all four sides
    page.padding = padding.only(left=40,top=30)
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }
    print(page.platform) #return the platform
    print(page.web) #return true if on web
    page.horizontal_alignment = 'center' #align to the center from x-axis
    page.vertical_alignment = 'center' #align to the center from y-axis
    page.scroll = 'always' #for adding scrollbar    hidden/adaptive/auto/none
    page.window_frameless = False # with or without titlebar
    print(page.session_id)
    page.window_opacity = 0.9 # transparency of the window
    page.resizable = False #resizable or not
    page.window_height =700 #set the height of the window
    page.window_width = 500  #set the width of the window

    for i in range(100):
        t = Text(
            value = 'Hello Shorya',
            size=40,
            color=colors.WHITE,
            bgcolor=colors.BLUE_600,
            weight=FontWeight.W_100,
            font_family="RobotoSlab",
            )
        page.add(t) # for adding widget into the page
    #page.controls.append(t) #for adding the widget into the page
    #page.update()
    print(page.width) #print the width of the page

flet.app(target=main,view=FLET_APP) #for running as app
#flet.app(target=main,view=WEB_BROWSER) #for running into browser


