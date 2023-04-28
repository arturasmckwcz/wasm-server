extern "C"
{
    int fibonacci(int n)
    {
        int a = 0;
        int b = 1;
        int tmp;

        for (int i = 0; i < n; i++)
        {
            tmp = a + b;
            a = b;
            b = tmp;
        }

        return a;
    }

    int main() { return 0; }
}