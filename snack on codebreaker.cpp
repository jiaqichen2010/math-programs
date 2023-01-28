#include <bits/stdc++.h>
using namespace std;

int arr[1000005];
int memo[1000005];

int maxsum(int i) {
	if (memo[i] != -1) {
		return memo[i];
	}
	if (i == 0) {
		memo[i] = arr[0];
		return memo[i];
	}
	else {
		memo[i] = max(arr[i], maxsum(i-1) + arr[i]);
		return memo[i];
	}
}

int main() {
	long long n; cin >> n;
	string input; cin >> input;
	for (int x = 0; x < 1000005; x++) {
		memo[x] = -1;
	}
	for (int i = 0; i < n; i++) {
		if (input[i] == 'M') {
			arr[i] = -2;
		}
		else {
			arr[i] = input[i]-'0'; // input[i] (character) - '0' (character) = integer version of it.
		}
	}
	
	for (int k = 0; k < n; k++) {
		maxsum(k);
	}
	
	int var = memo[max_element(memo, memo+n)-memo];
	
	if (var >= 0) {
		cout << var;
	}
	else {
		cout << "0";
	}
	cout << "\n";
	return 0;
}
