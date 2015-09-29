class Solution{
	public:
		int removeDuplicates(int A[], n){
			if (n == 0) return 0;
			int index = 0;
			for (int i = 1; i < n; i++){
				if(A[index] ！= A[i]){
					A[++index] = A[i];
				}

			}
			return index + 1;

		}


}


int main(){
	Solution solution();
	int a[3] = {1, 1, 3}
	solution.removeDuplicates(a, 3);
	printf()
}