"""
Professor Chase
---------------
A little chase game built with Py2SB3.

- Use the arrow keys to run the Professor around the stage.
- The scary Ghost constantly turns to face the Professor and creeps
  toward him every frame.
- If the Ghost touches the Professor, the game announces it and stops.

Run this file (e.g. `uv run professor_chase.py`) to compile it to
professor_chase.sb3, ready to open in the Scratch editor or TurboWarp.
"""

from scratch import transpile_to_json, save_sb3
from scratch.dsl import *  # noqa: F401,F403  (IDE autocomplete for all blocks)

# NOTE: the current py2sb3 package exposes `transpile_to_json` + `save_sb3`
# rather than a `create_scratch_file` helper. transpile_to_json reads
# this file's own source (see the bottom), finds every top-level class
# below, and compiles each one into a Scratch sprite -- no need to wrap
# the classes in a string.


class Wizard:
    """Stand-in sprite for the Professor -- player controlled."""

    def when_flag_clicked(self):
        go_to_xy(-150, 0)
        point_in_direction(90)
        show()
        say_for_secs("Run!", 1)
        while True:
            if key_pressed("up"):
                change_y(6)
            if key_pressed("down"):
                change_y(-6)
            if key_pressed("left"):
                change_x(-6)
                point_in_direction(-90)
            if key_pressed("right"):
                change_x(6)
                point_in_direction(90)

            # keep the Professor on-stage
            if x_position() > 230:
                set_x(230)
            if x_position() < -230:
                set_x(-230)
            if y_position() > 170:
                set_y(170)
            if y_position() < -170:
                set_y(-170)

            if touching("Ghost"):
                say_for_secs("The Professor has been caught!", 2)
                stop("all")


class Ghost:
    """The scary chaser -- always turns toward and creeps up on the Professor."""

    def when_flag_clicked(self):
        go_to_xy(150, 0)
        set_effect("ghost", 10)
        show()
        while True:
            point_towards("Wizard")
            move(3)

            if touching("Wizard"):
                say_for_secs("Gotcha, Professor!", 2)
                stop("all")


if __name__ == "__main__":
    with open(__file__) as f:
        source = f.read()
    json_str = transpile_to_json(source)
    save_sb3(json_str, "professor_chase.sb3")
    print("Wrote professor_chase.sb3")
