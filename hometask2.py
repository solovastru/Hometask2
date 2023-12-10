import math

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = self.create_canvas()

    def create_canvas(self):
        return [" " * self.width for _ in range(self.height)]

    def print_canvas(self):
        def create_row_headers(length: int):
            return "".join([str(i % 10) for i in range(length)])

        header = " " + create_row_headers(len(self.canvas[0]))
        print(header)

        for idx, row in enumerate(self.canvas):
            print(idx % 10, row, idx % 10, sep="")
        print(header)




    def draw_polygon(self, *points: tuple[int, int], closed: bool = True, line_char: str = "*"):

        def draw_line_segment(self, start: tuple[int, int], end: tuple[int, int], line_char: str = "*"):


            def replace_at_index(s: str, r: str, idx: int) -> str:
                return s[:idx] + r + s[idx + len(r):]

            x1, y1 = start
            x2, y2 = end

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            sx = 1 if x1 < x2 else -1
            sy = 1 if y1 < y2 else -1
            error = dx - dy

            while x1 != x2 or y1 != y2:
                self[y1] = replace_at_index(self[y1], line_char, x1)

                double_error = error * 2
                if double_error > -dy:
                    error -= dy
                    x1 += sx

                if double_error < dx:
                    error += dx
                    y1 += sy

            self[y2] = replace_at_index(self[y2], line_char, x2)

            start_points = points[:-1]
            end_points = points[1:]

            if closed:
                start_points += (points[-1],)
            for start_point, end_point in zip(start_points, end_points):
                self.draw_line_segment(self, start_point, end_point, line_char)



    def draw_line(self: list[str, ...], start: tuple[int, int], end: tuple[int, int], line_char: str = "*"):
        self.draw_polygon(self, start, end, closed=False, line_char=line_char)


    def draw_rectangle(self: list[str, ...], upper_left: tuple[int, int], lower_right: tuple[int, int],
                       line_char: str = "*"):
        x1, y1 = upper_left
        x2, y2 = lower_right
        self.draw_polygon(self, upper_left, (x2, y1), lower_right, (x1, y2), line_char=line_char)

    def draw_n_gon(self: list[str, ...], center: tuple[int, int], radius: int, number_of_points: int,
                   rotation: int = 0,
                   line_char: str = "*"):
        angles = range(rotation, 360 + rotation, 360 // number_of_points)

        points = []
        for angle in angles:
            angle_in_radians = math.radians(angle)

            x = center[0] + radius * math.cos(angle_in_radians)
            y = center[1] + radius * math.sin(angle_in_radians)

            points.append((round(x), round(y)))

        self.draw_polygon(self, *points, line_char=line_char)



canvas = Canvas(100, 40)


print(canvas.draw_line((10, 4), (92, 19), "+"))
# A polygon with five points, the last point will be connected to the first one
canvas.draw_polygon((7, 12), (24, 29), (42, 15), (37, 32), (15, 35))
# A rectangle from the upper-left corner to the lower-right corner
canvas.draw_rectangle((45, 2), (80, 27), line_char='#')
# An n-gon with a high number of points will appear like a circle
canvas.draw_n_gon((72, 25), 12, 20, 80, "-")
canvas.print_canvas()




class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    #def __str__(self):
        #return f"{self.x}/{self.y}" # used to print a single object

    def __repr__(self): # used to print a collection of objects
        return f"({self.x}/{self.y})" # comma outside in order to see the numbers inside braces in the output


    def distance_from_origin(self) -> float:
         return math.sqrt(self.x**2 + self.y**2)



p1 = Point(1, 1)
p2 = Point(5, 5)
p3 = Point(10, 10)

print(p1.distance_from_origin())
print(p2.distance_from_origin())
print(p3.distance_from_origin())


class Shape(Point):
    def __init__(self, *points):
        self.points = list(points)


    def __repr__(self):
        return f"{self.points}"

    def centroid(self) -> Point:
        average_x = sum(point.x for point in self.points)/len(self.points)
        average_y = sum(point.y for point in self.points)/len(self.points)
        return average_x, average_y


    def distance_centroid_from_origin(self) -> float:
        centroid = self.centroid()
        return math.sqrt(centroid[0]**2 + centroid[1]**2)


    def __lt__(self, other):
        return self.distance_centroid_from_origin() < other.distance_centroid_from_origin()

    def __eq__(self, other):
        return self.distance_centroid_from_origin() == other.distance_centroid_from_origin()


s1 = Shape(p1, p2, p3)
s2 = Shape(p2)
s3 = Shape()

print(s1)
print(s2)
print(s3)

s1 = Shape(Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0))
s2 = Shape(Point(0, 0.5), Point(0.5, 1), Point(1, 0.5), Point(0.5, 0))

print(s1.centroid())
print(s2.centroid())
print(Shape.__eq__(s1, s2))

s2 = Shape(Point(5, 5), Point(5, 6), Point(6, 6), Point(6, 5))
print(Shape.__lt__(s1, s2))

s3 = Shape(Point(10, 10), Point(10, 11), Point(11, 11), Point(11, 10))
shapes = [s3, s1, s2]
print(shapes)
print(sorted(shapes))


## I didn't manage to print the shapes and I also don't know how to do it
## I guess I might have missed some return or print functions but I can't see where