# import bisect
#
#
# def count(x, y, n, NoOfY):
#     if x == 0:
#         return 0
#     if x == 1:
#         return NoOfY[0]
#     idx = bisect.bisect_right(y, x)
#     ans = n - idx
#     ans += NoOfY[0] + NoOfY[1]
#     if x == 2:
#         ans -= NoOfY[3] + NoOfY[4]
#     if x == 3:
#         ans += NoOfY[2]
#     return ans
#
#
# def count_pairs(X, Y, m, n):
#     NoOfY = [0] * 5
#     for i in range(n):
#         if Y[i] < 5:
#             NoOfY[Y[i]] += 1
#     Y.sort()
#     total_pairs = 0
#     for x in X:
#         total_pairs += count(x, Y, n, NoOfY)
#     return total_pairs
#
#
# # Driver Code
# if __name__ == '__main__':
#     X = [2, 1, 6]
#     Y = [1, 5]
#     print("Total pairs = ", count_pairs(X, Y, len(X), len(Y)))


# code
t = int(input())


def count_fr(lst, start=0):
    count_res = [0] * 5
    indx = 0
    for i in range(1, 5):
        while i == lst[indx]:
            count_res[i] += 1
            indx += 1
    return count_res


for tt in range(t):
    m, n = (int(x) for x in input().split())
    xarr = [int(x) for x in input().split()]
    yarr = [int(x) for x in input().split()]
    xarr.sort()
    yarr.sort()
    """
    Rule- For any pair xx and yy from xarr and yarr resp. if yy > xx  and xx is 3 and above
    then this pair is valid pair. For Eg. take any xx greater than 3 and yy greater than 3 ie. from
    4 onwards, xx and yy will always be a valid pair
    Rule for '1' as xx-For handling one-All non one element from arr will make valid pair with each '1' in yarr
                 No. of ones in arrx are redundant[Handeled Seperately (1)]
    Rule for '2' ax xx-Since any pair with yy as '1' from yarr has been taken care of, pair with
              '2' are (2,3)-not valid(8<9) (2,4)-not valid(16==16) (2,5),(2,6),(2,7).... All pairs
              with xx as '2' and yy as '5' or above are valid pair[Handeled Seperately (2)]
    Rule for '3' as xx-  For yy less than 3 ie with 2 (3,2) is valid as 9>8[Handeled Seperately (3)]
                General rule applies for all yy greater than 3 as (3,4),(3,5),(3,6).... are valid pairs.
    Conclusion- After taking care of rule for '1' , '2' and '3' we can apply genral rule for xx=3 and hence
    yy>=4
    """
    ans_count = 0
    x_indx = 0
    y_indx = 0
    countx = count_fr(xarr)
    county = count_fr(yarr)
    # handling one [Handeled Seperately (1)]
    ans_count += county[1] * (m - countx[1])  # county[1] gives the no of '1' in yarr simillarly for xarr
    # handling 3 as xx and 2 as yy [Handeled Seperately (3)]
    ans_count += countx[3] * county[2]  # countx[3] gives the no of '3' in xarr
    # handling 2 as xx and yy>4    [Handeled Seperately (2)]
    ans_count += (n - sum(county)) * countx[2]  # sum(county) gives total count of elements having value <=4
    # Taking elements from xarr with value 3 and above and hence taking elements from yarr with
    # value 4 and above
    while xarr[x_indx] <= 2:
        x_indx += 1
    while x_indx < m and y_indx < n:
        if xarr[x_indx] >= yarr[y_indx]:
            y_indx += 1
            continue
        ans_count += n - y_indx
        x_indx += 1
    print(ans_count)
