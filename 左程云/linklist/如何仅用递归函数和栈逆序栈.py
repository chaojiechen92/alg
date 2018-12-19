def reverse(stack):
    if not stack:
        return

    def getbottumval(s):
        if len(s) == 1:
            return s.pop()
        val = s.pop()
        ret = getbottumval(s)
        s.append(val)
        return ret

    bottum_val = getbottumval(stack)
    reverse(stack)
    stack.append(bottum_val)
    return


if __name__ == "__main__":
    n = [1, 2, 3]
    reverse(n)
    print(n)
