# Exercício Express: operações POST

## Executar

No terminal desta pasta, instale as dependências e inicie o servidor:

```bash
npm install
npm start
```

O servidor usa a porta 3001. Acesse `http://localhost:3001/` para confirmar que está ativo.

## Testar no Postman

1. Inicie o servidor com `npm start` e mantenha esse terminal aberto.
2. No Postman, importe o arquivo `postman/site-soma.postman_collection.json`.
3. Abra uma das requisições da coleção e confirme que o método é `POST`.
4. A requisição usa `http://localhost:3001` e, na aba **Body**, envia JSON em **raw**. Pressione **Send** para conferir a resposta.

Para montar a requisição manualmente, use a URL `http://localhost:3001/soma` e este corpo:

```json
{
  "a": 7,
  "b": 5
}
```

A resposta esperada é `O resultado da soma de 7 e 5 é 12`. A coleção também verifica o status HTTP e o texto da resposta em cada operação.

Para repetir o teste com as outras operações, altere a URL:

| Operação | URL | Exemplo de resposta para 7 e 5 |
| --- | --- | --- |
| Soma | `http://localhost:3001/soma` | `... é 12` |
| Subtração | `http://localhost:3001/subtracao` | `... é 2` |
| Multiplicação | `http://localhost:3001/multiplicacao` | `... é 35` |
| Divisão | `http://localhost:3001/divisao` | `... é 1.4` |

Todas as rotas recebem um objeto JSON com os campos numéricos `a` e `b`. Campos ausentes ou inválidos retornam HTTP 400; a divisão por zero também é rejeitada.