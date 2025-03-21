package week14.Leetcode_2115_FindAllPossibleRecipesfromGivenSupplies;

import java.util.*;

public class Leetcode_2115_FindAllPossibleRecipesfromGivenSupplies_FirstCommit {
    class Solution {
        public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
            HashSet<String> suppliesSet = new HashSet<>();
            List<String> result = new ArrayList<>();

            for(String supply : supplies){
                suppliesSet.add(supply);
            }

            int prev = 0;
            do {
                prev = suppliesSet.size();
                for(int i = 0 ; i<recipes.length ; i++){
                    boolean isAllThere = true;
                    for(String ingredient : ingredients.get(i)){
                        if(!suppliesSet.contains(ingredient)){
                            isAllThere = false;
                            break;
                        }
                    }
                    if(isAllThere) suppliesSet.add(recipes[i]);
                }
            } while(prev != suppliesSet.size());

            for(int i = 0 ; i<recipes.length ; i++){
                boolean isAllThere = true;
                for(String ingredient : ingredients.get(i)){
                    if(!suppliesSet.contains(ingredient)){
                        isAllThere = false;
                        break;
                    }
                }
                if(isAllThere) result.add(recipes[i]);
            }

            return result;
        }
    }
}
