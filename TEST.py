pos = 250
posy = 50
# x="{cx-7+dx}" y="{cy+dy}  14x50
w = """
<svg width="500" height="500" xmlns="http://www.w3.org/2000/svg">
    <style>
        text{
            font-family: sans-serif;
        }
    </style>
    <rect width="14" height="50" x="116" y="170" fill="red"/>
    <rect width="14" height="50" x="100" y="100" fill="red"/>
    <rect width="14" height="50" x="132" y="100" fill="red"/>
    <polygon points="114,150 100,150 116,170 130,170 146,150 132,150 123,160" fill="red"/>
</svg>
"""

###" comment on prettyfy le SVG ????"


with open('test.svg','w') as svgfile:
    svgfile.write(w)

        