import sys
import pygame
from _thread import start_new_thread
from .exceptions import DrawError


class PygameQuick:
    def __init__(self, width=800, height=600, title="PygameQuick Window", bgcolor=(41, 41, 41)):
        self._win_width = width
        self._win_height = height
        self._win_title = title
        self._bg_color = bgcolor
        self._pygame = pygame
        self._pygame.init()
        self._screen = self._pygame.display.set_mode((self._win_width, self._win_height))
        self._c_polygons = []
        self._c_circles = []
        self._c_rects = []
        self._le_raise = []
        self.run = True
        self.keys = []
        self._run_frame()
        
    def _run_frame(self):
        for event in self._pygame.event.get():
            if event.type == self._pygame.QUIT:
                self.run = False
                sys.exit()

        self._screen.fill(self._bg_color)

        try:
            for polygon, color, width in self._c_polygons:
                self._pygame.draw.polygon(self._screen, color, polygon, width)
            self._c_polygons = []
        except Exception as e:
            le_re = DrawError(f"Failed to draw polygons: {e}")
            self._le_raise.append(le_re)
        try:

            for circle, color, radius in self._c_circles:
                self._pygame.draw.circle(self._screen, color, circle, radius)
            self._c_circles = []
        except Exception as e:
            le_re = DrawError(f"Failed to draw circles: {e}")
            self._le_raise.append(le_re)
        try:

            for rect, color in self._c_rects:
                self._pygame.draw.rect(self._screen, color, rect)
            self._c_rects = []
        except Exception as e:
            le_re = DrawError(f"Failed to draw rectangles: {e}")
            self._le_raise.append(le_re)

        self._pygame.display.flip()

    def frame(self):
        self._run_frame()
        self.keys = self._pygame.key.get_pressed()

    def draw_polygon(self, polygon: list[tuple[int or float, int or float]], color: tuple[int, int, int], width: int):
        """
        Draw a polygon on the canvas.

        Args:
            polygon (list[tuple[int or float, int or float]]): list of (x, y) coordinates defining the vertices of the polygon.
            color (tuple[int, int, int]): The RGB color values for the polygon.
            width (int): The width of the polygon's outline.

        Returns:
            None
        """
        polygon_data = (polygon, color, width)
        self._c_polygons.append(polygon_data)

    def draw_circle(self, pos: tuple[int or float, int or float], color: tuple[int, int, int],
                    radius: int):
        """
        Draw a circle on the canvas.

        Args:
            pos (tuple[int or float, int or float, int or float]): The position of the circle as a tuple of (x, y, z) coordinates.
            color (tuple[int, int, int]): The RGB color values for the circle.
            radius (int): The radius of the circle.

        Returns:
            None
        """
        circle_data = (pos, color, radius)
        self._c_circles.append(circle_data)

    def draw_rect(self, rect: tuple[tuple[int, int, int, int], tuple[int, int, int]], color: tuple[int, int, int]):
        """
        Draw a rectangle on the canvas.

        Args:
            rect (tuple[tuple[int, int, int, int], tuple[int, int, int]]): The rectangle's position and size as ((x, y, width, height), (color)).
            color (tuple[int, int, int]): The RGB color values for the rectangle.

        Returns:
            None
        """
        rect_data = (rect, color)
        self._c_rects.append(rect_data)
