import sys

from ntt.draw.primitives import (
    draw_bright_circle,
    draw_crosshair,
    draw_filled_polygon,
    draw_frame_counter,
    draw_grid,
    draw_line,
    draw_rectangle,
    draw_ripple,
    write_text,
)
from ntt.frames.display import display_frame
from ntt.frames.frame_generation import full_frame
from ntt.frames.io import write


def generate_primitives_showcase(output_path: str = "primitives_showcase.png"):
    frame = full_frame(width=800, height=800, color=(40, 40, 40))

    draw_grid(frame, rows=8, cols=8)
    write_text(
        frame,
        text="NTT Primitives Showcase",
        posXY=(20, 40),
        color=(255, 255, 255),
        thickness=2,
    )

    draw_rectangle(frame, posXY=((50, 100), (200, 250)), color=(0, 255, 0))
    write_text(frame, "draw_rectangle", posXY=(50, 90), color=(0, 255, 0), thickness=1)

    draw_line(frame, start_point=(300, 100), end_point=(450, 250), color=(255, 0, 0))
    write_text(frame, "draw_line", posXY=(300, 90), color=(255, 0, 0), thickness=1)

    draw_crosshair(frame, x=650, y=175, text="crosshair", color=(0, 255, 255), cross_size=20, draw_circle=True)

    draw_bright_circle(frame, center=(150, 400), radius=50, brightness_factor=100)
    write_text(frame, "draw_bright_circle", posXY=(50, 470), color=(255, 255, 255), thickness=1)

    points = [(400, 350), (450, 450), (350, 450)]
    draw_filled_polygon(frame, points, color=(255, 100, 200), alpha=0.7)
    write_text(frame, "draw_filled_polygon", posXY=(320, 470), color=(255, 100, 200), thickness=1)

    draw_frame_counter(frame, current=42, total=100, posXY=(600, 400), color=(200, 200, 200))

    draw_ripple(frame, center=(600, 600), num_rings=10, max_radius=150, color=(100, 255, 100), thickness=2)
    write_text(frame, "draw_ripple", posXY=(550, 770), color=(100, 255, 100), thickness=1)

    write(output_path, frame)
    print(f"Primitives showcase saved to {output_path}")
    return frame


if __name__ == "__main__":
    output_path = sys.argv[1] if len(sys.argv) > 1 else "primitives_showcase.png"
    frame = generate_primitives_showcase(output_path)
    if "--display" in sys.argv:
        display_frame(frame)
