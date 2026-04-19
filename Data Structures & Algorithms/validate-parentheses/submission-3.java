class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character,Character> hash = new HashMap<>();
        hash.put(']','[');
        hash.put(')','(');
        hash.put('}','{');
        HashSet<Character> set = new HashSet<>();
        set.add('(');
        set.add('[');
        set.add('{');

        for (int i = 0 ; i < s.length() ; i++){
            if(set.contains(s.charAt(i)) )stack.add(s.charAt(i));
            
            else{
                if (stack.empty())return false;

                char top = stack.pop();
                if(hash.get(s.charAt(i)) != top)return false;

            }
        }
        if (!stack.empty())return false;
        return true ;
    }
}

