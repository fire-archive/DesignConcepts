import re
import sys
import string

expressions = [
        (re.compile(r"""\[([^\]]+)\]\(([^)]*)\)"""), r"""\2[\1]"""),
        (re.compile(r"""####"""), """===="""),
        (re.compile(r"""###"""), """==="""),
        (re.compile(r"""##"""), """=="""),
        (re.compile(r"""#"""), """="""),

        # first transform **foo** -> __foo__ globally
        (re.compile(r"""\*\*([^* ][^*]*)\*\*"""), r"""__\1__"""),

        # now deal with *foo* -> _foo_, remember to add a space when you hit *foo*bar
        (re.compile(r"""\*([^* ][^*]*)\*(\s|[%s])""" % string.punctuation), r"""_\1_\2"""),
        (re.compile(r"""\*([^* ][^*]*)\*"""), r"""_\1_ """),

        # now __foo__ -> *foo*, remember to add a space when you hit __foo__bar
        (re.compile(r"""__([^_ ][^_]*)__(\s|[%s])""" % string.punctuation), r"""*\1*\2"""),
        (re.compile(r"""__([^_ ][^_]*)__"""), r"""*\1* """),
]

for l in sys.stdin.readlines():
    for i,o in expressions:
        l = i.sub(o, l)
    print l,
