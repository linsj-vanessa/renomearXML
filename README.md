# Renomear XML – NFe (Padrão Promax)

Ferramenta em Python com interface gráfica para **renomear arquivos XML de Nota Fiscal Eletrônica (NFe)** com base na **chave de acesso (44 dígitos)**.

O nome final segue o padrão exigido pelo **sistema Promax (AMBEV)** para **notas fiscais de entrada**:

```

<chave_de_acesso>-nfe.xml

```

---

## 🖥️ Funcionalidades

- Interface gráfica simples (Tkinter)
- Seleção da pasta onde estão os XMLs
- Identificação automática da **chave de acesso (44 números)**
- Renomeação segura dos arquivos
- Ignora arquivos que não seguem o padrão esperado
- Evita sobrescrever arquivos já existentes

---

## 📁 Exemplo de funcionamento

### Arquivo original
```

26260107526557002153550010010492111425887832-InPut - d2be31cb.xml

```

### Arquivo final
```

26260107526557002153550010010492111425887832-nfe.xml

````

---

## 🚀 Como executar (modo script)

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/renomear-xml-nfe.git
````

2. Execute o script:

```bash
python script.py
```

3. Escolha a pasta com os XMLs
4. Clique em **Renomear arquivos**

---

## 📦 Versão executável (.exe)

O projeto pode ser convertido em `.exe` usando **PyInstaller**, permitindo uso em máquinas **sem Python instalado**.

Exemplo:

```bash
pyinstaller --onefile --windowed script.py
```

O executável será gerado na pasta:

```
dist/
```

---

## ⚙️ Personalização do sufixo (`-nfe`)

O sufixo `-nfe` pode ser facilmente alterado para atender outros sistemas ou regras.

No código, basta modificar esta linha:

```python
novo_nome = f"{chave_44}-nfe.xml"
```

### Exemplos:

```python
# NFC-e
novo_nome = f"{chave_44}-nfce.xml"

# CT-e
novo_nome = f"{chave_44}-cte.xml"

# Qualquer outro padrão
novo_nome = f"{chave_44}-entrada.xml"
```

Assim, a ferramenta pode ser adaptada para **qualquer padrão de nomenclatura**, não ficando restrita apenas ao Promax.

---

## 🧠 Regra utilizada

* O script identifica **qualquer sequência de 44 números** no nome do arquivo
* Essa sequência é tratada como **chave de acesso da NFe**
* Todo o restante do nome original é descartado

Essa abordagem garante robustez mesmo quando o nome do arquivo contém:

* textos adicionais
* GUIDs
* espaços
* hífens
* padrões variados

---

## 🏢 Contexto corporativo

Este projeto foi criado para atender a uma necessidade prática de **importação de XMLs de NFe no sistema Promax (AMBEV)**, que exige nomenclatura padronizada para notas fiscais de entrada.

---

## 📄 Licença

Uso livre para fins pessoais ou corporativos.
Adapte conforme sua necessidade.

