import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """ 
        graph = collections.defaultdict(list) # key값이 없을 경우 미리 지정해 놓은 초기(default)값을 반환하는 dictionary
        for a, b in sorted(tickets): # sorted()는 정렬된 리스트를 반환
            graph[a].append(b) # graph에 a를 key로, b를 value로 추가

        route, stack = [], ['JFK'] # `JFK`에서 출발
        while stack: # stack이 비어있지 않을 때까지
            while graph[stack[-1]]: # stack의 마지막 값이 graph에 있을 때
                stack.append(stack.pop()) # stack의 마지막 값을 pop해서 stack에 추가
            route.append(stack.pop()) # stack이 비어있을 때까지 pop한 값을 route에 추가
            
        return route[::-1] # route를 역순으로 반환