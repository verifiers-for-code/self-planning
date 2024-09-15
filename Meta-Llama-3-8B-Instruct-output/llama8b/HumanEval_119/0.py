def match_parens(lst):
    open_parens = 0
    close_parens = 0
    for s in lst:
        if s == '(':
            open_parens += 1
        elif s == ')':
            if open_parens == 0:
                return 'No'
            open_parens -= 1
    return 'Yes' if open_parens == 0 else 'No'