public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char, int> dict = new();
        if (s.Length != t.Length) return false;
        foreach(char c in s)
            if (dict.ContainsKey(c))
                dict[c] ++;
            else
                dict[c] = 1;
        foreach(char c in t)
            if (dict.ContainsKey(c) && dict[c] > 0)
                dict[c] --;
            else
                return false;
        return true;
    }
}