def isPrime(N):
    if N == 1 or N == 2:
        return False

    for i in range(2, N):
        if N%i == 0:
            return False

    return True

def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):

                N = nums[i] + nums[j] + nums[k]
                if isPrime(N):
                    answer += 1

    return answer