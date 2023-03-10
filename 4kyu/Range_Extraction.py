# A format for expressing an ordered list of integers is to use a comma separated list of either
#
# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by
# a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered
# a range unless it spans at least 3 numbers. For example "12,13,15-17"
#
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly
# formatted string in the range format.
#
# Example:
#
# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

def solution(lst):
    ranges = []
    start = lst[0]
    prev = lst[0]
    for i in range(1, len(lst)):
        if lst[i] == prev + 1:
            prev = lst[i]
        else:
            if prev == start:
                ranges.append(str(prev))
            elif prev == start + 1:
                ranges.extend([str(start), str(prev)])
            else:
                ranges.append(str(start) + "-" + str(prev))
            start = lst[i]
            prev = lst[i]
    # handle the last range
    if prev == start:
        ranges.append(str(prev))
    elif prev == start + 1:
        ranges.extend([str(start), str(prev)])
    else:
        ranges.append(str(start) + "-" + str(prev))
    return ",".join(ranges)






print(solution(
    [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))  # , '-6,-3-1,3-5,7-11,14,15,17-20'
print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))  # , '-3--1,2,10,15,16,18-20'


# better ideas

# def solution(args):
#     out = []
#     beg = end = args[0]
#
#     for n in args[1:] + [""]:
#         if n != end + 1:
#             if end == beg:
#                 out.append(str(beg))
#             elif end == beg + 1:
#                 out.extend([str(beg), str(end)])
#             else:
#                 out.append(str(beg) + "-" + str(end))
#             beg = n
#         end = n
#
#     return ",".join(out)