class Physics:
    g = 1

    @staticmethod
    def apply_gravity(velocityY):
        return velocityY + Physics.g

    @staticmethod
    def handle_collision(X, Y, velocityX, velocityY):
        if X < 0 or X > 768:
            velocityX *= -1
        if Y < 0 and velocityY < 0:
            velocityY *= -1
            Y = 0
        if Y > 568 and velocityY > 0:
            velocityY *= -1
            Y = 568
        return X, Y, velocityX, velocityY
