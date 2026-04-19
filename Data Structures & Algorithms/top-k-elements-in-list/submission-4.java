
class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) == null) {
                map.put(nums[i], 1);
            }
            else {
                map.put(nums[i], map.get(nums[i]) + 1);
            }
        }
        
        LinkedList<Integer>[] freq = new LinkedList[nums.length];

        for(int i = 0; i < nums.length; i++) {
            freq[i] = new LinkedList<>();
        }
        
        map.forEach((key, value) -> {
            freq[value - 1].add(key);
        });

        int[] max = new int[k];
        int index = 0;
        for (int i = freq.length - 1; i >= 0 ; i--) {
            if (freq[i].size() == 0)
                continue;
            
            for(Integer val : freq[i]) {
                max[index] = val;
                if (index == k - 1)
                    return max;
                index++;
            }
        }
        return max;
    }
}
