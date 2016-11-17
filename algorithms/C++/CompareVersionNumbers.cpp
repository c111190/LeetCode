class Solution {
public:
    int compareVersion(string version1, string version2) {
        int ans=0;
        string v1=version1, v2=version2;
        ans = compare(stoi(v1), stoi(v2));
        
        while(ans == 0 && (v1.size() > 1 || v2.size() > 1)){
            
            v1 = v1.find(".") != std::string::npos? v1.substr(v1.find(".")+1) : "0";
            v2 = v2.find(".") != std::string::npos? v2.substr(v2.find(".")+1) : "0";
            ans = compare(stoi(v1), stoi(v2));
        }
        
        return ans;
    }
    
    int compare( int num1 , int num2){
        
        if (num1 > num2)
            return 1;
        
        else if (num1 < num2)
            return -1;
        
        else
            return 0;
    }
};