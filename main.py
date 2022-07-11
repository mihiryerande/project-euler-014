# Problem 14:
#     Longest Collatz Sequence
#
# Description:
#     The following iterative sequence is defined for the set of positive integers:
#         n → n/2 (n is even)
#         n → 3n + 1 (n is odd)
#
#     Using the rule above and starting with 13, we generate the following sequence:
#         13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
#     It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#
#     Although it has not been proved yet (Collatz Problem),
#       it is thought that all starting numbers finish at 1.
#     Which starting number, under one million, produces the longest chain?
#
#     NOTE: Once the chain starts the terms are allowed to go above one million.

from typing import List, Tuple

COLLATZ = dict()


def collatz_count(x: int) -> int:
    """
    Returns the number of elements in the Collatz chain starting with `x`
      and (presumably) ending with 1.

    Args:
        x (int): Natural number

    Returns:
        (int): Length of Collatz chain for `x`

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(x) == int and x > 0
    global COLLATZ
    if x not in COLLATZ:
        # Not already seen, so must calc and persist
        chain_count = 1 + (0 if x == 1 else collatz_count(x//2 if x % 2 == 0 else 3*x+1))
        COLLATZ[x] = chain_count
    return COLLATZ[x]


def main(n: int) -> Tuple[int, List[int]]:
    """
    Returns the number (< `n`) which produces the longest Collatz chain,
      as well as the chain itself.

    Args:
        n (int): Natural number greater than 1

    Returns:
        (Tuple[int, List[int]]):
            Tuple of ...
              * Number less than `n` producing the largest Collatz chain
              * The chain itself

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 1

    longest_count = 0
    best_num = 0
    for i in range(1, n):
        this_count = collatz_count(i)
        if this_count > longest_count:
            best_num = i
            longest_count = this_count

    # Recompute the actual chain
    x = best_num
    longest_chain = [x]
    while x > 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3*x+1
        longest_chain.append(x)

    return best_num, longest_chain


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    start, chain = main(num)
    print('Longest chain starting below {}:'.format(num))
    print('  Starts at {}'.format(start))
    print('  Length is {}'.format(len(chain)))
    print('  Chain:')
    print('    {}'.format('\n    → '.join(map(str, chain))))
