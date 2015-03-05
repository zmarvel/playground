# Hyperbinary #

A description of this problem can be found [here](http://www.reddit.com/r/dailyprogrammer/comments/2xx86n/20150302_challenge_204_intermediate_its_like/). This is an intermediate problem from [/r/dailyprogrammer](http://www.reddit.com/r/dailyprogrammer/).

This solution takes advantage of the transformations you can perform on a binary number to find all its "hyperbinary" forms.

    > 8
    1000 -> 200 -> 120 -> 112

    > 13
    1101 -> 1021 -> 221

    > 18
    10010 --> 2010 --> 2002 --> x
          \-> x    |        \-> 1212 
                   |                 
                   \-> 1210 --> 1202 --> x
                                     \-> 1212 --> x
                                              \-> x

    > 73
    1001001 -> 1000201 -> 1000121
           \-> 201001 -> 200201 -> 200121 -> 120121 -> 112121`
                     \-> 121001 -> 120201 -> 120121 -> 112121 # could have stopped at the point of the previous substitution to eliminate duplicates

As you can see, this approach generates some duplicates, but here's the idea: `10` can be rewritten as `02`, and `20` can be rewritten as `12`. My implementation of the algorithm will attempt to start making substitutions from the least significant bit.

The first rule, `10 = 02`, works because `10` is `1*2^i + 0*2^(i-1)`, which is the same as `2*2^(i-1) = 2^i`.

The second rule, `20 = 12`, works because `20` is `2*2^i + 0*2^(i-1) = 2^(i+1)`, which is the same as `1*2^i + 2*2(i-1) = 2^i + 2^i = 2*2^i = 2^(i+1)`.


## Improvements ##

This approach is not very efficient. It takes several seconds to find 12345678. Here's a different way to look at it.

Let's ignore the odd numbers for now.

Will work on this later.
