# write a python code to print n natural numbers using a for loop
class natural_numbers:
    def __init__(self, n):
        self.n = n

    def print_natural_numbers(self):
        for i in range(1, self.n + 1):
            print(i)
# Example usage
if __name__ == "__main__":
    n = 10
    natural_numbers_instance = natural_numbers(n)
    print(f"The first {n} natural numbers are:")
    natural_numbers_instance.print_natural_numbers()


# convert the above code to JAVA
public class NaturalNumbers {
    private int n;

    public NaturalNumbers(int n) {
        this.n = n;
    }

    public void printNaturalNumbers() {
        for (int i = 1; i <= n; i++) {
            System.out.println(i);
        }
    }

    public static void main(String[] args) {
        int n = 10;
        NaturalNumbers naturalNumbersInstance = new NaturalNumbers(n);
        System.out.println("The first " + n + " natural numbers are:");
        naturalNumbersInstance.printNaturalNumbers();
    }
}

# convert the above code to Golang
package main
import "fmt"
type NaturalNumbers struct {
    n int
}
func (nn *NaturalNumbers) printNaturalNumbers() {
    for i := 1; i <= nn.n; i++ {
        fmt.Println(i)
    }
}
func main() {    n := 10
    naturalNumbersInstance := NaturalNumbers{n: n}
    fmt.Printf("The first %d natural numbers are:\n", n)
    naturalNumbersInstance.printNaturalNumbers()
}
