class Solution {
    public boolean isAnagram(String s, String t) {
        int firstLength = s.length() - 1; 
        int secondLength = t.length() - 1;
        if(secondLength != firstLength)return false ;
        HashMap<Character ,Integer> map = new HashMap<>();

        for (int i = 0 ; i <= secondLength ; i++){
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }

        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            if ((map.get(c) == null)||(map.get(c) == 0)  ) {
                return false;
            }
            map.put(c, map.get(c) - 1);
        }

        return true ;
    }
}
