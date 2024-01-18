"use client";
import React, { useState } from "react";
import styles from "./page.module.css";

export default function Home() {
  // inicializar uma variável reativa que vai receber o resultado da requisição
  const [resultado, setResultado] = useState(
    "Nenhuma requisição foi realizada..."
  );

  // função para fazer a requisição ao container do back-end
  async function fazerRequisicao() {
    try {
      // fazer uma requisição para a porta do container do back-end
      const response = await fetch("http://localhost:8000/");
      // receber o retorno da requisição e coletar a resposta em formato json
      const data = await response.json();
      // setar o retorno da requisição como o novo valor da variável resultado
      setResultado(data["message"]);
    } catch (err) {
      // mostrar um alerta caso a requisição não tenha sido realizada por algum motivo
      alert("Requisição não foi realizada");
    }
  }

  return (
    <main className={styles.main}>
      <h1 style={{ marginBottom: 20 }}>
        MBA em Engenharia de Software | MBA USP/Esalq
      </h1>
      {/* botão que faz a requisição quando clicado */}
      <button
        style={{ padding: 10, margin: 20, fontSize: 24 }}
        onClick={fazerRequisicao}
      >
        Fazer requisição ao back-end
      </button>
      {/* elemento que printa dinamicamente o valor da variável resultado */}
      <h2>Resultado: {resultado}</h2>
    </main>
  );
}
