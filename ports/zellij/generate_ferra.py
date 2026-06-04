"""Generate ferra.kdl theme file from semantic color definitions."""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Color:
    """RGB color with hex support."""

    r: int
    g: int
    b: int

    @classmethod
    def from_hex(cls, hex_str: str) -> "Color":
        hex_str = hex_str.lstrip("#")
        return cls(
            r=int(hex_str[0:2], 16),
            g=int(hex_str[2:4], 16),
            b=int(hex_str[4:6], 16),
        )

    def to_kdl(self) -> str:
        return f"{self.r} {self.g} {self.b}"


# ── Ferra palette ──────────────────────────────────────────────
night = Color.from_hex("#2b292d")
ash = Color.from_hex("#383539")
umber = Color.from_hex("#4d424b")
bark = Color.from_hex("#6F5D63")
mist = Color.from_hex("#D1D1E0")
sage = Color.from_hex("#B1B695")
blush = Color.from_hex("#fecdb2")
coral = Color.from_hex("#ffa07a")
rose = Color.from_hex("#F6B6C9")
ember = Color.from_hex("#e06b75")
honey = Color.from_hex("#F5D76E")
black = Color(0, 0, 0)


@dataclass
class ColorPattern:
    """Base, background, and four emphasis slots."""

    base: Color
    background: Color
    emphasis_0: Color
    emphasis_1: Color
    emphasis_2: Color
    emphasis_3: Color

    def to_kdl(self, name: str) -> str:
        lines = [f"        {name} {{"]
        for slot in (
            "base",
            "background",
            "emphasis_0",
            "emphasis_1",
            "emphasis_2",
            "emphasis_3",
        ):
            color: Color = getattr(self, slot)
            lines.append(f"            {slot} {color.to_kdl()}")
        lines.append("        }")
        return "\n".join(lines)


@dataclass
class MultiplayerColors:
    """Colors for up to 10 players. Use None for unused slots."""

    player_1: Color
    player_2: Color
    player_3: Color
    player_4: Color
    player_5: Color
    player_6: Color
    player_7: Color
    player_8: Color
    player_9: Color
    player_10: Color

    def to_kdl(self) -> str:
        lines = ["        multiplayer_user_colors {"]
        for i in range(1, 11):
            attr = f"player_{i}"
            color: Color = getattr(self, attr)
            lines.append(f"            {attr} {color.to_kdl()}")
        lines.append("        }")
        return "\n".join(lines)


@dataclass
class Theme:
    """A Zellij theme built from semantic color patterns."""

    text_unselected: ColorPattern
    text_selected: ColorPattern
    ribbon_selected: ColorPattern
    ribbon_unselected: ColorPattern
    table_title: ColorPattern
    table_cell_selected: ColorPattern
    table_cell_unselected: ColorPattern
    list_selected: ColorPattern
    list_unselected: ColorPattern
    frame_unselected: ColorPattern
    frame_selected: ColorPattern
    frame_highlight: ColorPattern
    exit_code_success: ColorPattern
    exit_code_error: ColorPattern
    multiplayer_user_colors: MultiplayerColors
    name: str = "ferra"

    def to_kdl(self) -> str:
        blocks: list[str] = []
        blocks.append("themes {")
        blocks.append(f"    {self.name} {{")

        pattern_names = [
            "text_unselected",
            "text_selected",
            "ribbon_selected",
            "ribbon_unselected",
            "table_title",
            "table_cell_selected",
            "table_cell_unselected",
            "list_selected",
            "list_unselected",
            "frame_unselected",
            "frame_selected",
            "frame_highlight",
            "exit_code_success",
            "exit_code_error",
        ]
        for pn in pattern_names:
            cp: ColorPattern = getattr(self, pn)
            blocks.append(cp.to_kdl(pn))

        blocks.append(self.multiplayer_user_colors.to_kdl())

        blocks.append("    }")
        blocks.append("}")
        return "\n".join(blocks) + "\n"


# ── Build the Ferra theme ─────────────────────────────────────
ferra_theme = Theme(
    name="ferra",
    text_unselected=ColorPattern(
        base=mist,
        background=night,
        emphasis_0=blush,
        emphasis_1=sage,
        emphasis_2=coral,
        emphasis_3=blush,
    ),
    text_selected=ColorPattern(
        base=mist,
        background=ash,
        emphasis_0=blush,
        emphasis_1=sage,
        emphasis_2=coral,
        emphasis_3=rose,
    ),
    ribbon_selected=ColorPattern(
        base=coral,
        background=night,
        emphasis_0=ember,
        emphasis_1=blush,
        emphasis_2=rose,
        emphasis_3=bark,
    ),
    ribbon_unselected=ColorPattern(
        base=black,
        background=bark,
        emphasis_0=ember,
        emphasis_1=mist,
        emphasis_2=bark,
        emphasis_3=rose,
    ),
    table_title=ColorPattern(
        base=coral,
        background=black,
        emphasis_0=blush,
        emphasis_1=sage,
        emphasis_2=coral,
        emphasis_3=rose,
    ),
    table_cell_selected=ColorPattern(
        base=mist,
        background=ash,
        emphasis_0=blush,
        emphasis_1=sage,
        emphasis_2=coral,
        emphasis_3=rose,
    ),
    table_cell_unselected=ColorPattern(
        base=mist,
        background=night,
        emphasis_0=blush,
        emphasis_1=sage,
        emphasis_2=coral,
        emphasis_3=rose,
    ),
    list_selected=ColorPattern(
        base=mist,
        background=ash,
        emphasis_0=blush,
        emphasis_1=sage,
        emphasis_2=coral,
        emphasis_3=rose,
    ),
    list_unselected=ColorPattern(
        base=mist,
        background=night,
        emphasis_0=blush,
        emphasis_1=sage,
        emphasis_2=coral,
        emphasis_3=rose,
    ),
    frame_unselected=ColorPattern(
        base=ash,
        background=ash,
        emphasis_0=blush,
        emphasis_1=sage,
        emphasis_2=rose,
        emphasis_3=black,
    ),
    frame_selected=ColorPattern(
        base=bark,
        background=black,
        emphasis_0=blush,
        emphasis_1=sage,
        emphasis_2=rose,
        emphasis_3=black,
    ),
    frame_highlight=ColorPattern(
        base=umber,
        background=black,
        emphasis_0=rose,
        emphasis_1=blush,
        emphasis_2=blush,
        emphasis_3=blush,
    ),
    exit_code_success=ColorPattern(
        base=coral,
        background=black,
        emphasis_0=sage,
        emphasis_1=night,
        emphasis_2=rose,
        emphasis_3=bark,
    ),
    exit_code_error=ColorPattern(
        base=ember,
        background=black,
        emphasis_0=honey,
        emphasis_1=black,
        emphasis_2=black,
        emphasis_3=black,
    ),
    multiplayer_user_colors=MultiplayerColors(
        player_1=rose,
        player_2=bark,
        player_3=black,
        player_4=honey,
        player_5=sage,
        player_6=black,
        player_7=ember,
        player_8=black,
        player_9=black,
        player_10=black,
    ),
)


if __name__ == "__main__":
    output_path = "ferra.kdl"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ferra_theme.to_kdl())
    print(f"Written {output_path}")
