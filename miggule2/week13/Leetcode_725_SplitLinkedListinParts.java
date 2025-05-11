package week13;

public class Leetcode_725_SplitLinkedListinParts {

    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    class Solution {
        public ListNode[] splitListToParts(ListNode head, int k) {
            ListNode p = head; // head를 움직이지 않게 하기 위한 변수

            // list 길이 구하기
            int len = 0;
            while(p != null && p.next != null){
                len++;
                p = p.next;
            }

            ListNode[] result = new ListNode[k];

            // 배열에 들어갈 리스트 크기를 구하기 위한 변수
            int value = len/k;
            int mod = len%k;

            for (int i = 0; i < k; i++) {
                int count = i <= mod ? value+1 : value; // 문제 조건에 알맞게 list 크기를 k로 나눈 몫에다 나머지에 해당하는 개수의 배열에는 +1.
                ListNode dummy = new ListNode(0); // 더미 노드 사용 (풀이 참고)
                ListNode pointer = dummy; // 리스트를 생성할 때 움직일 포인트
                // 배열 각각에 들어갈 list 생성
                for (int j = 0; j < count && head != null; j++) {
                    pointer.next = new ListNode(head.val);
                    pointer = pointer.next;
                    head = head.next;
                }
                result[i] = dummy.next; // 더미 노드 다음 노드를 결과에 저장
            }

            return result;
        }
    }
}
