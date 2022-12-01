""" Credit: https://www.reddit.com/r/adventofcode/comments/z9ezjb/comment/iyi5lfb/ """

data = open("advent-of-code\day-1\input_dummy.txt").read()
totals = [sum([int(c) for c in elf.split("\n")]) for elf in data.strip().split("\n\n")]
print(f"Part 1: {max(totals)}")
print(f"Part 2: {sum(sorted(totals, reverse=True)[:3])}")