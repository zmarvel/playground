# Project 6 #

*in which we implement a hash table*

## `__init__(self, dict)` ##

First we define `m` and `n`, which signify the length of the array containing
the hash table and the number of items the hash table actually contains,
respectively.  If a dict was given, we can just set `m` to twice the length of
the input.  If not, 11.  We start by filling the array with `None`, then we put
all the items in the dictionary in our hash table.

## `__getitem__(self, key)` ##

To begin with, we hash the key.  If the cell in the array at the hashed index
is not empty, we can start looking in the chain of items there for the pair we
are looking for.  If we find an item in the chain with the key we are looking
for, we return its value.  In the case that we do not find such an item, or in
the case that the cell in the array at the hashed index was empty, we need to
raise a KeyError, because there is no value associated with the given key in the
table.

## `__setitem__(self, key, value)` ##

First, calculate α, which is the load factor of the hash table. We want to keep
it around 1/2.  If it's more than 1/2, we'll just reinitialize our hash table,
passing it itself. This will initialize it to twice its size. Next, we find our
key => value pair in the hash table. If there's no key => value pair chain there
already, we'll put one there with our pair in it. If there is a chain there,
we'll look down it for our key. If we find the key, we'll change its associated
value to the given value. If not, we'll just add the key => value pair to the
chain.

## `__delitem__(self, key)` ##

First we calculate α again. If it's less than 1/4, this time, our table is too
small. We need to cut it in half, so we just call our hash table constructor
again on itself, giving us an `m` value 1/2 of the previous. Now we need to look
for our key. If we find it, we just remove its key => value pair. If we aren't
able to find it in there, we raise a KeyError.

## `keys(self)` ##

Just iterate through the `data` array, which contains chains. At each chain,
iterate through the chain and add the keys we run over to a list. At the end of
the `data` array, return said list.
