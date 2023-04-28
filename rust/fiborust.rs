#[no_mangle]
pub extern "C" fn fibonacci(n: i32) -> i32 {
    if n <= 0 {
        return 0;
    } else if n == 1 {
        return 1;
    } else {
        let mut fib1 = 1;
        let mut fib2 = 1;
        for _i in 2..n {
            let next = fib1 + fib2;
            fib1 = fib2;
            fib2 = next;
        }
        return fib2;
    }
}

fn main() {
    for i in 2..10+1 {
        println!("{index}: {fib}", index=i, fib=fibonacci(i));
    }
}