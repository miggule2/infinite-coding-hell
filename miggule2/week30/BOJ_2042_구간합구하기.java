package week30;

import java.util.*;
import java.io.*;

public class BOJ_2042_구간합구하기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n,k,m;
        String[] input= br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        k = Integer.parseInt(input[1]);
        m = Integer.parseInt(input[2]);

        ArrayList<Long> arr = new ArrayList<>();
        long[] segTree = new long[n * 4];
        for(int i = 0; i < n; i++){
            long num = Long.parseLong(br.readLine());
            arr.add(num);
        }

        build(arr,segTree,0,n-1,0);

        for(int i = 0; i < k+m; i++){
            long choice, a, b;
            input= br.readLine().split(" ");
            choice = Long.parseLong(input[0]);
            a = Long.parseLong(input[1]);
            b = Long.parseLong(input[2]);

            if(choice == 1){
                change(segTree,0,n-1,a-1,b,0);
            }
            else System.out.println(getSum(segTree,a-1,b-1,0,n-1,0));
        }
    }

    // 구간합을 구하기 위한 세그먼트 트리 생성 함수
    private static long build(ArrayList<Long> arr, long[] segTree,long start, long end, int index){
        if(start == end) return segTree[index] = arr.get((int)start); // 리프노드

        // 자식 노드 채우기(자식 노드의 합)
        long mid = (start+end)/2;
        return segTree[index] = build(arr,segTree,start,mid,index*2+1)+build(arr,segTree,mid+1,end,index*2+2);
    }

    // 세그먼트 트리 내 요소 변경 함수
    private static long change(long[] segTree, long nowStart, long nowEnd, long destination, long toChange, int index){
        if(nowStart > destination || nowEnd < destination) return segTree[index]; // destination이 구간 내에 없는 경우
        if(nowStart == destination && nowEnd == destination) return segTree[index] = toChange; // 현재 구간이 정확시 destination인 경우

        // 부분적으로 걸쳐 있을 경우 다시 내려감 + 올라오면서 자식 노드의 합으로 고침
        long mid = (nowStart+nowEnd)/2;
        return segTree[index] = change(segTree,nowStart,mid,destination,toChange,index*2+1) + change(segTree,mid+1,nowEnd,destination,toChange,index*2+2);
    }

    // 세그먼트 트리 구간 합 구하는 함수
    private static long getSum(long[] segTree, long start, long end, long nowStart, long nowEnd, int index){
        if(nowStart > end || nowEnd < start) return 0; // 현재 구간이 구하는 범위 밖인 경우
        if(start <= nowStart && nowEnd <= end) return segTree[index]; // 현재 구간이 구하는 범위에 완전히 포함되는 경우

        // 부분적으로 걸쳐 있을 경우 다시 내려감 + 올라오면서 자식 노드의 합을 리턴
        long mid = (nowStart+nowEnd)/2;
        return getSum(segTree,start,end,nowStart,mid,index*2+1) + getSum(segTree,start,end,mid+1,nowEnd,index*2+2);
    }
}
