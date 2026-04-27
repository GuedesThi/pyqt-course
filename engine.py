import math # usei para raiz quadrada

# responsável pelas operações de estatística
class StatsEngine:
    # método não precisa de uma instância da classe
    @staticmethod
    # método para pegar valores
    def get_data(text):
        try:
            # pega a string, divide por vírgulas, remove espaços e converte para float
            return [float(x.strip()) for x in text.split(",") if x.strip()]
        except ValueError:
            # se o usuário digitar algo que não é número
            return None

    # método não precisa de uma instância da classe
    @staticmethod
    # método para calcular a média
    def calc_mean(data):
        # quantidade de valores
        n = len(data)
        # soma dos valores
        soma = sum(data)
        # cálculo da média
        res = soma / n
        # fórmula da média
        formula = "μ = (Σ xᵢ) / n"
        # passo a passo da conta
        steps = f"1. Soma de todos os valores (Σ): {soma}\n2. Quantidade de elementos (n): {n}\n3. Cálculo: {soma} / {n} = {res:.2f}"
        return res, formula, steps

    # método não precisa de uma instância da classe
    @staticmethod
    # método para calcular variância
    def calc_variance(data):
        # quantidade de valores
        n = len(data)
        # verifica se o usuário colocou no mínimo 2 valores para a conta
        if n < 2: return 0, "", "Erro: Necessário ao menos 2 valores para variância amostral."
        # cálculo da média
        mean = sum(data) / n 
        # soma do quadrado das distâncias entre cada número e a média
        sq_diff = sum((x - mean) ** 2 for x in data)
        # resultado final
        res = sq_diff / (n - 1)
        # fórmula da variância
        formula = "s² = Σ(xᵢ - μ)² / (n - 1)"
        # passo a passo da conta
        steps = f"1. Média calculada (μ): {mean:.2f}\n2. Soma dos quadrados das diferenças: {sq_diff:.2f}\n3. Divisão por (n-1): {sq_diff:.2f} / {n-1} = {res:.4f}"
        return res, formula, steps

    # método não precisa de uma instância da classe
    @staticmethod
    # método para calcular desvio padrão
    def calc_std_dev(data):
        # separa os três resultados de calc_variance em três variáveis
        var, _, steps_v = StatsEngine.calc_variance(data)
        # cálculo do desvio padrão
        res = math.sqrt(var)
        # fórmula do desvio padrão
        formula = "σ = √s²"
        # passo a passo da conta
        steps = f"{steps_v}\n4. Extração da Raiz Quadrada: √{var:.4f} = {res:.4f}"
        return res, formula, steps
