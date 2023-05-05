from typing import NamedTuple, IO
from enum import Enum
import random as rd
import sys

# @author Anthea Blais

class Shapes(Enum):
    """ Enumerator shapes class"""
    CIRCLE = 0
    RECTANGLE = 1
    ELLIPSE = 2
    
class FloatRange(NamedTuple):
    """class for the float ranges"""
    fmin: float
    fmax: float

class IntRange(NamedTuple):
    """class for the integer ranges"""
    imin: int
    imax: int

class Colours(NamedTuple):
    """Class for the different colours"""
    red: IntRange
    green: IntRange
    blue: IntRange
    opacity: FloatRange

# STATIC FUNCTIONS
def gen_int(r: IntRange) -> int:
    """Generates a random integer"""
    return rd.randint(r.imin, r.imax)

def gen_float(r: FloatRange) -> float:
    """Generates a random float"""
    return round(rd.uniform(r.fmin,r.fmax),2) #rounds to 2 decimal spaces


class PyArtConfig:
    """ sets the configurations for shapes to be displayed"""
    counter: int = 1 #counts the number of shapes created
    
    def __init__(self, viewport: IntRange, rad: IntRange, rx: IntRange, ry: IntRange, width: IntRange, height: IntRange, red: Colours.red, green: Colours.green, blue: Colours.blue, opacity: Colours.opacity) -> None:
        """ Initiates the class and sets configurations 
                parameters:
                    viewport - Intrange, window range the shapes can be within
                    rad - IntRange, determines radius of circle
                    rx - IntRange, determines rx in ellipse 
                    ry - IntRange, determines ry in ellipse
                    width - IntRange, determines width of rectangle 
                    height - IntRange, determines height of rectangle
                    red - (Colours.red) IntRange, determines red rgb number
                    green - (Colours.green) IntRange, determines green rgb number
                    blue - (Colours.blue) IntRange, determines blue rgb number
                    opacity - (Colours.opacity) Intrange, determines the opactiy
    
        """
        self.viewport = viewport
        self.rad = rad
        self.rx = rx
        self.ry = ry
        self.width = width
        self.height = height
        self.red = red
        self.green = green
        self.blue = blue
        self.opacity = opacity
        PyArtConfig.counter +=1

    @classmethod
    def get_count(cls) -> int:
        """ returns the number of instances created from this class"""
        return cls.counter
    
    @classmethod
    def from_input(cls, viewport: IntRange) -> any:
        """ Modifies and returns the class based on the user input. Creates the configurations used for shape constraints."""
        viewport: IntRange = viewport

        rad_min: int = int(input('radius Min:'))
        rad_max: int = int(input('radius Max:'))
        radius = IntRange(imin=rad_min, imax=rad_max)

        ellp_min: int = int(input('ellipse min:'))
        ellp_max: int = int(input('ellipse max:'))
        rxy: IntRange = IntRange(imin=ellp_min,imax=ellp_max)

        width_min: int = int(input('min width:'))
        width_max: int = int(input('max width:'))
        width: IntRange = IntRange(imin= width_min,imax=width_max)

        height_min: int = int(input('min height:'))
        height_max: int = int(input('max height:'))
        height: IntRange = IntRange(imin=height_min,imax=height_max)

        red_min: int = int(input('min red:'))
        red_max: int = int(input('max red:'))
        red: IntRange = IntRange(imin=red_min,imax=red_max)

        green_min: int = int(input('min green:'))
        green_max: int = int(input('max green:'))
        green: IntRange = IntRange(imin=green_min,imax=green_max)

        blue_min: int = int(input('min blue:'))
        blue_max: int = int(input('max blue:'))
        blue: IntRange = IntRange(imin=blue_min,imax=blue_max)

        opacity_min: float = float(input('min opacity:'))
        opacity_max: float = float(input('max opacity:'))
        opacity: FloatRange = FloatRange(fmin=opacity_min,fmax=opacity_max)

        #modifies the class so that it has the new user defined constraints
        return cls(viewport = viewport, rad = radius, rx = rxy, ry = rxy, width = width, height = height, red = red, green = green, blue = blue, opacity = opacity)
        
class CircleShape: 
    """ Class to create a circle"""
    def __init__(self, config: PyArtConfig, shape_name: Shapes) -> None:
        """ Initalizes the CircleShape class
                parameters:
                    congig - PyArtConfig, numbers generated from contraints
                    shape_name - Shapes, type of shape
        """

        #generates the elements needed for a circle based on the previously set constraints
        self.x = gen_int(config.viewport) 
        self.y = gen_int(config.viewport)
        self.rad = gen_int(config.rad)
        self.rx = None
        self.ry = None
        self.width = None
        self.height = None
        self.red = gen_int(config.red)
        self.green = gen_int(config.green) 
        self.blue = gen_int(config.blue)
        self.opacity = gen_float(config.opacity)
        self.shape_name = shape_name.name
        
    def __str__(self) -> str:
        """ Returns the string description of the CircleShape class"""
        return f'{self.shape_name}\nx: {self.x}\ny: {self.y}\nr: {self.rad}\nred: {self.red}\ngreen: {self.green}\nblue: {self.blue}\nopacity: {self.opacity}'

    def write_line(self) -> str:
        """ Returns the formatted string of CircleShape instance that will put into the html file """
        return (f'<circle cx="{self.x}" cy="{self.y}" r="{self.rad}" fill="rgb({self.red},{self.green},{self.blue})" fill-opacity="{self.opacity}"></circle>')

class RectangleShape:
    """ Class to create a rectangle"""
    def __init__(self, config: PyArtConfig, shape_name: Shapes) -> None:
        """ Initalizes the RectangleShape class
                parameters:
                    congig - PyArtConfig, numbers generated from contraints
                    shape_name - Shapes, type of shape
        """
        #generates the elements needed for a Rectangle based on the previously set constraints
        self.x = gen_int(config.viewport)
        self.y = gen_int(config.viewport)
        self.rad = None
        self.rx = None
        self.ry = None
        self.width = gen_int(config.width)
        self.height = gen_int(config.height)
        self.red = gen_int(config.red)
        self.green = gen_int(config.green)
        self.blue = gen_int(config.blue)
        self.opacity = gen_float(config.opacity)
        self.shape_name = shape_name.name
    
    def __str__(self) -> str:
        """ Returns the string description of the RectangleShape class"""
        return f'{self.shape_name}\nx: {self.x}\ny: {self.y}\nwidth: {self.width}\nheight: {self.height}\nred: {self.red}\ngreen: {self.green}\nblue: {self.blue}\nopacity: {self.opacity}'

    def write_line(self) -> str:
        """ Returns the formatted string of RectangleShape instance that will put into the html file """
        return (f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" style="fill:rgb({self.red},{self.green},{self.blue});fill-opacity:{self.opacity}"></rect>')
         
class EllipseShape:
    """ Class to creates a ellipse"""
    def __init__(self, config: PyArtConfig, shape_name: Shapes) -> None:
        """ Initalizes the EllipseShape class
                parameters:
                    congig - PyArtConfig, numbers generated from contraints
                    shape_name - Shapes, type of shape
        """
        #generates the elements needed for a Ellipse based on the previously set constraints
        self.x = gen_int(config.viewport)
        self.y = gen_int(config.viewport)
        self.rad = None
        self.rx = gen_int(config.rx)
        self.ry = gen_int(config.ry)
        self.width = None
        self.height = None
        self.red = gen_int(config.red)
        self.green = gen_int(config.green)
        self.blue = gen_int(config.blue)
        self.opacity = gen_float(config.opacity)
        self.shape_name = shape_name.name

    def __str__(self) -> str:
        """ Returns the string description of the EllipseShape class"""
        return f'{self.shape_name}\nx: {self.x}\ny: {self.y}\nrx: {self.rx}\nry: {self.ry}\nred: {self.red}\ngreen: {self.green}\nblue: {self.blue}\nopactiy: {self.opacity}'

    def write_line(self) -> str:
        """ Returns the formatted string of EllipseShape instance that will put into the html file """
        return (f'<ellipse cx="{self.x}" cy="{self.y}" rx="{self.rx}" ry="{self.ry}" style="fill:rgb({self.red},{self.green},{self.blue})"></ellipse>')

class HtmlDoc:
    """ Class that writes to the html file"""
    IDENTATION = "  "
    def __init__(self, file: str,title: str, canvas_width: int, canvas_height: int) -> None:
        """ Initalizes the class
                parameters:
                    file - str, the name of the file
                    title - str, title of the html document
        """
        self.title = title
        self.__file_name = file
        self.__file: IO = open(self.__file_name,'w')
        self.__indents: int = 0
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.write_header()

    def increase_indent(self) -> None:
        """ increases the indent inside of the html file"""
        self.__indents += 1

    def decrease_indent(self) -> None:
        """ decrease the indent inside of the html file"""
        self.__indents -= 1

    def append(self, content: str) -> None:
        """ appends together the formatted string and the associated number of tabs to be output into html file"""
        self.__file = open(self.__file_name,'a')
        tabs: str = HtmlDoc.IDENTATION * self.__indents
        self.__file.write(f'{tabs}{content}\n')
        self.__file.flush()

    def write_header(self) -> None:
        """ writes the beggining of the html file"""
        self.append('<html>')
        self.append('<head>')
        self.increase_indent()
        self.append(f'<title>{self.title}</title>')
        self.decrease_indent()
        self.append('</head>')
        self.append('<body>')
        self.increase_indent()
        self.append(f'<svg width = "{self.canvas_width}" height="{self.canvas_height}">')

    def end_body(self) -> None:
        """ writes the end of the html file. """
        self.append('</svg>')
        self.decrease_indent()
        self.append('</body>')
        self.append('</html>')

class RandomShape:
    """ Class that determines what shape will randomly be outputted into the html file."""
    def __init__(self, config: PyArtConfig, shape: Shapes) -> None:
        """ Initalizes the class
                Parameters:
                    config: PyArtConfig - shape configurations
                    shape: Shapes - the number associated with the given shape
        """
        self.__config = config
        self.__shape = shape

    def get_shape(self) -> (CircleShape | RectangleShape | EllipseShape | None):
        """ method that gets the actual shape to be outputted into html file"""

        #creates the shape instance based on the random number that was generated
        if(self.__shape.value == 0):
            return CircleShape(config = self.__config,shape_name = self.__shape)
        
        elif(self.__shape.value == 1):
            return RectangleShape(config = self.__config, shape_name = self.__shape)
        
        elif(self.__shape.value == 2):
            return EllipseShape(config = self.__config, shape_name = self.__shape)
    

class SvgCanvas:
    """ Class that writes svg related elements into html file """
    IDENTATION = "  "
    def __init__(self,file: IO, config: PyArtConfig, shape: Shapes, indents: int) -> None:
        """ Initalizes the class
                parameters:
                    file - IO, the html file
                    config - PyArtConfig, the configurations for the shape
                    shape - Shapes,n the type of shape 
                    indents - int, the number of indents used for a line
        """
        self.__file_name = file
        self.__indents = indents

        #the actual shape instance 
        self.__shape_instance = RandomShape(config,shape).get_shape() 

    def append(self, content: str) -> None:
        """ appends together the formatted string and the associated number of tabs to be output into html file
                parameters
                    content - str, the string which contains all formatted shape elements to write to file
        """
        self.__file: IO = open(self.__file_name, 'a')
        tabs: str = SvgCanvas.IDENTATION * self.__indents
        self.__file.write(f'{tabs}{content}\n')
        self.__file.flush()
    
    def increase_indent(self) -> None:
        """ increases the indent inside of the html file"""
        self.__indents += 1

    def decrease_indent(self) -> None:
        """ decreases the indent inside of the html file"""
        self.__indents -= 1

    def mid_body(self) -> None:
        """ writes the actual shape into the html file"""
        self.increase_indent()
        self.increase_indent()
        self.append(self.__shape_instance.write_line())
        
def main() -> None:
    """main method"""

    #gets user input for number of shapes, what types of shapes user wants to generate
    num_shapes: int = int(input("Number of shapes to generate: "))
    shape_type_min: int = int(input("min number for shape type:"))
    shape_type_max: int = int(input("max number for shape type:"))

    #gets user input for how big the svg width and height will be 
    canvas_width: int = int(input("Canvas width:"))
    canvas_height: int = int(input("Canvas height:"))
    viewport: IntRange = IntRange(0,max(canvas_width,canvas_height))
    
    #sets the initial configurations/ constraints set by the user input
    user_input: PyArtConfig = PyArtConfig.from_input(viewport)

    with open('part3.html', 'a') as sys.stdout:
        doc: HtmlDoc = HtmlDoc(file="part3.html", title="My Art Part 3!!",canvas_width=canvas_width, canvas_height=canvas_height)
        while(PyArtConfig.get_count() <= num_shapes + 1):
            range: int = gen_int(IntRange(shape_type_min,shape_type_max)) #generates specified shapes
            #generates shapes within the user specified range
            configurations: PyArtConfig = PyArtConfig(viewport=viewport, rad=user_input.rad,rx=user_input.rx, ry=user_input.ry, width=user_input.width, height=user_input.height, red=user_input.red, green=user_input.green, blue=user_input.blue, opacity=user_input.opacity)
            
            #writes the shape into the html file
            svg: SvgCanvas = SvgCanvas(file="part3.html",config=configurations,shape=Shapes(range),indents=0)
            svg.mid_body()  #writes the middle of the html doc
        doc.end_body()  #writes the end of the html doc
        

    
if __name__ == "__main__":

    main()