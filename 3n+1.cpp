#include <bits/stdc++.h>
using namespace std;

int main() {
	long long input;
	cin >> input;
	while (1 == 1) {
		cout << input << " ";
		if (input % 2 == 0) {
			input = input / 2;
		}
		else if (input % 2 == 1) {
			input = input * 3 + 1;
		}
		if (input == 1) {
			cout << input;
			break;
		}
	}
	
	return 0;
}
