var num_list = [3,5,2,7];

var length = num_list.length;

function bubble_sort(num_list){
    for (var i = 0; i < length; i++){
        for (var k = 0; k < length - i - 1; k++){
            if (num_list[k] > num_list[k+1]){
                var tmp = num_list[k];
                num_list[k] = num_list[k+1];
                num_list[k+1] = tmp;
            }
        }
    }
    return num_list;
}

var ans = bubble_sort(num_list);
console.log(ans);