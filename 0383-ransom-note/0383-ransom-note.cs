public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        Dictionary<char, int> dict = new();
        foreach(char c in magazine)
            if (dict.ContainsKey(c))
                dict[c]++;
            else
                dict.Add(c, 1);
        foreach(char c in ransomNote)
            if (dict.ContainsKey(c) && dict[c] > 0)
                dict[c]--;
            else
                return false;
        return true;
        
    }
}