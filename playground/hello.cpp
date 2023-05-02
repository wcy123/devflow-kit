#include <iostream>
#include <any>
#include <cassert>
using namespace std;
template <int act_fix, int channel>
struct CostVolume
{
    void operator()(int x)
    {
       cout << "hello x " << x;
    }
};

template <int channel>
struct CostVolume<0, channel>
{
    void operator()(int x)
    {
        cout << "channel " << channel;
    }
};

void cost_volume(int act_fix, int channel)
{
    if (act_fix == 0 && channel == 32)
    {
        // enable const folding optimization.
        cost_volume_real(0, 32, 100);
    } 
}
int main(int argc, char *argv[])
{
    any x = 100;
    cout << "hello world" << endl;
    cost_volume(0, 32);
}