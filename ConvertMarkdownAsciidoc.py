import re
import sys

expressions = [
        (re.compile(r"""\[([^\]]+)\]\(([^)]*)\)"""), r"""\2[\1]"""),
        (re.compile(r"""####"""), """===="""),
        (re.compile(r"""###"""), """==="""),
        (re.compile(r"""##"""), """=="""),
        (re.compile(r"""#"""), """="""),

        # first transform those with trailing space or punctuation
        (re.compile(r"""\*\*([^* ][^*]*)\*\*(?:\s|[[:punct:]])"""), r"""__\1__"""),
        (re.compile(r"""\*([^* ][^*]*)\*(?:\s|[[:punct:]])"""), r"""_\1_"""),

        # now deal with those remaining, i.e which have trailing text
        (re.compile(r"""\*\*([^* ][^*]*)\*\*"""), r"""__\1__ """),
        (re.compile(r"""\*([^* ][^*]*)\*"""), r"""_\1_ """),
]

for l in sys.stdin.readlines():
    for i,o in expressions:
        l = i.sub(o, l)
    print l,
