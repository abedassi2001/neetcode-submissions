class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length() != t.length()) return false; 

        HashMap<Character,Integer> map =  new HashMap<>();

        for(char c : s.toCharArray()){
            map.put(c , map.getOrDefault(c,0) + 1);
        }

        for(char k : t.toCharArray()){
            int counter = map.getOrDefault(k , 0) ;
        
            if (counter == 0 ) return false ;

            map.put(k , map.get(k) - 1);
        }
        return true ;
    }
}
