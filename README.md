# count_inc_end

This function counts from `start` to `end` with an increment of `inc`. If `is_exclusive` is `True`, the `end` value is excluded from the count. If `start` is equal to `end`, the function returns `None` if `is_exclusive` is `True`, else it prints `start`.

```python
## Signature
def count_inc_end(start: int, end: int, inc: int, is_exclusive: bool) -> None:
    """
    Count from `start` to `end` with an increment of `inc`.
    If `is_exclusive` is `True`, the `end` value is excluded from the count.
    If `start` is equal to `end`, the function returns `None` if `is_exclusive` is `True`, else it prints `start`.

    Args:
    start (int): the starting value of the count
    end (int): the ending value of the count
    inc (int): the increment value for each step of the count
    is_exclusive (bool): whether or not to exclude the end value from the count

    Returns:
    None

    Example:
    count_inc_end(2, 5, 1, False)
    # Output: 2 3 4 5
    """
    # function implementation here

      """
      

## Usage
This funtion can be used in any Python script that requires counting numbers within a range. Here are some examples of how to use it:

   # Import the function
  import count_inc_end

   # Count from 5 to 2 with an increment of 2, excluding the end value
  count_inc_end(5, 2, 2, True)

   # Count from 2 to 5 with an increment of 2, including the end value
  count_inc_end(2, 5, 2, False)

   # Count from -3 to -7 with an increment of 1, excluding the end value
  count_inc_end(-3, -7, 1, True)

   # Count from 2 to 5 with an increment of 1, including the end value
  count_inc_end(2, 5, 1, False)

   # Count from 5 to 2 with an increment of 2, including the end value
  count_inc_end(5, 2, 2, False)

   # Count from 6 to 2 with an increment of 2, including the end value
  count_inc_end(6, 2, 2, False)

## Contributing
If you find any bugs or issues with the count_inc_end function, feel free to open an issue or submit a pull request. We welcome contributions from the community.


