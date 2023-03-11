from pprint import pprint
import Rhino
import scriptcontext
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import math
import Rhino.UI
import Eto.Drawing as drawing
import Eto.Forms as forms

class SampleEtoHouseDialog(forms.Dialog[bool]):
 
    # Dialog box Class initializer
    def __init__(self):

        #parameters to export
        self.start_point = []

        

        # Initialize dialog box
        self.Title = 'High Building Configurator'
        self.Padding = drawing.Padding(10)
        self.Resizable = True
 
        # Create labels for the dialog
        self.start_point = forms.Label(Text = 'Select start points of  building:')
        self.number_cloum_x = forms.Label(Text = 'Select number of cloumn x axes:')
        self.number_cloum_y = forms.Label(Text= 'Select number of cloumn y axes:')
        self.distances_cloum_x = forms.Label(Text = 'Select distances cloum x axes:')
        self.distances_cloum_y = forms.Label(Text= 'Select distances cloum y axes:')
        self.floor_number = forms.Label(Text = 'Select floor number of building(the number have to be bigger than 7 ):')
        self.height_of_floor = forms.Label(Text = 'Select height of floor :')
        self.start_empty_floor = forms.Label(Text= 'Select starting point of empty floor:')
        self.middle_empty_point = forms.Label(Text = 'Select middle empty point:')



        self.start_pointX_label = forms.Label(Text = 'X:')
        self.start_pointY_label = forms.Label(Text = 'Y:')
        self.start_pointZ_label = forms.Label(Text = 'Z:')

        self.number_cloum_x_label = forms.Label(Text = 'Select number of cloumn x axes:')
        self.number_cloum_y_label = forms.Label(Text = 'Select number of cloumn y axes:')
        self.distances_cloum_x_label = forms.Label(Text = 'Select distances cloum x axes:')
        self.distances_cloum_y_label = forms.Label(Text = 'Select distances cloum y axes:')
        self.floor_number_label = forms.Label(Text = 'Select floor number of building(the number have to be bigger than 7 ):')
        self.height_of_floor_label = forms.Label(Text = 'Select height of floor :')
        self.start_empty_floor_label = forms.Label(Text = 'Select starting point of empty floor:')
        self.middle_empty_point_label = forms.Label(Text = 'Select middle empty point:')



        # Create the input dialogs
        self.start_pointX = forms.TextBox(Text = None)
        self.start_pointY = forms.TextBox(Text = None)
        self.start_pointZ = forms.TextBox(Text = None)
        self.number_cloum_x = forms.TextBox(Text = None)
        self.number_cloum_y  = forms.TextBox(Text = None)
        self.distances_cloum_x = forms.TextBox(Text = None)
        self.distances_cloum_y = forms.TextBox(Text = None)
        self.floor_number  = forms.TextBox(Text = None)
        self.height_of_floor  = forms.TextBox(Text = None)
        self.start_empty_floor  = forms.TextBox(Text = None)
        self.middle_empty_point  = forms.TextBox(Text = None)
        
        # On button Clicks events
 
        # Create the submit and abort button
        self.SubmitButton = forms.Button(Text = 'Submit')
        self.SubmitButton.Click += self.OnSubmitButtonClick
        self.AbortButton = forms.Button(Text = 'Cancel')
        self.AbortButton.Click += self.OnCloseButtonClick


        # Create a table layout and add all the controls
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(45, 10)
        layout.AddRow(self.start_point)
        layout.BeginVertical()
        layout.AddRow(self.start_pointX_label,
                      self.start_pointX,
                      self.start_pointY_label,
                      self.start_pointY,
                      self.start_pointZ_label, 
                      self.start_pointZ)
        layout.EndVertical()


        layout.AddRow(self.number_cloum_x)
        layout.BeginVertical()
        layout.AddRow(self.number_cloum_x_label, self.number_cloum_x )
        layout.EndVertical()

        layout.AddRow(self.number_cloum_y)
        layout.BeginVertical()
        layout.AddRow(self.number_cloum_y_label,self.number_cloum_y) 
        layout.EndVertical()

        layout.AddRow(self.distances_cloum_x)
        layout.BeginVertical()
        layout.AddRow(self.distances_cloum_x_label ,self.number_cloum_y)
        layout.EndVertical()

        layout.AddRow(self.distances_cloum_y)
        layout.BeginVertical()
        layout.AddRow(self.distances_cloum_y_label , self.distances_cloum_y)
        layout.EndVertical()

        layout.AddRow(self.floor_number)
        layout.BeginVertical()
        layout.AddRow(self.floor_number_label, self.floor_number)
        layout.EndVertical()

        layout.AddRow(self.height_of_floor)
        layout.BeginVertical()
        layout.AddRow(self.height_of_floor_label, self.height_of_floor)
        layout.EndVertical()

        layout.AddRow(self.start_empty_floor)
        layout.BeginVertical()
        layout.AddRow(self.start_empty_floor_label, self.start_empty_floor)
        layout.EndVertical() 

        layout.AddRow(self.middle_empty_point)
        layout.BeginVertical()
        layout.AddRow(self.middle_empty_point_label , self.middle_empty_point)
        layout.EndVertical() 


        layout.AddRow(None) # spacer

        layout.AddRow(self.SubmitButton, self.AbortButton)
 
        # Set the dialog content
        self.Content = layout
 
    # Start of the class functions

    #Select points from Rhino and return to dialog


    def SelectPtsButtonClick(self, sender, e):
        Rhino.UI.EtoExtensions.PushPickButton(self, self.OnGetRhinoObjects)
        
    def making_start_point(self):
        self.start_point = [float(self.start_pointX.Text), 
                          float(self.start_pointY.Text), 
                          float(self.start_pointZ.Text)]

    def making_x_cloumn(self):
        self.number_cloum_x = float(self.number_cloum_x.Text)

    def making_y_cloumn(self):
        self.number_cloum_y = float(self.number_cloum_y.Text) 

    def distance_x_cloumn(self):
        self.distances_cloum_x = float(self.distances_cloum_x.Text)

    def distance_y_cloumn(self):
        self.distances_cloum_y = float(self.distances_cloum_y.Text)

    def floor_numbera(self):
        self.floor_number = float(self.floor_number.Text)

    def height_of_floora(self):
        self.height_of_floor = float(self.height_of_floor.Text)

    def start_empty_floora(self):
        self.start_empty_floor = float(self.start_empty_floor.Text)

    def middle_empty_pointa(self):
        self.middle_empty_point = float(self.middle_empty_point.Text)


    # Get the value of the parameters
    def get_start_point(self):
        return self.start_point

    def get_number_cloum_x(self):
        return self.number_cloum_x

    def get_number_cloum_y(self):
        return self.number_cloum_y
    
    def get_distances_cloum_x(self):
        return self.distances_cloum_x

    def get_distances_cloum_y(self):
        return self.distances_cloum_y

    def get_floor_number(self):
        return self.floor_number

    def get_height_of_floor(self):
        return self.height_of_floor
    
    def get_start_empty_floor(self):
        return self.start_empty_floor

    def get_middle_empty_point(self):
        return self.middle_empty_point


    # Close button click handler
    def OnCloseButtonClick(self, sender, e):
        self.Close(False)

    # Submit button click handler
    def OnSubmitButtonClick(self, sender, e):
        #Save info
        self.making_start_point()
        self.making_x_cloumn()
        self.making_y_cloumn()
        self.distance_x_cloumn()
        self.distance_y_cloumn()
        self.floor_numbera()
        self.height_of_floora()
        self.start_empty_floora()
        self.middle_empty_pointa()

        if self.start_point and self.number_cloum_x and self.number_cloum_y and self.distances_cloum_x and self.distances_cloum_y and self.floor_number and self.height_of_floor and self.start_empty_floor and self.middle_empty_point:
            self.Close(True)
        else:
            self.Close(False)
 
## End of Dialog Class ##
 
# The script that will be using the dialog.
def RequestHouseGenerator():
    dialog = SampleEtoHouseDialog()
    rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)

    if (rc): 
        start_point = dialog.get_start_point()
        number_cloum_x = dialog.get_number_cloum_x()
        number_cloum_y = dialog.get_number_cloum_y()
        distances_cloum_x = dialog.get_distances_cloum_x()
        distances_cloum_y = dialog.get_distances_cloum_y()
        floor_number = dialog.get_floor_number()
        height_of_floor = dialog.get_height_of_floor()
        start_empty_floor = dialog.get_start_empty_floor()
        middle_empty_point = dialog.get_middle_empty_point()


        #print ("pts", list_pt)
        #print ("ext", extrusion)
        #print ("origin", origin)

        return start_point, number_cloum_x, number_cloum_y, distances_cloum_x, distances_cloum_y,floor_number,height_of_floor,start_empty_floor,middle_empty_point
    else:
        print("Invalid inputs! Please try again.")
        return None, None, None



class making_high_building():

    def __init__(self, start_point,number_cloum_x,number_cloum_y,distances_cloum_x,distances_cloum_y,floor_number,height_of_floor,start_empty_floor,middle_empty_point):
        self.start_point = start_point
        self.number_cloum_x =  distances_cloum_x
        self.number_cloum_y =  number_cloum_x
        self.distances_cloum_x = number_cloum_y
        self.distances_cloum_y = distances_cloum_y
        self.floor_number = floor_number
        self.height_of_floor = height_of_floor

        self.start_empty_floor = start_empty_floor
        self.middle_empty_point  = middle_empty_point


    ## creating point for construction element 
    def making_point_floor(self,floor_number):

        height = floor_number*self.height_of_floor
        first_floor = []
        a = self.start_point[0]
        start_point_floor = (self.start_point[0],self.start_point[1],self.start_point[2]+ height)
        for i in range(int(self.number_cloum_x)):
            y_axes = []
            next_point_x= []
            next_point_x = [a ,start_point_floor[1],start_point_floor[2]]
            a += self.distances_cloum_x
#            rs.AddPoint(next_point_x)
            
            b = next_point_x[1] 

            y_axes.append(next_point_x)
            for i in range(int(self.number_cloum_y-1)):
                b += self.distances_cloum_y
                next_point_y = [next_point_x[0],b, next_point_x[2]]
#                rs.AddPoint(next_point_y)
                y_axes.append(next_point_y)
            first_floor.append(y_axes)

        return first_floor

    def making_point_all_floors(self):
        floors = []
        
        for i in range(int(self.floor_number)):
            floor = self.making_point_floor(i)
            floors.append(floor)
        return floors
    
    def drawing_column(self):
        pointlist = self.making_point_all_floors()
        columns = []

        for i in range(int(self.floor_number)):
            column_floor = []
            for j in range(int(self.number_cloum_x)):
                column_x = []
                for k in range(int(self.number_cloum_y)):
                    if i < self.floor_number -1  :
                        line = rs.AddLine(pointlist[i][j][k],pointlist[i+1][j][k])
##                        rect = rs.AddRectangle((pointlist[i][j][k]), self.column_y, self.column_x)
##                        column = rs.ExtrudeCurve(rect,line ) 
                        column_x.append(line)
                column_floor.append(column_x)
            columns.append(column_floor)
            
        return columns
    
    def drawing_beams_x(self):
        pointlist = self.making_point_all_floors()
 
        beamx = []

        for i in range(int(self.floor_number)):
            beam_floor = []
            for j in range(int(self.number_cloum_x)):
                beam_x = []
                for k in range(int(self.number_cloum_y)):
                    if k < self.number_cloum_y-1 : 
##                        rect = self.drawing_rectengle_yz((pointlist[i][j][k]),self.beam_x,self.beam_y)
                        line = rs.AddLine((pointlist[i][j][k]), (pointlist[i][j][k+1]))
##                        beam = rs.ExtrudeCurve(rect,line)
                        beam_x.append(line)
                beam_floor.append(beam_x)
            beamx.append(beam_floor)


        return beamx

    def drawing_beams_console(self):
        pointlist = self.making_point_all_floors()
 
        beamx = []

        for i in range(int(self.floor_number)):
            beam_floor = []
            for x in range(int(self.number_cloum_x)):
                beam_x = []
                for y in range(int(self.number_cloum_y)):
                    middle = int((3*self.number_cloum_x)/self.middle_empty_point) 

                    start = self.start_empty_floor -1
                    
                    # deleting cross beams     
                    if i in [start+1, start+2] and x ==0 and y == 0:
                        continue

                    if i in [start+4,start+5] and x == self.number_cloum_x-1 and y == self.number_cloum_y-1:
                        continue
                    
                    #deleting facede beams y axes 
                    if i in [start+2] and x == 0 and y > middle - 1:
                        continue

                    if i in [start+1] and x == 0 and y < middle :
                        continue
                    
                    
                    if i in [start+4] and x == self.number_cloum_x-1  and y > middle - 1:
                        continue

                    if i in [start+3] and x == self.number_cloum_x-1 and y < middle :
                        continue

                    #deleting facede beams x axes 
                    if i in [start+1] and x < middle and y == 0  :
                        continue
                    if i in [start+2] and x > middle-1  and y == 0 :
                        continue
                    if i in [start+3] and x < middle and y == self.number_cloum_y-1 :
                        continue
                    if i in [start+4] and x > middle-1  and y == self.number_cloum_y-1 :
                        continue



                    if y == 0  : 
                        pointa = pointlist[i][x][y]
                        pointb= (pointa[0],pointa[1]-self.distances_cloum_y/3,pointa[2])
                        line = rs.AddLine(pointa,pointb)
                        beam_x.append(line)

                    if y == self.number_cloum_y-1 :
                        pointa = pointlist[i][x][y]
                        pointb= (pointa[0],pointa[1]+self.distances_cloum_y/3,pointa[2])
                        line = rs.AddLine(pointa,pointb)
                        beam_x.append(line)

                    if x == 0 :
                        pointa = pointlist[i][x][y]
                        pointb= (pointa[0]-self.distances_cloum_x/3,pointa[1],pointa[2])
                        line = rs.AddLine(pointa,pointb)
                        beam_x.append(line)

                    if x == self.number_cloum_x-1 :
                        pointa = pointlist[i][x][y]
                        pointb= (pointa[0]+self.distances_cloum_x/3,pointa[1],pointa[2])
                        line = rs.AddLine(pointa,pointb)
                        beam_x.append(line)

                beam_floor.append(beam_x)
            beamx.append(beam_floor)

        return beamx
        
    def drawing_beams_y(self):
        pointlist = self.making_point_all_floors()

        beamy = []
        for i in range(int(self.floor_number)):
            beam_floor = []
            for j in range(int(self.number_cloum_x)):
                beam_x = []
                for k in range(int(self.number_cloum_y)):
                    if j < self.number_cloum_x-1 : 
##                        rect = self.drawing_rectengle_xz((pointlist[i][j][k]),self.beam_x,self.beam_y)
                        line = rs.AddLine((pointlist[i][j][k]), (pointlist[i][j+1][k]))
###                        beam = rs.ExtrudeCurve(rect,line)
                        beam_x.append(line)
                beam_floor.append(beam_x)
            beamy.append(beam_floor)


        return beamy

    def floor_point(self,floor_number):
        point = self.start_point
        start_point_floor = (point[0] - (self.distances_cloum_x/3) ,point[1] - (self.distances_cloum_y/3),point[2])

        height = floor_number*self.height_of_floor
        first_floor = []
        a = start_point_floor[0]
        start_point_floora = (start_point_floor[0],start_point_floor[1],start_point_floor[2]+ height)
        for i in range(int(self.number_cloum_x)*3):
            y_axes = []
            next_point_x= []
            next_point_x = [a ,start_point_floora[1],start_point_floora[2]]
            a += self.distances_cloum_x/3
###            rs.AddPoint(next_point_x)
            
            b = next_point_x[1] 

            y_axes.append(next_point_x)
            for i in range(int(self.number_cloum_y)*3-1):
                b += self.distances_cloum_y/3
                next_point_y = [next_point_x[0],b, next_point_x[2]]
###                rs.AddPoint(next_point_y)
                y_axes.append(next_point_y)
            first_floor.append(y_axes)

        return first_floor

    def drawing_rectengla(self,numberfloor):
        vector = rs.AddLine((0,0,0),(0,0,1.5))
        points = self.floor_point(numberfloor)
        plane = rs.WorldXYPlane()
        rectangle = [] 
        for i in range(len(points)-1):
            rectangleX = []
            for j in range(len(points[0])-1):
                point = points[i][j]
                object = rs.AddRectangle(plane,self.distances_cloum_x/3,self.distances_cloum_y/3)
                object_ = rs.MoveObject(object,point)
##                object1 = rs.AddPlanarSrf(object_)
##                object2 = rs.ExtrudeSurface(object1,vector)
                rectangleX.append(object_)

            rectangle.append(rectangleX)
        return rectangle

    def drawing_allrectangles(self):
        rectangles = []
        for i in range(int(self.floor_number)):
            rectangle = self.drawing_rectengla(i)
            rectangles.append(rectangle)
        return rectangles

## deleting some part and getting final shape

    def final_floor(self):



        rectengles = self.drawing_allrectangles()
        remaining_rectengles = []
        start = int(self.start_empty_floor) -1 
        middle_point = 5 
        for floor in range(len(rectengles)):
            each_floor = []
            for x in range(len(rectengles[0])):
                rectengle_X = []
                for y in range(len(rectengles[0][0])):
                    rectengle = rectengles[floor][x][y]


                    if floor == start + 1  and x == 0 and y < int(self.middle_empty_point)+1 :
                        rs.DeleteObject(rectengle)
                    if floor == start + 2 and x == 0 and y > int(self.middle_empty_point) :
                        rs.DeleteObject(rectengle)


                    if floor == start +3 and x == len(rectengles[0])-1 and y < int(self.middle_empty_point)  : 
                        rs.DeleteObject(rectengle)
                    if floor == start + 4 and x == len(rectengles[0])-1 and y > int(self.middle_empty_point) :
                        rs.DeleteObject(rectengle)


                    if floor == start +1 and x < int(self.middle_empty_point) and y == 0 :
                        rs.DeleteObject(rectengle)
                    if floor == start + 2 and  x > int(self.middle_empty_point)-1 and y == 0:
                        rs.DeleteObject(rectengle)


                    if floor == start +3 and  x < int(self.middle_empty_point) and y == len(rectengles[0][0])-1:
                        rs.DeleteObject(rectengle)
                    if floor == start + 4 and x > int(self.middle_empty_point)-1  and y == len(rectengles[0][0])-1 :
                        rs.DeleteObject(rectengle)

    
                    #first edge point
                    if floor == start and x == 0 and y == 0 :
                        rs.DeleteObject(rectengle)
                    if floor == start+2 and (x in [0,1,2]) and (y in [0,1]):
                        rs.DeleteObject(rectengle)
                    if floor == start+1 and (x in [0,1]) and (y in [0,1,2]):
                        rs.DeleteObject(rectengle)
                    if floor == start + 3  and x == 0 and y == 0:
                        rs.DeleteObject(rectengle)


                    #second edge point
                    a = len(rectengles[0])
                    b = len(rectengles[0][0])
                    if floor == start +3  and x == a-1 and y == b-1 :
                        rs.DeleteObject(rectengle)

                    if floor == start+ 5 and (x in [a-1,a-2,a-3]) and (y in [b-1,b-2,b-3]):
                        rs.DeleteObject(rectengle)
                    if floor == start+ 4  and (x in [a-1,a-2]) and (y in [b-1,b-2,b-3]):
                        rs.DeleteObject(rectengle)
                    if floor == start + 6   and x == a-1 and y == b-1 :
                        rs.DeleteObject(rectengle)


                    #roof deleting system
                    if (floor in list(range(start+4,len(rectengles)))) and (x in (int(a/2)-1,int(a/2),int(a/2)+1)) and (y in (int(b/2)-1,int(b/2),int(b/2)+1)):
                        rs.DeleteObject(rectengle)
                    if (floor in list(range(start+7,len(rectengles)))) and (x in [int(a/2)-2] ) and (y in [int(b/2)+1] ):
                        rs.DeleteObject(rectengle)
                    if (floor in list(range(start+8,len(rectengles)))) and (x in [int(a/2)+2] ) and (y in [int(b/2)] ):
                        rs.DeleteObject(rectengle)
                    if (floor in list(range(start+6,len(rectengles)))) and (x in [int(a/2)+1] ) and (y in [int(b/2)+2] ):
                        rs.DeleteObject(rectengle)
                    if (floor in list(range(start+8,len(rectengles)))) and (x in [int(a/2)] ) and (y in [int(b/2)+2] ):
                        rs.DeleteObject(rectengle)                    

                    else :
                        rectengle_X.append(rectengle)               


                each_floor.append(rectengle_X)
            remaining_rectengles.append(each_floor)
        
        return remaining_rectengles  

    def final_support_beam(self):
        support = []
        start = self.start_empty_floor -1 
        points = self.making_point_all_floors()  
        for floor in range(len(points)):
            for x in range(len(points[0])):
                for y in range(len(points[0][0])):
                    
                    if  floor in [start + 3] and x == self.number_cloum_x - 1 and y == self.number_cloum_y - 1  :
                        continue



                    # x axses suppor beams
                    
                    if floor in [start + 6, start + 3] and y in [0, len(points[0][0])-1] and x in list(range(len(points[0])-1)) :
                        pointa = points[floor][x][y]
                        pointb = points[floor+1][x][y]
                        point_bb = (pointb[0]+self.distances_cloum_x/2,pointb[1],pointb[2])
                        beam  = rs.AddLine(pointa,point_bb)
                        support.append(beam)
                    
                    if  floor in [start + 6, start + 3] and y in [0, len(points[0][0])-1] and x in list(range(1,len(points[0]))) :

                        pointa = points[floor][x][y]
                        pointb = points[floor+1][x][y]
                        point_bb = (pointb[0]-self.distances_cloum_x/2,pointb[1],pointb[2])
                        beam  = rs.AddLine(pointa,point_bb)
                        support.append(beam)
                    
                    # y axes suppor beam
                    if  floor in [start + 6, start + 3] and x in [0, len(points[0])-1] and y in list(range(1,len(points[0][0]))) :
                        pointa = points[floor][x][y]
                        pointb = points[floor+1][x][y]
                        point_bb = (pointb[0],pointb[1]-self.distances_cloum_y/2,pointb[2])
                        beam  = rs.AddLine(pointa,point_bb)
                        support.append(beam)

                    if  floor in [start + 6, start + 3]and x in [0, len(points[0])-1] and y in list(range(0,len(points[0][0])-1)) :
                        
                        pointa = points[floor][x][y]
                        pointb = points[floor+1][x][y]
                        point_bb = (pointb[0],pointb[1]+self.distances_cloum_y/2,pointb[2])
                        beam  = rs.AddLine(pointa,point_bb)
                        support.append(beam)


        return support

    def final_cloumn(self):

        start = self.start_empty_floor -1 

        cloumns = self.drawing_column()
        remaing_cloumns = []
        for floor in range(len(cloumns)-1):
            for x in range(len(cloumns[0])):
                for y in range(len(cloumns[0][0])):
                    cloumn = cloumns[floor][x][y]
                    ## first edge deleting cloumns 
                    if (floor in [start, start +1 , start + 2 ]) and x == 0 and y == 0 :
                        rs.DeleteObject(cloumn)
                    if (floor in [start+3, start +4 , start + 5 ]) and x == len(cloumns[0])-1 and y == len(cloumns[0][0])-1: 
                        rs.DeleteObject(cloumn)

                    else :
                        remaing_cloumns.append(cloumn)

    def final_beam(self):
        start = int(self.start_empty_floor) -1 

        beamsx = self.drawing_beams_x()
        beamsy = self.drawing_beams_y()
        support_console = self.drawing_beams_console()
        remaing_beams  = []
        for floor in range(len(beamsx)):
            for x in range(len(beamsx[0])):
                for y in range(len(beamsx[0][0])):
                               beam = beamsx[floor][x][y]
                               if floor in [start+1, start +2] and x ==0 and y == 0 :
                                   rs.DeleteObject(beam)
                               if floor in [start+4, start +5] and x == len(beamsx[0]) -1  and y == len(beamsx[0][0])-1 :
                                   rs.DeleteObject(beam)                                   

                               else :
                                   remaing_beams.append(beam)

        for floor in range(len(beamsy)):
            for x in range(len(beamsy[0])-1):
                for y in range(len(beamsy[0][0])):
                               beam = beamsy[floor][x][y]
                               if floor in [start+1, start +2] and x ==0 and y == 0 :
                                   rs.DeleteObject(beam)
                               if floor in [start+4, start +5] and x == len(beamsy[0]) -2 and y == len(beamsy[0][0])-1 :
                                   rs.DeleteObject(beam)                                   

                               else :
                                   remaing_beams.append(beam)
        
        
        return remaing_beams


if __name__=="__main__":

    start_point,number_cloum_x,number_cloum_y,distances_cloum_x,distances_cloum_y,floor_number,height_of_floor,start_empty_floor,middle_empty_point = RequestHouseGenerator()


    #rs.DeleteObjects(rs.AllObjects())
    
    #input list house front facade profile
    #list_pt1 = [ [0,0,0], [0,0,3], [1.5,0,4], [3,0,3], [3,0,0] ]

    # creating house object
    Building1 = making_high_building(start_point,number_cloum_x,number_cloum_y,distances_cloum_x,distances_cloum_y,floor_number,height_of_floor,start_empty_floor,middle_empty_point)

    Building1.final_cloumn()
    Building1.final_beam()
    Building1.final_support_beam()
    Building1.final_floor()

    # optional
    # in case if you have more houses you can init them and store the in a list to loop through them.
    # storing the house objects in a list to loop through them

