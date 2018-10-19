from colorsys import rgb_to_hls, hls_to_rgb


def clamp(v):
    return max(min(v, 255), 0)


def to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def to_hex(rgb):
    return '#%02x%02x%02x' % rgb


COLORS = [
    # content
    ["base03", "#011827"],
    ["base02", "#023658"],
    ["base01", "#c6c6c6"],
    ["base00", "#eeeeee"],

    # base pallet
    ["yellow",    "#E2D511"],
    ["orange",    "#FF5C40"],
    ["brown",     "#B26800"],
    ["red",       "#CC1514"],
    ["magenta",   "#E318FF"],
    ["violet",    "#6C71C4"],
    ["blue",      "#3D7599"],
    ["cyan",      "#00FFDA"],
    ["green",     "#A6E22E"],
    ["dark-gray", "#444444"],
    ["lite-gray", "#eeeeee"],
]


def adjust_rgb(rgb, factor):
    r, g, b = rgb
    return (
        clamp(r * factor),
        clamp(g * factor),
        clamp(b * factor),
    )


for (key, n_hex) in COLORS:
    n_rgb = to_rgb(n_hex)
    d_rgb = to_hex(adjust_rgb(n_rgb, 0.7))
    l_rgb = to_hex(adjust_rgb(n_rgb, 1.2))

    print("%s\t\t%s\t%s\t%s" % (key, d_rgb, n_hex, l_rgb))
