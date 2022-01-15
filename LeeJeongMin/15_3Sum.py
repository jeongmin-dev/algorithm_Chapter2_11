from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #   숫자 리스트가 주어진다.
        #   세숫자[i, j, k]는 i != j, i != k, j != k
        #   세수의 합이 0이 되는 수를 리스트로 반환하세요.

        # 중복값을 사용할 수 없다 -> sort(): i(기준값) 중복값 체크
        # 0 < i면 빈리스트 -> sort()로 정렬 해주었기 때문에

        result = []     # 결과를 담아줄 빈리스트 생성
        # 중복값을 사용할 수 없다 -> sort(): i(기준값) 중복값 체크 [-1, 0, 1, 2, -1, -4] -> [-4, -1, -1, 0, 1, 2]
        nums.sort()

        for idx, num in enumerate(nums):
            # 만약 두번째 숫사가 왼쪽의 숫자와 같으면 (중복 숫자 찾기)
            if idx > 0 and num == nums[idx - 1]:
                continue
            # 두번째, 세번째 숫자
            l, r = idx+1, len(nums)-1

            while l < r:
                threeSum = num + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1

        return result


s = Solution()
# print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([]))
# print(s.threeSum([0]))
