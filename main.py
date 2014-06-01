import Image, ImageDraw, string
from itertools import cycle


def draw_chessboard(tag_size=5, pixel_width=200):
    "Draw an n x n chessboard using PIL."
    def sq_start(i):
        "Return the x/y start coord of the square at column/row i."
        return i * pixel_width / tag_size
    
    def square(i, j):
        "Return the square corners, suitable for use in PIL drawings" 
        return map(sq_start, [i, j, i + 1, j + 1])
    binary = lambda cc: cc>0 and [cc&1]+binary(cc>>1) or []
    n = (tag_size-2)*(tag_size-2)-4
    n=2**n
    for i in range(0,n):
        print i
        bin = list(("{0:0%db}"%n).format(i))
        revbin =  list(reversed(bin))
        pix = [[1 for x in range(0,tag_size)] for x in range(0,tag_size)]
        
        
        for xx in range(1,tag_size-1):
            for yy in range(1,tag_size-1):
                pix[xx][yy]=2
                if (xx==(tag_size-1)-yy and (xx==1 or yy==1)) or (xx==tag_size-2 and yy==tag_size-2):
                    pix[xx][yy]=1
                if xx==1 and yy==1:
                    pix[xx][yy]=0
        cc=0
        
        for xx in range(1,tag_size-1):
            for yy in range(1,tag_size-1):
                if(pix[xx][yy]==2):
                    if int(revbin[cc]) > 0:
                        pix[xx][yy]=1
                    else :
                        pix[xx][yy]=0
                    cc=cc+1
               
    
        squares=[]
        for xx in range(0,tag_size):
            strng = ''
            for yy in range(0,tag_size):
                if(pix[xx][yy]==0):
                    squares.append(square(xx,yy))
                strng+=str(pix[xx][yy])
            print strng
                
        
        image = Image.new("L", (pixel_width, pixel_width))
        draw_square = ImageDraw.Draw(image).rectangle
        for sq in squares:
            draw_square(sq, fill='white')
    
    
    
                
        image.save("tag%d.%dx%d.png"%(i,tag_size,tag_size))
    
    
    
    
draw_chessboard(tag_size=5, pixel_width=300)
