#include <bits/stdc++.h>
using namespace std;

int main() {
	long long a; cin >> a; string output = "Prime";
	for (int i = 2; i <= floor(sqrt(a)); i++) {
		if (a % i == 0) {
			output = "Not Prime";
			cout << "Your number is divisible by " << i << "\n";
			break;
		}
	}
	cout << output;
	return 0;
}
