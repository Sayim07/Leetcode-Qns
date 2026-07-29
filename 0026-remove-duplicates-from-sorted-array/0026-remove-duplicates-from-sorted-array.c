int removeDuplicates(int* a, int n) {
    int i=0, j=1, r=1;

    while(j < n){
        if(a[j] == a[j-1]){
            j++;
        }
        else{
            a[i+1] = a[j];
            i++;
            r++;
            j++;
        }
    }
    return r;
}