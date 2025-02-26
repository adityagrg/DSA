class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sarr = s.toCharArray();
        char[] tarr = t.toCharArray();

        HashMap<Character, Integer> shm = new HashMap<>();
        HashMap<Character, Integer> thm = new HashMap<>();

        for (char ch : sarr) {
            if (shm.containsKey(ch)) {
                shm.put(ch, shm.get(ch) + 1);
            }
            else {
                shm.put(ch, 1);
            }
        }

        for (char ch : tarr) {
            if (thm.containsKey(ch)) {
                thm.put(ch, thm.get(ch) + 1);
            }
            else {
                thm.put(ch, 1);
            }
        }

        if (shm.equals(thm)) {
            return true;
        }
        else {
            return false;
        }
    }
}