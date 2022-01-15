from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #   1. 모든 숫자 로그는 문자 로그 뒤에 온다.
        #   2. 문자를 in order로 정렬한다.
        #   3. 숫자는 식별자를 기준으로 정렬한다.

        #   리스트 요소들의 시작이 d인지 l인지 식별

        


s = Solution()
print(s.reorderLogFiles(["dig1 8 1 5 1", "let1 art can",
      "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
