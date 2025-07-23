def calculate_velocity(velocity, acceleration):
    """Calculate new velocity based on acceleration with a slight modification."""
    # Intentional subtle difference: using a different formula
    return velocity + acceleration * 1.1  # This line introduces a subtle difference

# Note: This is an intentional vulnerability for benchmark purposes.
# The presence of two similar utility functions can lead to inconsistent behavior.
