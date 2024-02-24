package org.code.practice.problems;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

public class MapVSFlatMap {

    public static void run () {
        List<List<Integer>> rdd = new ArrayList<List<Integer>>();
        for (int i = 0 ; i < 4 ; i++) {
            List<Integer> row = new ArrayList<Integer>();
            row.add(i);
            row.add(i + 10);
            rdd.add(row);
        }
        List<Integer> func1Res = rdd.stream().map( item -> {
            return item.get(0) + item.get(1);
        } ).collect(Collectors.toList());
        System.out.println(func1Res);
        List<Integer> func2Res = rdd.stream().flatMap(Collection::stream).collect(Collectors.toList());
        System.out.println(func2Res);
    }
}
