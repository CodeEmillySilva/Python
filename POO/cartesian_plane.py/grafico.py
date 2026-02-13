import matplotlib.pyplot as plt

# Dados
meses = ["Jan", "Fev", "Mar", "Abr", "Mai"]
valores = [1.0, 4.0, 3.0, 5.0, 5.5]

# Criar o gráfico
plt.plot(meses, valores, marker='o', linestyle='-', color='blue', label='Linha 1')

# Personalização
plt.title('Variação Mensal')
plt.xlabel('Mês')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)

# Exibir
plt.tight_layout()
plt.show()
