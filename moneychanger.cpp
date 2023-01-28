#include <bits/stdc++.h>
using namespace std;
int dp[10005];

int main() {
	int n, v; cin >> n >> v;
	int coin[n+1];
	for (int i = 1; i <= n; i++) {
		cin >> coin[i];
	}
	dp[0] = 0;
	for (int i = 1; i <= v; i++) {
		dp[i] = 10000000;
	}
	for (int i = 1; i <= v; i++) {
		for (int j = 1; j <= n; j++) {
			if (coin[j] <= i) {
				dp[i] = min(dp[i], dp[i-coin[j]] + 1);
			}
		}
	}
	if (dp[v] == 10000000) {
		cout << -1;
	}
	else {
		cout << dp[v];
	}
	return 0;
	}
