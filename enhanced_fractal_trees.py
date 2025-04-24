import turtle
import random
import colorsys
import math
from typing import List, Tuple

class Leaf:
    def __init__(self, x: float, y: float, color: Tuple[float, float, float]):
        self.x = x
        self.y = y
        self.color = color
        self.angle = random.uniform(0, 360)
        self.speed = random.uniform(1, 3)
        self.swing = random.uniform(0.5, 1.5)
        self.size = random.uniform(2, 4)

class EnhancedFractalTree:
    def __init__(self):
        # Set up the screen
        self.screen = turtle.Screen()
        self.screen.title("Enhanced Fractal Trees")
        self.screen.bgcolor("black")
        self.screen.setup(800, 800)
        
        # Create main turtle for tree
        self.tree_turtle = turtle.Turtle()
        self.tree_turtle.speed(0)
        self.tree_turtle.hideturtle()
        
        # Create turtle for leaves
        self.leaf_turtle = turtle.Turtle()
        self.leaf_turtle.speed(0)
        self.leaf_turtle.hideturtle()
        
        # Initialize parameters
        self.branch_len = 120
        self.angle = 30
        self.min_len = 5
        self.hue = 0.3  # Green hue
        self.wind_time = 0
        self.wind_strength = 0.5
        self.animation_speed = 50
        self.day_time = 0
        self.leaves: List[Leaf] = []
        self.max_leaves = 50
        
        # Set up event listeners
        self.screen.onkey(self.clear_and_draw, "space")
        self.screen.onkey(self.increase_angle, "Up")
        self.screen.onkey(self.decrease_angle, "Down")
        self.screen.onkey(self.increase_length, "Right")
        self.screen.onkey(self.decrease_length, "Left")
        self.screen.onkey(self.shift_color, "c")
        self.screen.onkey(self.increase_wind, "w")
        self.screen.onkey(self.decrease_wind, "s")
        self.screen.onkey(self.toggle_day_night, "d")
        self.screen.listen()
        
        # Start animation
        self.animate()
        
    def create_fractal_tree(self, branch_len, angle, min_len=5, depth=0):
        if branch_len < min_len:
            # Possibly spawn a leaf at branch tips
            if random.random() < 0.1 and len(self.leaves) < self.max_leaves:
                pos = self.tree_turtle.pos()
                color = colorsys.hsv_to_rgb(self.hue, 0.8, 0.8)
                self.leaves.append(Leaf(pos[0], pos[1], color))
            return
            
        wind_effect = math.sin(self.wind_time + depth) * self.wind_strength * (branch_len / self.branch_len)
        color = colorsys.hsv_to_rgb(self.hue, 1.0, 1.0 - depth * 0.1)
        self.tree_turtle.color(color)
        
        self.tree_turtle.forward(branch_len)
        pos = self.tree_turtle.pos()
        heading = self.tree_turtle.heading()
        
        self.tree_turtle.right(angle * (1 + random.uniform(-0.1, 0.1)) + wind_effect)
        self.create_fractal_tree(branch_len * 0.7, angle, min_len, depth + 1)
        
        self.tree_turtle.penup()
        self.tree_turtle.setpos(pos)
        self.tree_turtle.setheading(heading)
        self.tree_turtle.pendown()
        
        self.tree_turtle.left(angle * (1 + random.uniform(-0.1, 0.1)) + wind_effect)
        self.create_fractal_tree(branch_len * 0.7, angle, min_len, depth + 1)
        
        self.tree_turtle.penup()
        self.tree_turtle.setpos(pos)
        self.tree_turtle.setheading(heading)
        self.tree_turtle.pendown()
    
    def update_leaves(self):
        self.leaf_turtle.clear()
        new_leaves = []
        
        for leaf in self.leaves:
            # Update leaf position
            leaf.y -= leaf.speed
            leaf.x += math.sin(self.wind_time + leaf.angle) * leaf.swing
            
            # Draw leaf if still on screen
            if leaf.y > -400:
                self.leaf_turtle.penup()
                self.leaf_turtle.goto(leaf.x, leaf.y)
                self.leaf_turtle.pendown()
                self.leaf_turtle.dot(leaf.size, leaf.color)
                new_leaves.append(leaf)
        
        self.leaves = new_leaves
    
    def update_sky(self):
        # Calculate sky color based on day_time
        sky_hue = 0.6  # Base blue hue
        sky_sat = 0.7
        sky_val = 0.3 + 0.4 * math.sin(self.day_time)  # Oscillate between darker and lighter
        sky_color = colorsys.hsv_to_rgb(sky_hue, sky_sat, sky_val)
        self.screen.bgcolor(sky_color)
    
    def draw_tree(self):
        self.tree_turtle.clear()
        self.tree_turtle.penup()
        self.tree_turtle.setpos(0, -200)
        self.tree_turtle.setheading(90)
        self.tree_turtle.pendown()
        self.create_fractal_tree(self.branch_len, self.angle, self.min_len)
    
    def animate(self):
        self.wind_time += 0.1
        self.day_time += 0.01
        self.update_sky()
        self.draw_tree()
        self.update_leaves()
        self.screen.ontimer(self.animate, self.animation_speed)
    
    def clear_and_draw(self):
        self.angle = random.randint(20, 40)
        self.branch_len = random.randint(80, 150)
        self.hue = random.random()
        self.leaves.clear()
        
    def increase_angle(self):
        self.angle = min(45, self.angle + 5)
    
    def decrease_angle(self):
        self.angle = max(15, self.angle - 5)
    
    def increase_length(self):
        self.branch_len = min(200, self.branch_len + 10)
    
    def decrease_length(self):
        self.branch_len = max(60, self.branch_len - 10)
    
    def shift_color(self):
        self.hue = (self.hue + 0.1) % 1.0
        
    def increase_wind(self):
        self.wind_strength = min(2.0, self.wind_strength + 0.2)
        
    def decrease_wind(self):
        self.wind_strength = max(0, self.wind_strength - 0.2)
        
    def toggle_day_night(self):
        self.day_time += math.pi  # Instantly switch between day and night

def main():
    tree = EnhancedFractalTree()
    
    print("Enhanced Fractal Tree Controls:")
    print("Space: Generate new random tree")
    print("Up/Down: Increase/decrease branching angle")
    print("Right/Left: Increase/decrease branch length")
    print("C: Change color scheme")
    print("W/S: Increase/decrease wind strength")
    print("D: Toggle day/night cycle")
    
    turtle.mainloop()

if __name__ == "__main__":
    main()