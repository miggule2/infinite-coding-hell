package week32;

import java.util.*;

public class Programmers_완주하지못한선수{
    public String solution(String[] participant, String[] completion) {
        String result = null;
        HashMap<String,Integer> participantSet = new HashMap<>();
        for(String person : participant){
            if(!participantSet.containsKey(person)) participantSet.put(person,0);

            participantSet.put(person, participantSet.get(person)+1);
        }

        for(String person: completion){
            participantSet.put(person, participantSet.get(person)-1);
        }

        for(String person: participantSet.keySet()){
            if(participantSet.get(person) != 0) {result = person; break;}
        }

        return result;
    }
}