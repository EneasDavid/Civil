import java.util.Scanner;

public class Conversor {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int valorDecimal, valorBinario;
        String valorHexadecimal;
        
        System.out.println("Qual tipo da entrada?\n1.decimal\n2.binario\n3.hexadecimal");
        int tipoEntrada = input.nextInt();

        System.out.println("Dsigite o valor a ser convertido:");
        String entrada = input.next();

        switch (tipoEntrada) {
            case 1:
                // Converter para binário
                valorBinario = Integer.parseInt(entrada, 10);
                // Converter para hexadecimal
                valorHexadecimal = Integer.toHexString(Integer.parseInt(entrada));
                System.out.println("Valor em binário: " + Integer.toBinaryString(valorBinario) + "\nValor em hexadecimal: " + valorHexadecimal);
                break;
            case 2:
                // Converter para decimal
                valorDecimal = Integer.parseInt(entrada, 2);
                // Converter para hexadecimal
                valorHexadecimal = Integer.toHexString(valorDecimal);
                System.out.println("Valor em decimal: " + valorDecimal + "\nValor em hexadecimal: " + valorHexadecimal);
                break;
            case 3:
                // Converter para decimal
                valorDecimal = Integer.parseInt(entrada, 16);
                // Converter para binário
                valorBinario = Integer.parseInt(entrada, 16);
                System.out.println("Valor em decimal: " + valorDecimal + "\nValor em binário: " + Integer.toBinaryString(valorBinario));
                break;
            default:
                System.out.println("Opção inválida. Execute o programa novamente.");
        }
        input.close();
    }
}
