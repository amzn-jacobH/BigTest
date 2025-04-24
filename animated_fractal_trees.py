import turtle
import random
import colorsys
import math

class AnimatedFractalTree:
    def __init__(self):
        # Set up the screen
        self.screen = turtle.Screen()
        self.screen.title("Animated Fractal Trees")
        self.screen.bgcolor("black")
        self.screen.setup(800, 800)
        
        # Create and configure the turtle
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        
        # Initialize parameters
        self.branch_len = 120
        self.angle = 30
        self.min_len = 5
        self.hue = 0.3  # Green hue
        self.wind_time = 0
        self.wind_strength = 0.5
        self.animation_speed = 50  # milliseconds
        
        # Set up event listeners
        self.screen.onkey(self.clear_and_draw, "space")
        self.screen.onkey(self.increase_angle, "Up")
        self.screen.onkey(self.decrease_angle, "Down")
        self.screen.onkey(self.increase_length, "Right")
        self.screen.onkey(self.decrease_length, "Left")
        self.screen.onkey(self.shift_color, "c")
        self.screen.onkey(self.increase_wind, "w")
        self.screen.onkey(self.decrease_wind, "s")
        self.screen.listen()
        
        # Start animation
        self.animate()
        
    def create_fractal_tree(self, branch_len, angle, min_len=5, depth=0):
        """Recursively draws a fractal tree with color gradient and wind effect"""
        if branch_len < min_len:
            return
            
        # Calculate wind effect based on height and time
        wind_effect = math.sin(self.wind_time + depth) * self.wind_strength * (branch_len / self.branch_len)
        
        # Calculate color based on branch depth
        color = colorsys.hsv_to_rgb(self.hue, 1.0, 1.0 - depth * 0.1)
        self.t.color(color)
        
        # Draw current branch
        self.t.forward(branch_len)
        pos = self.t.pos()
        heading = self.t.heading()
        
        # Right branch with wind effect
        self.t.right(angle * (1 + random.uniform(-0.1, 0.1)) + wind_effect)
        self.create_fractal_tree(branch_len * 0.7, angle, min_len, depth + 1)
        
        # Return and draw left branch
        self.t.penup()
        self.t.setpos(pos)
        self.t.setheading(heading)
        self.t.pendown()
        
        self.t.left(angle * (1 + random.uniform(-0.1, 0.1)) + wind_effect)
        self.create_fractal_tree(branch_len * 0.7, angle, min_len, depth + 1)
        
        # Return to start position
        self.t.penup()
        self.t.setpos(pos)
        self.t.setheading(heading)
        self.t.pendown()
    
    def draw_tree(self):
        """Set up and draw a new tree"""
        self.t.clear()
        self.t.penup()
        self.t.setpos(0, -200)
        self.t.setheading(90)
        self.t.pendown()
        self.create_fractal_tree(self.branch_len, self.angle, self.min_len)
    
    def animate(self):
        """Animate the tree by updating wind time and redrawing"""
        self.wind_time += 0.1
        self.draw_tree()
        self.screen.ontimer(self.animate, self.animation_speed)
    
    def clear_and_draw(self):
        """Generate new random parameters and draw"""
        self.angle = random.randint(20, 40)
        self.branch_len = random.randint(80, 150)
        self.hue = random.random()
        
    def increase_angle(self):
        """Increase branching angle"""
        self.angle = min(45, self.angle + 5)
    
    def decrease_angle(self):
        """Decrease branching angle"""
        self.angle = max(15, self.angle - 5)
    
    def increase_length(self):
        """Increase initial branch length"""
        self.branch_len = min(200, self.branch_len + 10)
    
    def decrease_length(self):
        """Decrease initial branch length"""
        self.branch_len = max(60, self.branch_len - 10)
    
    def shift_color(self):
        """Shift the base hue of the tree"""
        self.hue = (self.hue + 0.1) % 1.0
        
    def increase_wind(self):
        """Increase wind strength"""
        self.wind_strength = min(2.0, self.wind_strength + 0.2)
        
    def decrease_wind(self):
        """Decrease wind strength"""
        self.wind_strength = max(0, self.wind_strength - 0.2)

def main():
    tree = AnimatedFractalTree()
    
    # Display instructions
    print("Animated Fractal Tree Controls:")
    print("Space: Generate new random tree")
    print("Up/Down: Increase/decrease branching angle")
    print("Right/Left: Increase/decrease branch length")
    print("C: Change color scheme")
    print("W/S: Increase/decrease wind strength")
    
    # Keep window open
    turtle.mainloop()

if __name__ == "__main__":
    main()