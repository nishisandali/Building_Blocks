
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9878831
#    Student name: DEENALATHTHAGE HESHANKA SANDALI DEENALATTHA
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  BUILDING BLOCKS
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "stack_blocks".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a pile of building blocks
#  whose arrangement is determined by data stored in a list which
#  specifies the blocks' locations.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

block_size = 250 # pixels
top_and_bottom_border = 75 # pixels
left_and_right_border = 150 # pixels
canvas_width = (block_size + left_and_right_border) * 2
canvas_height = (block_size + top_and_bottom_border) * 2

#
#--------------------------------------------------------------------#



#-----Functions for Managing the Canvas------------------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Set the coordinate system so that location (0, 0) is centred on
    # the point where the blocks will be stacked
    setworldcoordinates(-canvas_width / 2, -top_and_bottom_border,
                        canvas_width / 2, canvas_height - top_and_bottom_border)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 50 # pixels
    penup()
    goto(-(canvas_width / 2 + overlap), -(top_and_bottom_border + overlap)) # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(top_and_bottom_border + overlap)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(top_and_bottom_border + overlap)
    end_fill()
    penup()

    # Draw a friendly sun peeking into the image
    goto(-canvas_width / 2, block_size * 2)
    color('yellow')
    dot(250)

    # Reset everything ready for the student's solution
    color('black')
    width(1)
    penup()
    home()
    setheading(0)
    tracer(True)
    

# As a debugging aid, mark the coordinates of the centres and corners
# of the places where the blocks will appear
def mark_coords(show_corners = False, show_centres = False):

    # Go to each coordinate, draw a dot and print the coordinate, in the given colour
    def draw_each_coordinate(colour):
        color(colour)
        for x_coord, y_coord in coordinates:
            goto(x_coord, y_coord)
            dot(4)
            write(' ' + str(x_coord) + ', ' + str(y_coord), font = ('Arial', 12, 'normal'))

    # Don't draw lines between the coordinates
    penup()

    # The list of coordinates to display
    coordinates = []

    # Only mark the corners if the corresponding argument is True
    if show_corners:
        coordinates = [[-block_size, block_size * 2], [0, block_size * 2], [block_size, block_size * 2],
                       [-block_size, block_size], [0, block_size], [block_size, block_size],
                       [-block_size, 0], [0, 0], [block_size, 0]]
        draw_each_coordinate('dark blue')

    # Only mark the centres if the corresponding argument is True
    if show_centres:
        coordinates = [[-block_size / 2, block_size / 2], [block_size / 2, block_size / 2],
                       [-block_size / 2, block_size + block_size / 2], [block_size / 2, block_size + block_size / 2]]
        draw_each_coordinate('red')

    # Put the cursor back how it was
    color('black')
    home()


# End the program by hiding the cursor and releasing the window
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# the building blocks:
#
# 1. The name of the block, from 'Block A' to 'Block D'
# 2. The place to put the block, either 'Top left', 'Top right',
#    'Bottom left' or 'Bottom right'
# 3. The block's orientation, meaning the direction in which the top
#    of the block is pointing, either 'Up', 'Down', 'Left' or 'Right'
# 4. An optional mystery value, 'X' or 'O', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily mention all four blocks.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#

# The following data set doesn't require drawing any blocks
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

arrangement_00 = []

# Each of the following data sets specifies drawing just one block
# in an upright orientation.  You may find them useful when
# creating your individual pieces.

arrangement_01 = [['Block A', 'Bottom left', 'Up', 'O']]
arrangement_02 = [['Block B', 'Bottom right', 'Up', 'O']]
arrangement_03 = [['Block C', 'Bottom left', 'Up', 'O']]
arrangement_04 = [['Block D', 'Bottom right', 'Up', 'O']]

# Each of the following data sets specifies drawing just one block
# in non-upright orientations.  You may find them useful when
# ensuring that you can draw all the blocks facing in different
# directions.

arrangement_10 = [['Block A', 'Bottom left', 'Down', 'O']]
arrangement_11 = [['Block A', 'Bottom right', 'Left', 'O']]
arrangement_12 = [['Block A', 'Bottom left', 'Right', 'O']]

arrangement_13 = [['Block B', 'Bottom left', 'Down', 'O']]
arrangement_14 = [['Block B', 'Bottom right', 'Left', 'O']]
arrangement_15 = [['Block B', 'Bottom left', 'Right', 'O']]

arrangement_16 = [['Block C', 'Bottom left', 'Down', 'O']]
arrangement_17 = [['Block C', 'Bottom right', 'Left', 'O']]
arrangement_18 = [['Block C', 'Bottom left', 'Right', 'O']]

arrangement_19 = [['Block D', 'Bottom left', 'Down', 'O']]
arrangement_20 = [['Block D', 'Bottom right', 'Left', 'O']]
arrangement_21 = [['Block D', 'Bottom left', 'Right', 'O']]

# The following data sets all stack various numbers of
# blocks in various orientations

arrangement_30 = [['Block C', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Top right', 'Up', 'O']]

arrangement_32 = [['Block B', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Bottom left', 'Up', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]
arrangement_33 = [['Block B', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Bottom left', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O']]
arrangement_34 = [['Block B', 'Bottom left', 'Up', 'O'],
                  ['Block A', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Top left', 'Up', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]

arrangement_40 = [['Block C', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top right', 'Right', 'O']]
arrangement_41 = [['Block A', 'Bottom left', 'Down', 'O'],
                  ['Block C', 'Bottom left', 'Up', 'O']]

arrangement_42 = [['Block B', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block C', 'Top right', 'Down', 'O']]
arrangement_43 = [['Block B', 'Bottom right', 'Right', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block A', 'Top left', 'Right', 'O']]
arrangement_44 = [['Block B', 'Bottom left', 'Down', 'O'],
                  ['Block A', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top left', 'Right', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]

arrangement_50 = [['Block B', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block C', 'Top right', 'Down', 'X']]
arrangement_51 = [['Block B', 'Bottom right', 'Right', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block A', 'Top left', 'Right', 'X']]
arrangement_52 = [['Block B', 'Bottom left', 'Down', 'O'],
                  ['Block A', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top left', 'Right', 'O'],
                  ['Block C', 'Top right', 'Up', 'X']]

arrangement_60 = [['Block B', 'Bottom right', 'Left', 'X'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block C', 'Top right', 'Down', 'O']]
arrangement_61 = [['Block B', 'Bottom right', 'Right', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'X'],
                  ['Block A', 'Top left', 'Right', 'O']]
arrangement_62 = [['Block B', 'Bottom left', 'Down', 'X'],
                  ['Block A', 'Bottom right', 'Left', 'X'],
                  ['Block D', 'Top left', 'Right', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]

# The following arrangements create your complete image, but
# oriented the wrong way

arrangement_80 = [['Block C', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top right', 'Left', 'X'],
                  ['Block A', 'Bottom left', 'Left', 'O'],
                  ['Block B', 'Top left', 'Left', 'O']]

arrangement_81 = [['Block B', 'Bottom right', 'Right', 'X'],
                  ['Block D', 'Bottom left', 'Right', 'X'],
                  ['Block A', 'Top right', 'Right', 'O'],
                  ['Block C', 'Top left', 'Right', 'O']]

arrangement_89 = [['Block A', 'Bottom right', 'Down', 'O'],
                  ['Block C', 'Top right', 'Down', 'O'],
                  ['Block B', 'Bottom left', 'Down', 'O'],
                  ['Block D', 'Top left', 'Down', 'O']]

# The following arrangements should create your complete image
# (but with the blocks stacked in a different order each time)

arrangement_90 = [['Block C', 'Bottom left', 'Up', 'O'],
                  ['Block D', 'Bottom right', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'X'],
                  ['Block A', 'Top left', 'Up', 'O']]

arrangement_91 = [['Block D', 'Bottom right', 'Up', 'X'],
                  ['Block C', 'Bottom left', 'Up', 'X'],
                  ['Block A', 'Top left', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'O']]

arrangement_92 = [['Block D', 'Bottom right', 'Up', 'X'],
                  ['Block B', 'Top right', 'Up', 'O'],
                  ['Block C', 'Bottom left', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O']]

arrangement_99 = [['Block C', 'Bottom left', 'Up', 'O'],
                  ['Block D', 'Bottom right', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'O']]

#
#--------------------------------------------------------------------# 

#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "stack_blocks" function.
#

#coordinates
x = 0
y = 250
outline = []

#black border outline
def draw(outline):
    color('black')
    width(4)
    pendown()
    for side in range(4):
        forward(250)
        left(90)     
        

# Draws the blocks
def block(dummy_parameter):
    for para in dummy_parameter:
        
        #Draws block A
        if 'Block A' in para[0]:
            if 'X' in para[3]:
                continue
            else:
                penup()
                width(1)

                #Draws the position of the picture
                 #Draws if in Top left
                if 'Top left' in para[1]:
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(0,500)
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(-250,250)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(-250,500)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(0,250)
                #Draws if in Top right
                if 'Top right' in para[1]:
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(0,250)
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(250,500)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(0,500)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(250,250)
                #Draws if in Bottom left
                if 'Bottom left' in para[1]:
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(-250,0)
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(0,250)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(-250,250)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(0,0)
                #Draws if in Bottom right
                if 'Bottom right' in para[1]:
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(0,0)
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(250,250)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(0,250)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(250,0)
                    
                #Draws the green border
                color('green')
                begin_fill()
                forward(75)
                left(90)
                forward(225)
                right(90)
                forward(175)
                left(90)
                forward(25)
                left(90)
                forward(250)
                left(90)
                forward(250)
                end_fill()
                left(90)
                penup()
                forward(75)

                #Draws the white background
                color('white')
                pendown()
                begin_fill()
                for side in range(2):
                    forward(175)
                    left(90)
                    forward(225)
                    left(90)
                end_fill()
                penup()
                
                 #Draws if in Top left
                if 'Top left' in para[1]:
                    if 'Up' in para[2]:
                        goto(x,y+95)
                    if 'Down' in para[2]:
                        goto(x-250,y+155)
                    if 'Left' in para[2]:
                        goto(x-155,y)
                    if 'Right' in para[2]:
                        goto(x-95,y+250)
                 #Draws if in Top right
                if 'Top right' in para[1]:
                    if 'Up' in para[2]:
                        goto(x+250,y+95)
                    if 'Down' in para[2]:
                        goto(x,y+155)
                    if 'Left' in para[2]:
                        goto(x+95,y)
                    if 'Right' in para[2]:
                        goto(x+155,y+250)
                 #Draws if in Bottom left
                if 'Bottom left' in para[1]:
                    if 'Up' in para[2]:
                        goto(x,y-155)
                    if 'Down' in para[2]:
                        goto(x-250,y-95)
                    if 'Left' in para[2]:
                        goto(x-155,y-250)
                    if 'Right' in para[2]:
                        goto(x-95,y)
                 #Draws if in Bottom right
                if 'Bottom right' in para[1]:
                    if 'Up' in para[2]:
                        goto(x+250,y-155)
                    if 'Down' in para[2]:
                        goto(x,y-95)
                    if 'Left' in para[2]:
                        goto(x+95,y-250)
                    if 'Right' in para[2]:
                        goto(x+155,y)

                #Draws the piece of the picture
                right(180)
                color('green')
                begin_fill()
                forward(90)
                circle(20,50) 
                forward(80)
                circle(15,180)
                forward(70)
                right(50)
                forward(45)
                right(125)
                forward(76)
                left(125)
                forward(88)
                left(90)
                forward(96)
                end_fill()
                penup()
                right(90)

                #Draws the position of the black border outline
                     #Draws if in Top left
                if 'Top left' in para[1]:
                    setheading(0)
                    goto(-250,250)
                #Draws if in Top right
                if 'Top right' in para[1]:
                    setheading(0)
                    goto(0,250)
                #Draws if in Bottom left
                if 'Bottom left' in para[1]:
                    setheading(0)
                    goto(-250,0)
                #Draws if in Bottom right
                if 'Bottom right' in para[1]:
                    setheading(0)
                    goto(0,0)

                #Draws the black border outline
                draw(outline)

        #Draws block B
        if 'Block B' in para[0]:
            if 'X' in para[3]:
                continue
            else:
                penup()
                width(1)
                
                #Draws the position of the picture
                #Draws if in Top left
                if 'Top left' in para[1]:
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(0,500)
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(-250,250)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(-250,500)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(0,250)
                #Draws if in Top right
                if 'Top right' in para[1]:
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(0,250)
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(250,500)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(0,500)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(250,250)
                #Draws if in Bottom left
                if 'Bottom left' in para[1]:
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(-250,0)
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(0,250)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(-250,250)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(0,0)
                #Draws if in Bottom right
                if 'Bottom right' in para[1]:
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(0,0)
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(250,250)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(0,250)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(250,0)

                #draws the green border
                forward(175)
                color('green')
                pendown()
                begin_fill()
                forward(75)
                left(90)
                forward(250)
                left(90)
                forward(250)
                left(90)
                forward(25)
                left(90)
                forward(175)
                right(90)
                forward(225)
                end_fill()

                #draws the white background
                right(90)
                color('white')
                begin_fill()
                for side in range(2):
                    forward(175)
                    right(90)
                    forward(225)
                    right(90)
                end_fill()
                penup()
                
                #Draws if in Top left
                if 'Top left' in para[1]:
                    if 'Up' in para[2]:
                        goto(x-75,y)
                    if 'Down' in para[2]:
                        goto(x-175,y+250)
                    if 'Left' in para[2]:
                        goto(x-250,y+75)
                    if 'Right' in para[2]:
                        goto(x,y+175)
                 #Draws if in Top right
                if 'Top right' in para[1]:
                    if 'Up' in para[2]:
                        goto(x+175,y)
                    if 'Down' in para[2]:
                        goto(x+75,y+250)
                    if 'Left' in para[2]:
                        goto(x,y+75)
                    if 'Right' in para[2]:
                        goto(x+250,y+175)
                 #Draws if in Bottom left
                if 'Bottom left' in para[1]:
                    if 'Up' in para[2]:
                        goto(x-75,y-250)
                    if 'Down' in para[2]:
                        goto(x-175,y)
                    if 'Left' in para[2]:
                        goto(x-250,y-175)
                    if 'Right' in para[2]:
                        goto(x,y-75)
                #Draws if in Bottom right
                if 'Bottom right' in para[1]:
                    if 'Up' in para[2]:
                        goto(x+175,y-250)
                    if 'Down' in para[2]:
                        goto(x+75,y)
                    if 'Left' in para[2]:
                        goto(x,y-175)
                    if 'Right' in para[2]:
                        goto(x+250,y-75)


                #draws the piece of the picture
                right(90)
                pendown()
                color('green')
                begin_fill()
                forward(25)
                left(90)
                forward(60)
                right(50)
                forward(65)
                circle(20,40)
                right(2)
                forward(63)
                left(102)
                forward(96)
                left(90)
                forward(30)
                left(60)
                forward(40)
                right(102) 
                forward(53)
                left(43)
                forward(90)
                end_fill()

                penup()
                left(135)
                forward(190)
                dot(60)
                
                penup()
                

                #Draws the position of the black outline
                     #Draws if in Top left
                if 'Top left' in para[1]:
                    setheading(0)
                    goto(-250,250)
                #Draws if in Top right
                if 'Top right' in para[1]:
                    setheading(0)
                    goto(0,250)
                #Draws if in Bottom left
                if 'Bottom left' in para[1]:
                    setheading(0)
                    goto(-250,0)
                #Draws if in Bottom right
                if 'Bottom right' in para[1]:
                    setheading(0)
                    goto(0,0)

                #Draws the black outline
                draw(outline)

        #Draws block C
        if 'Block C' in para[0]:
            if 'X' in para[3]:
                continue
            else:
                penup()
                width(1)
                
                #Draws the position of the picture
                #Draws if in Top left
                if 'Top left' in para[1]:
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(0,500)
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(-250,250)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(-250,500)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(0,250)
                #Draws if in Top right
                if 'Top right' in para[1]:
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(0,250)
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(250,500)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(0,500)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(250,250)
                #Draws if in Bottom left
                if 'Bottom left' in para[1]:
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(-250,0)
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(0,250)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(-250,250)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(0,0)
                #Draws if in Bottom right
                if 'Bottom right' in para[1]:
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(0,0)
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(250,250)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(0,250)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(250,0)

                
            #Draws the white background
                color('white')
                begin_fill()
                for side in range(4):
                    forward(250)
                    left(90)
                end_fill()
                
                #Draws the green border
                color('green')
                pendown()
                begin_fill()
                forward(250)
                left(90)
                forward(10)
                left(90)
                forward(200)
                right(125)
                forward(30)
                left(35)
                forward(60)
                left(90)
                forward(40)
                right(90)
                circle(-40,90)
                left(90)
                forward(115)
                left(90)
                forward(70)
                left(90)
                forward(250)
                end_fill()
                penup()

             #Draws if in Top left
                if 'Top left' in para[1]:
                    if 'Up' in para[2]:
                        goto(x-86,y+250)
                    if 'Down' in para[2]:
                        goto(x-164,y)
                    if 'Left' in para[2]:
                        goto(x,y+86)
                    if 'Right' in para[2]:
                        goto(x-250,y+164)
                 #Draws if in Top right
                if 'Top right' in para[1]:
                    if 'Up' in para[2]:
                        goto(x+164,y+250)
                    if 'Down' in para[2]:
                        goto(x+86,y)
                    if 'Left' in para[2]:
                        goto(x+250,y+86)
                    if 'Right' in para[2]:
                        goto(x,y+164)
                 #Draws if in Bottom left
                if 'Bottom left' in para[1]:
                    if 'Up' in para[2]:
                        goto(x-86,y)
                    if 'Down' in para[2]:
                        goto(x-164,y-250)
                    if 'Left' in para[2]:
                        goto(x,y-164)
                    if 'Right' in para[2]:
                        goto(x-250,y-86)
                 #Draws if in Bottom right
                if 'Bottom right' in para[1]:
                    if 'Up' in para[2]:
                        goto(x+164,y)
                    if 'Down' in para[2]:
                        goto(x+86,y-250)
                    if 'Left' in para[2]:
                        goto(x+250,y-164)
                    if 'Right' in para[2]:
                        goto(x,y-86)

                #Draws the piece of the picture
                pendown()
                right(35)
                color('green')
                begin_fill()
                forward(20)
                circle(15,40)
                right(10)
                forward(95)
                right(85)
                forward(74)
                circle(30,90)
                left(90)   
                forward(100)
                circle(40,90)
                right(20)
                forward(55)
                right(100)
                forward(62)
                left(120)
                forward(91)
                left(90)
                forward(85)
                end_fill()
                
                penup()
                right(180)
                #Draws the position of the black outline
                     #Draws if in Top left
                if 'Top left' in para[1]:
                    setheading(0)
                    goto(-250,250)
                #Draws if in Top right
                if 'Top right' in para[1]:
                    setheading(0)
                    goto(0,250)
                #Draws if in Bottom left
                if 'Bottom left' in para[1]:
                    setheading(0)
                    goto(-250,0)
                #Draws if in Bottom right
                if 'Bottom right' in para[1]:
                    setheading(0)
                    goto(0,0)
                   
                #Draws the black border outline
                draw(outline)
            
        #Draws block D
        if 'Block D' in para[0]:
            if 'X' in para[3]:
                continue
            else:
                penup()
                width(1)
                
                #Draws the position of the picture
                #Draws if in Top left
                if 'Top left' in para[1]:
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(0,500)
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(-250,250)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(-250,500)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(0,250)
                #Draws if in Top right
                if 'Top right' in para[1]:
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(0,250)
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(250,500)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(0,500)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(250,250)
                #Draws if in Bottom left
                if 'Bottom left' in para[1]:
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(-250,0)
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(0,250)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(-250,250)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(0,0)
                #Draws if in Bottom right
                if 'Bottom right' in para[1]:
                    if 'Up' in para[2]:
                        setheading(0)
                        goto(0,0)
                    if 'Down' in para[2]:
                        setheading(180)
                        goto(250,250)
                    if 'Left' in para[2]:
                        setheading(270)
                        goto(0,250)
                    if 'Right' in para[2]:
                        setheading(90)
                        goto(250,0)

                    
                #Draws the white background
                color('white')
                pendown()
                begin_fill()
                for side in range(4):
                    forward(250)
                    left(90)
                end_fill()

                #Draws the green border
                color('green')
                begin_fill()
                forward(250)
                left(90)
                forward(250)
                left(90)
                forward(75)
                left(90)
                forward(220)
                right(35)
                forward(24)
                right(55)
                forward(60)
                right(125)
                forward(30)
                left(125)
                forward(50)
                left(55)
                forward(30)
                right(55)
                forward(50)
                left(90)
                forward(8)
                end_fill()
                
                penup()

                #Draws if in Top left
                if 'Top left' in para[1]:
                    if 'Up' in para[2]:
                        goto(x-250,y+160)
                    if 'Down' in para[2]:
                        goto(x,y+90)
                    if 'Left' in para[2]:
                        goto(x-90,y+250)
                    if 'Right' in para[2]:
                        goto(x-160,y)
                 #Draws if in Top right
                if 'Top right' in para[1]:
                    if 'Up' in para[2]:
                        goto(x,y+160)
                    if 'Down' in para[2]:
                        goto(x+250,y+90)
                    if 'Left' in para[2]:
                        goto(x+160,y+250)
                    if 'Right' in para[2]:
                        goto(x+90,y)
                 #Draws if in Bottom left
                if 'Bottom left' in para[1]:
                    if 'Up' in para[2]:
                        goto(x-250,y-89)
                    if 'Down' in para[2]:
                        goto(x,y-160)
                    if 'Left' in para[2]:
                        goto(x-90,y)
                    if 'Right' in para[2]:
                        goto(x-160,y-250)
                 #Draws if in Bottom right
                if 'Bottom right' in para[1]:
                    if 'Up' in para[2]:
                        goto(x,y-89)
                    if 'Down' in para[2]:
                        goto(x+250,y-160)
                    if 'Left' in para[2]:
                        goto(x+160,y)
                    if 'Right' in para[2]:
                        goto(x+90,y-250)
                        
                #Draws the piece of the picture
                pendown()
                color('green')
                begin_fill()
                left(35)
                forward(120)
                circle(20,40)
                left(15)
                forward(55)
                left(125)
                forward(210)
                right(65)
                forward(28)
                left(120)
                forward(30)
                left(90)
                forward(91)
                end_fill()
                penup()
                #Draws the position of the black outline
                     #Draws if in Top left
                if 'Top left' in para[1]:
                    setheading(0)
                    goto(-250,250)
                #Draws if in Top right
                if 'Top right' in para[1]:
                    setheading(0)
                    goto(0,250)
                #Draws if in Bottom left
                if 'Bottom left' in para[1]:
                    setheading(0)
                    goto(-250,0)
                #Draws if in Bottom right
                if 'Bottom right' in para[1]:
                    setheading(0)
                    goto(0,0)
                    
                #Draws the black border outline
                draw(outline)
        
# Draw the stack of blocks as per the provided data set       
def stack_blocks(dummy_parameter):
    block(dummy_parameter)
        
   
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by stacking your blocks correctly
title('Exit Door Sign Jigssaw Puzzle')
# Display the corner and centre coordinates of the places where
# the blocks must be placed
# ***** If you don't want to display the coordinates change the
# ***** arguments below to False
mark_coords(False, False)

### Call the student's function to display the stack of blocks
### ***** Change the argument to this function to test your
### ***** code with different data sets
stack_blocks(arrangement_99)

# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#

