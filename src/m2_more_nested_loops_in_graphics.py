"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Chengqian Lyu HERE.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    original_lowerleftcorner_x = rectangle.get_lower_left_corner().x
    original_lowerleftcorner_y = rectangle.get_lower_left_corner().y
    original_upperrightcorner_x = rectangle.get_upper_right_corner().x
    original_upperrightcorner_y = rectangle.get_upper_right_corner().y
    x1 = original_lowerleftcorner_x
    y1 = original_lowerleftcorner_y
    x2 = original_upperrightcorner_x
    y2 = original_upperrightcorner_y
    width = rectangle.get_width()
    height = rectangle.get_height()
    for k in range(n):
        for j in range(k + 1):
            newrectangle = rg.Rectangle(rg.Point(x1,y1),rg.Point(x2,y2))
            newrectangle.attach_to(window)
            x1 = x1 + width
            x2 = x2 + width
            window.render(0.1)
        x1 = original_lowerleftcorner_x
        x2 = original_upperrightcorner_x
        y1 = y1 - height
        y2 = y2 - height
        x1 = x1 - width/2*(k + 1)
        x2 = x2 - width/2*(k + 1)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
