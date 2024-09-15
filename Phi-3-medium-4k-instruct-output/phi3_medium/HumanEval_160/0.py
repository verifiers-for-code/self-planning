def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    

 1. Initialize the result with the first operand.
2. Loop through the operator list and operand list simultaneously.
3. Apply the operator to the result and the next operand.
4. Return the result.
    """
    # Step 1: Initialize the result with the first operand
    result = operand[0]

    # Step 2: Loop through the operator list and operand list simultaneously
    for op, num in zip(operator, operand[1:]):
        # Step 3: Apply the operator to the result and the next operand
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            result //= num
        elif op == '**':
            result **= num

    # Step 4: Return the result
    return result