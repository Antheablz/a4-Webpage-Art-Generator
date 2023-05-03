from typing import NamedTuple, IO
from enum import Enum
import random as rd
import sys


class Shapes(Enum):
    """ Enum class for different shapes"""
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
    return round(rd.uniform(r.fmin,r.fmax),2) #rounds to 2 decimal places


class PyArtConfig:
    """ Class which sets the configurations for shapes to be displayed"""
    
    counter: int = 0 #counts the number of shapes created
    def __init__(self, x: IntRange, y: IntRange, rad: IntRange, rx: IntRange, ry: IntRange, width: IntRange, height: IntRange, red: Colours.red, green: Colours.green, blue: Colours.blue, opacity: Colours.opacity) -> None:
        """ Initiates the class and sets configurations 
                parameters:
                    x - IntRange, determines random x coordinate of shape within constraints
                    y - IntRange, determines random y coordinate of shape within constraints
                    rad - IntRange, determines random radius of circle
                    rx - IntRange, determines random rx in ellipse within constraints
                    ry - IntRange, determines random ry in ellipse within constraints
                    width - IntRange, determines random width of rectangle within constraints
                    height - IntRange, determines random height of rectangle within constraints
                    red - (Colours.red) IntRange, random determines red rgb number within constraints
                    green - (Colours.green) IntRange, random determines green rgb number within constraints
                    blue - (Colours.blue) IntRange, random determines blue rgb number within constraints
                    opacity - (Colours.opacity) Intrange, random determines the opactiy within constraints
    
        """
        self.x = gen_int(x)
        self.y = gen_int(y)
        self.rad = gen_int(rad)
        self.rx = gen_int(rx)
        self.ry = gen_int(ry)
        self.width = gen_int(width)
        self.height = gen_int(height)
        self.red = gen_int(red)
        self.green = gen_int(green)
        self.blue = gen_int(blue)
        self.opacity = gen_float(opacity)
        PyArtConfig.counter +=1

    
    @classmethod
    def get_count(cls) -> int:
        """ returns the number of shapes"""
        return cls.counter


class CircleShape: 
    """ Class to create a circle"""
    def __init__(self, config: PyArtConfig, shape_name: Shapes) -> None:
        """ Initalizes the CircleShape class
                parameters:
                    congig - PyArtConfig, numbers generated from contraints
                    shape_name - Shapes, type of shape
        """
        self.x = config.x
        self.y = config.y
        self.rad = config.rad
        self.rx = None
        self.ry = None
        self.width = None
        self.height = None
        self.red = config.red
        self.green = config.green
        self.blue = config.blue
        self.opacity = config.opacity
        self.shape_name = shape_name.name
        
    def __str__(self) -> str:
        """ Returns the string description of the CircleShape class"""
        return f'{self.shape_name}\nx: {self.x}\ny: {self.y}\nr: {self.rad}\nred: {self.red}\ngreen: {self.green}\nblue: {self.blue}\nopacity: {self.opacity}'

class RectangleShape:
    """ Class to create a rectangle"""
    def __init__(self, config: PyArtConfig, shape_name: Shapes) -> None:
        """ Initalizes the RectangleShape class
                parameters:
                    congig - PyArtConfig, numbers generated from contraints
                    shape_name - Shapes, type of shape
        """
        self.x = config.x
        self.y = config.y
        self.rad = None
        self.rx = None
        self.ry = None
        self.width = config.width
        self.height = config.height
        self.red = config.red
        self.green = config.green 
        self.blue = config.blue
        self.opacity = config.opacity
        self.shape_name = shape_name.name
    
    def __str__(self) -> str:
        """ Returns the string description of the RectangleShape class"""
        return f'{self.shape_name}\nx: {self.x}\ny: {self.y}\nwidth: {self.width}\nheight: {self.height}\nred: {self.red}\ngreen: {self.green}\nblue: {self.blue}\nopacity: {self.opacity}'


class EllipseShape:
    """ Class to create a ellipse"""
    
    def __init__(self, config: PyArtConfig, shape_name: Shapes) -> None:
        """ Initalizes the EllipseShape class
                parameters:
                    congig - PyArtConfig, numbers generated from contraints
                    shape_name - Shapes, type of shape
        """
        self.x = config.x
        self.y = config.y
        self.rad = None
        self.rx = config.rx
        self.ry = config.ry
        self.width = None
        self.height = None
        self.red = config.red
        self.green = config.green
        self.blue = config.blue
        self.opacity = config.opacity
        self.shape_name = shape_name.name

    def __str__(self) -> str:
        """ Returns the string description of the EllipseShape class"""
        return f'{self.shape_name}\nx: {self.x}\ny: {self.y}\nrx: {self.rx}\nry: {self.ry}\nred: {self.red}\ngreen: {self.green}\nblue: {self.blue}\nopactiy: {self.opacity}'


class HtmlDoc:
    """ Class that writes to the html file"""
    IDENTATION = "  "
    def __init__(self, file: str,title: str) -> None:
        """ Initalizes the class
                parameters:
                    file - str, the name of the file
                    title - str, title of the html document
        """
        self.title = title
        self.__file: IO = open(file,'w')
        self.__indents: int = 0
        self.write_header()

    def increase_indent(self) -> None:
        """ increase the indent inside of the html file"""
        self.__indents += 1

    def decrease_indent(self) -> None:
        """ decrease the indent inside of the html file"""
        self.__indents -= 1

    def append(self, content: str) -> None:
        """ appends together the formatted string and the associated number of tabs to be output into html file"""
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
        self.append("<table>")

    def labels(self) -> None:
        """ writes the labels of the table in the html file"""
        self.increase_indent()
        self.increase_indent()
        self.append("<tr>")
        self.increase_indent()

        self.append("<th>CNT</th>")
        self.append("<th>SHA</th>")
        self.append("<th>X</th>")
        self.append("<th>Y</th>")
        self.append("<th>RAD</th>")
        self.append("<th>RX</th>")
        self.append("<th>RY</th>")
        self.append("<th>W</th>")
        self.append("<th>H</th>")
        self.append("<th>R</th>")
        self.append("<th>G</th>")
        self.append("<th>B</th>")
        self.append("<th>OP</th>")

        self.decrease_indent()
        self.append("</tr>")

class RandomShape:
    """ Class that determines what shape will randomly be outputted into the html file.
            Parameters:
                config: PyArtConfig - shape configurations
                shape: Shapes - the number associated with the given shape
    
    """
    def __init__(self, config: PyArtConfig, shape: Shapes) -> None:
        """Initalizes the class 
                parameters: 
                    config - PyArtConfig, the contraints for the generated shape
                    shape - Shape, the actual type of shape 
        
        """
        self.__config = config
        self.__shape = shape

    def get_shape(self) -> (CircleShape | RectangleShape | EllipseShape | None):
        """ method that gets the actual shape to be outputted """
        
        #finds and creates the shape instance based on the randomly generated number
        if(self.__shape.value == 0):
            return CircleShape(config = self.__config,shape_name = self.__shape)
        
        elif(self.__shape.value == 1):
            return RectangleShape(config = self.__config, shape_name = self.__shape)
        
        elif(self.__shape.value == 2):
            return EllipseShape(config = self.__config, shape_name = self.__shape)


class Table:
    """ class that writes the table into the html file"""
    INDENTATION = "  "
    def __init__(self,file: IO, shape: Shapes, indents: int, config: PyArtConfig) -> None:
        """Initalizes the class
                parameters:
                    file - IO, the html file
                    shapes - Shapes, the type of shape 
                    indents - int, the number of indents needed (if its greater than 1)
                    config - PyArtConfig, The configurations/constraints for each shape
        """
        self.__file: IO = open(file, 'a')
        self.__config = config
        self.__indents = indents

        #gets the instance of the random shape 
        self.__shape_instance = RandomShape(config,shape).get_shape() #self.get_shape() #create instance of class here
    
    def increase_indent(self) -> None:
        """ increases the indent inside of the html file"""
        self.__indents += 1

    def decrease_indent(self) -> None:
        """ decreases the indent inside of the html file"""
        self.__indents -= 1

    def append(self, content: str) -> None:
        """ appends together the formatted string and the associated number of tabs to be output into html file"""
        tabs: str = Table.INDENTATION * self.__indents
        self.__file.write(f'{tabs}{content}\n')
        self.__file.flush()

    def elements(self) -> None:
        """ writes the actual table elements in the html file"""
        self.increase_indent()
        self.increase_indent()
        self.increase_indent()
        self.append("<tr>")
        self.increase_indent()

        #appends the actual labels for each table column
        self.append(f"<td>{self.__config.get_count()}")
        self.append(f"<td>{self.__shape_instance.shape_name}</td>")
        self.append(f"<td>{self.__shape_instance.x}</td>")
        self.append(f"<td>{self.__shape_instance.y}</td>")
        self.append(f"<td>{self.__shape_instance.rad}</td>")
        self.append(f"<td>{self.__shape_instance.rx}</td>")
        self.append(f"<td>{self.__shape_instance.ry}</td>")
        self.append(f"<td>{self.__shape_instance.width}</td>")
        self.append(f"<td>{self.__shape_instance.height}</td>")
        self.append(f"<td>{self.__shape_instance.red}</td>")
        self.append(f"<td>{self.__shape_instance.green}</td>")
        self.append(f"<td>{self.__shape_instance.blue}</td>")
        self.append(f"<td>{self.__shape_instance.opacity}</td>")


        self.decrease_indent()
        self.append("</tr>")
    
    def end(self) -> None:
        """ Ends the table block and the html file """
        self.decrease_indent()
        self.append("</table>")
        self.decrease_indent()
        self.append("</body>")
        self.append("</html>")
        
def main() -> None:
    """main method"""
    
    with open('part2.html', 'a') as sys.stdout:
        range: int = gen_int(IntRange(0,2)) #generates the random 
        doc = HtmlDoc(file="part2.html", title="My Table Part 2!!")
        doc.labels() #writes the labels for columns of table

        while (PyArtConfig.get_count() < 10):
            range: int = gen_int(IntRange(0,2))

            #creates shapes based on the configurations
            configurations: PyArtConfig = PyArtConfig(x=IntRange(0,1000), y=IntRange(0,1000), rad=IntRange(0,100),rx=IntRange(10,30), ry=IntRange(10,30), width=IntRange(10,100), height=IntRange(10,100), red=IntRange(0,255), green=IntRange(0,255), blue=IntRange(0,255), opacity=FloatRange(0.0,1.0))
            table = Table(file="part2.html", shape=Shapes(range), indents=0,config=configurations)
            table.elements() #writes all the elements in the table into html file
        table.end() #writes the end of the html file
if __name__ == "__main__":
    main()