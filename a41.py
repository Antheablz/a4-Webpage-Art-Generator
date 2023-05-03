#!/usr/bin/env python3
from typing import IO
from enum import Enum
import sys

class Shapes(Enum):
    """ Enumerator shapes class"""
    CIRCLE = 0
    RECTANGLE = 1
    ELLIPSE = 2

class HtmlDoc:
    """ Class that writes all html related tags into the file"""

    IDENTATION = "  "
    def __init__(self, file: str,title: str) -> None:
        """ Initiates the HtmlDoc class
                parameters:
                    file - string containing html file name
                    title - string containing title of html page
        
        """
        
        self.title = title
        self.file: IO = open(file,'w')
        self.indents: int = 0
        self.write_header()

    def increase_indent(self) -> None:
        """ increases the indent inside of the html file """
        self.indents += 1

    def decrease_indent(self) -> None:
        """ decreases the indent inside of the html file"""
        self.indents -= 1

    def append(self, content: str) -> None:
        """ appends together the formatted string and the associated number of tabs to be output into html file
                parameters:
                    content - the string which contains all information to be written to file
        """
        tabs: str = HtmlDoc.IDENTATION * self.indents
        self.file.write(f'{tabs}{content}\n')
        self.file.flush()

    def write_header(self) -> None:
        """ writes the beggining of the html file """

        self.append('<html>')
        self.append('<head>')
        self.increase_indent()
        self.append(f'<title>{self.title}</title>')
        self.decrease_indent()
        self.append('</head>')
        self.append('<body>')
        
    
class SvgCanvas:
    """ Class that writes svg related elements into html file """
    IDENTATION = "  "
    def __init__(self,file: IO, width: int = 1000, height: int = 1000, shape: Shapes = 0, shape_type: str = "none", indents: int = 0) -> None:
        """ initializes the class
                parameters:
                    file - IO, 
                    width - int,
                    height - int,
                    shape - 
        
        """
        self.file: IO = open(file, 'a')
        self.width = width
        self.height = height
        self.indents = indents
        self.shape = shape 
        self.shape_type = shape_type

    def append(self, content: str) -> None:
        """ appends together the formatted string and the associated number of tabs to be output into html file
                parameters:
                    content - the string which contains all information to be written to file
        """
        tabs: str = SvgCanvas.IDENTATION * self.indents
        self.file.write(f'{tabs}{content}\n')
        self.file.flush()
    
    def increase_indent(self) -> None:
        """ increases the indent inside of the html file"""
        self.indents += 1

    def decrease_indent(self) -> None:
        """ decreases the indent inside of the html file"""
        self.indents -= 1

    def start_body(self) -> None:
        """Writes the beggining of the svg section in the html file"""

        self.increase_indent()
        self.append(f'<svg width = "{self.width}" height="{self.height}">')
        self.increase_indent()
        self.mid_body(self.shape_type)


    def mid_body(self,shape_type: str) -> None:
        """ Writes the actual shape into the html file depending on what specific shape is chosen
                parameters: 
                    shape_type - string that contains the shape type name
        """
        #determines what shape was given as input 
        if(shape_type == "circle"):
            self.append(self.shape.write_line()) #writes the first the formatted line into html file
            for i in range(0,4): #loops to modify each red shape
                self = SvgCanvas.gen_art(shape=self.shape,shape_type=self.shape_type,edit=100)
                self.append(self.shape.write_line()) #writes the rest of formatted shape lines into html file
            
            #resets so we can repeat to write the blue shapes in file
            self = SvgCanvas(file = "part1.html",width=1000,height=1000,shape=CircleShape((50,250,50,"rgb(0, 0, 255)",1.0)),shape_type="circle",indents=2)
            self.append(self.shape.write_line())
            for i in range(0,4):
                self = SvgCanvas.gen_art(shape=self.shape,shape_type=self.shape_type,edit=100)
                self.append(self.shape.write_line())

        elif(shape_type == "rectangle"):
            self.append(self.shape.write_line())
            for i in range(0,4):
                self = SvgCanvas.gen_art(shape=self.shape,shape_type=self.shape_type, edit=125)
                self.append(self.shape.write_line())
            self = SvgCanvas(file = "part1.html",width=1000,height=1000,shape=RectangleShape((50,250,100,100,"rgb(0, 0, 255)","1.0")),shape_type="rectangle",indents=2)
            self.append(self.shape.write_line())
            for i in range(0,4):
                self = SvgCanvas.gen_art(shape=self.shape,shape_type=self.shape_type,edit=125)
                self.append(self.shape.write_line())

        elif(shape_type == "ellipse"):
            self.append(self.shape.write_line())
            for i in range(0,4):
                self = SvgCanvas.gen_art(shape=self.shape,shape_type=self.shape_type,edit=125)
                self.append(self.shape.write_line())
            self = SvgCanvas(file = "part1.html",width=1000,height=1000,shape=EllipseShape((50,250,50,20,"rgb(0, 0, 255)")),shape_type="ellipse",indents=2)
            self.append(self.shape.write_line())
            for i in range(0,4):
                self = SvgCanvas.gen_art(shape=self.shape,shape_type=self.shape_type,edit=125)
                self.append(self.shape.write_line())

    def end_body(self) -> None:
        """ writes the end of the html file. """
        self.decrease_indent()
        self.append('</svg>')
        self.decrease_indent()
        self.append('</body>')
        self.append('</html>')

    
    @classmethod
    def gen_art(cls,shape, shape_type: str,edit: int) -> any:
        """ Determines/modifies the shape that will be written into the file
                Parameters:
                    shape - The actual shape 
                    shape_type - the string with the shape name
                    edit - position modification that will apply to new shape 

                returns:
                    modification to svg class such that a new shape is written into file
        
        """
        #modifies class position and colour based on the  shape
        if(shape_type == "circle"):
            return cls(file="part1.html",width = 1000,height = 1000, shape=CircleShape((edit + shape.cx,shape.cy,shape.r,shape.fill,shape.opacity)),shape_type="circle",indents = 2)
        
        elif(shape_type == "rectangle"):
            return cls(file = "part1.html", width = 1000, height = 1000, shape = RectangleShape((edit + shape.x,shape.y,shape.width, shape.height, shape.fill, shape.opacity)), shape_type = "rectangle", indents = 2)
        
        elif(shape_type == "ellipse"):
            return cls(file = "part1.html", width = 1000, height = 1000, shape = EllipseShape((edit + shape.cx, shape.cy, shape.rx,shape.ry, shape.fill)), shape_type="ellipse", indents = 2)
     
class CircleShape:
    """Class that creates a circle"""
    
    def __init__(self, circle: tuple = 0) -> None:
        """Initiates the CircleShape class
                parameters:
                    circle - tuple that contains all elements needed to initiate a circle
        """
        self.cx = circle[0]
        self.cy = circle[1]
        self.r = circle[2]
        self.fill = circle[3]
        self.opacity = circle[4]

    def write_line(self) -> str:
        """ formats the line to be written into the html file
                returns - formatted string
        """
        return (f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.r}" fill="{self.fill}" fill-opacity="{self.opacity}"></circle>')

class RectangleShape:
    """Class that creates a rectangle"""

    def __init__(self, rectangle: tuple = 0) -> None:
        """Initiates the RectangleShape class
                parameters:
                    rectangle - tuple that contains all elements needed to initiate a circle
        """
        self.x = rectangle[0]
        self.y = rectangle[1]
        self.width = rectangle[2]
        self.height = rectangle[3]
        self.fill = rectangle[4]
        self.opacity = rectangle[5]

    def write_line(self) -> str:
        """ formats the line to be written into the html file
                returns - formatted string
        """
        return (f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" style="fill:{self.fill};fill-opacity:{self.opacity}"></rect>')
         

class EllipseShape:
    """Class that creates an ellipse"""

    def __init__(self, ellipse: tuple = 0) -> None:
        """Initiates the EllipseShape class
                parameters:
                    ellipse - tuple that contains all elements needed to initiate a circle
        """
        self.cx = ellipse[0]
        self.cy = ellipse[1]
        self.rx = ellipse[2]
        self.ry = ellipse[3]
        self.fill = ellipse[4]

    def write_line(self) -> str:
        """ formats the line to be written into the html file
                returns - formatted string
        """
        return (f'<ellipse cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ry="{self.ry}" style="fill:{self.fill}"></ellipse>')


def main() -> None:
    """main method"""
    #list = [Shapes.CIRCLE.name,Shapes.RECTANGLE.name,Shapes.RECTANGLE.name]
    #print(f'shape types: {", ".join(list)}')
    #return 0

    with open('part1.html', 'a') as sys.stdout:
        doc = HtmlDoc(file="part1.html",title="My Art Part 1!!")
        
        #different shape options
        #svg = SvgCanvas(file = "part1.html",width=1000,height=1000,shape=EllipseShape((50,50,50,20,"rgb(255, 0, 0)")),shape_type="ellipse")
        #svg = SvgCanvas(file = "part1.html",width=1000,height=1000,shape=RectangleShape((50,50,100,100,"rgb(255, 0, 0)","1.0")),shape_type="rectangle")
        svg = SvgCanvas(file = "part1.html",width=1000,height=1000,shape=CircleShape((50,50,50,"rgb(255, 0, 0)",1.0)),shape_type="circle")
       
        svg.start_body() #begins writting the html body
        svg.end_body() #finished writting the end of the body
    

if __name__ == "__main__":
    main()