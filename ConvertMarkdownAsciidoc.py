import re
import sys

expressions = [
        (re.compile(r"""\[([^\]]+)\]\(([^)]*)\)"""), r"""\2[\1]"""),
        (re.compile(r"""####"""), """===="""),
        (re.compile(r"""###"""), """==="""),
        (re.compile(r"""##"""), """=="""),
        (re.compile(r"""#"""), """="""),

        (re.compile(r"""\*\*([^* ][^*]*)\*\*(?:\s|[[:punct:]])"""), r"""__\1__"""),
		(re.compile(r"""\*\*([^* ][^*]*)\*\*"""), r"""__\1__ """),

        (re.compile(r"""\*([^* ][^*]*)\*(?:\s|[[:punct:]])"""), r"""_\1_"""),
        (re.compile(r"""\*([^* ][^*]*)\*"""), r"""_\1_ """),
        
        (re.compile(r"""__([^* ][^*]*)__(?:\s|[[:punct:]])"""), r"""*\1*"""),
        (re.compile(r"""__([^* ][^*]*)__"""), r"""*\1* """),
]

for l in sys.stdin.readlines():
    for i,o in expressions:
        l = i.sub(o, l)
    print l,
