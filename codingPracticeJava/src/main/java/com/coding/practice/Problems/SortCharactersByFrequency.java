package com.coding.practice.Problems;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class SortCharactersByFrequency {

    public static void run () {
        String input = "tree";
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 0 ; i < input.length() ; i++) {
            char temp = input.charAt(i);
            if (!map.containsKey(temp)) {
                map.put(temp, 0);
            }
            int prevVal = map.get(temp);
            map.put(temp, prevVal + 1);
        }

        List<String> resultI = map.entrySet()
                .stream()
                .sorted((a, b) -> {
                    return b.getValue() - a.getValue();
                })
                .map(obj -> {
                    StringBuilder temp = new StringBuilder();
                    for (int i = 0 ; i < obj.getValue() ; i++) {
                        temp.append(obj.getKey());
                    }
                    return temp.toString();
                })
                .toList();
        StringBuilder builder = new StringBuilder();
        for (String c : resultI) {
            builder.append(c);
        }
        String result = builder.toString();
        System.out.println(result);
    }
}
