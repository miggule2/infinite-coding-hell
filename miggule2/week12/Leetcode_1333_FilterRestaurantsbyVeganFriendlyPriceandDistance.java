package week12;

import java.util.*;
public class Leetcode_1333_FilterRestaurantsbyVeganFriendlyPriceandDistance {
    public List<Integer> filterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        HashMap<Integer, Queue<int[]>> map = new HashMap<>();
        Arrays.sort(restaurants,Comparator.comparingInt(a -> a[0]));
        for(int i =0; i < restaurants.length; i++){
            if(!map.containsKey(restaurants[i][1])) map.put(restaurants[i][1], new LinkedList<>());
            map.get(restaurants[i][1]).add(restaurants[i]);
        }
        List<Integer> result = new LinkedList<Integer>();

        ArrayList<Integer> setList = new ArrayList<Integer>(map.keySet());
        Collections.sort(setList);
        for(int rating : setList){
            int size = map.get(rating).size();
            for(int i = 0; i < size; i++){
                int[] restaurant = map.get(rating).poll();
                if( ((veganFriendly == 1 && restaurant[2] == 1) || veganFriendly == 0) && restaurant[3] <= maxPrice && restaurant[4] <= maxDistance ) result.addFirst(restaurant[0]);
            }
        }

        return result;
    }
}
