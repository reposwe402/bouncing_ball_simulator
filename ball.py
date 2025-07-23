from physics import Physics

class Ball:
    def __init__(self, renderer):
        self.velocityX = 4
        self.velocityY = 4
        self.X = random.randint(0, 768)
        self.Y = random.randint(0, 350)
        self.renderer = renderer

    def render_ball(self):
        self.renderer.render_ball(self.X, self.Y)

    def move_ball(self):
        # Apply gravity
        self.velocityY = Physics.apply_gravity(self.velocityY)
        # Update position based on velocity
        self.X += self.velocityX
        self.Y += self.velocityY
        # Handle collision
        self.X, self.Y, self.velocityX, self.velocityY = Physics.handle_collision(
            self.X, self.Y, self.velocityX, self.velocityY
        )
