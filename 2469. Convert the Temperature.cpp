class Solution
{
public:
    vector<double> convertTemperature(double celsius)
    {
        vector<double> result;
        result.push_back(celsius + 273.15);
        result.push_back(celsius * 1.8 + 32.0);
        return result;
    }
};