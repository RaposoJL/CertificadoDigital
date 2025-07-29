-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 27/07/2025 às 00:08
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `certificado_digital_novo`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `aluno`
--

CREATE TABLE `aluno` (
  `id` int(11) NOT NULL,
  `nome_completo` varchar(100) DEFAULT NULL,
  `nome_mae` varchar(100) DEFAULT NULL,
  `nome_pai` varchar(100) DEFAULT NULL,
  `cpf` char(14) DEFAULT NULL,
  `municipio` varchar(100) DEFAULT NULL,
  `estado` char(2) DEFAULT NULL,
  `data_nascimento` date DEFAULT NULL,
  `rg` varchar(20) DEFAULT NULL,
  `orgao_expedidor` varchar(50) DEFAULT NULL,
  `turma` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `base_comum_disciplinas`
--

CREATE TABLE `base_comum_disciplinas` (
  `id` int(11) NOT NULL,
  `aluno_id` int(11) DEFAULT NULL,
  `nome_disciplina` varchar(100) DEFAULT NULL,
  `ano_escolar` int(11) DEFAULT NULL,
  `ano_realizacao` int(11) DEFAULT NULL,
  `carga_horaria` int(11) DEFAULT NULL,
  `frequencia` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `certificado`
--

CREATE TABLE `certificado` (
  `id` int(11) NOT NULL,
  `aluno_id` int(11) DEFAULT NULL,
  `data_emissao` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `curso_tecnico`
--

CREATE TABLE `curso_tecnico` (
  `id` int(11) NOT NULL,
  `aluno_id` int(11) DEFAULT NULL,
  `nome_curso` varchar(100) DEFAULT NULL,
  `eixo_tecnologico` varchar(100) DEFAULT NULL,
  `perfil_profissional` text DEFAULT NULL,
  `carga_horaria_total` int(11) DEFAULT NULL,
  `data_conclusão` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `curso_tecnico_disciplinas`
--

CREATE TABLE `curso_tecnico_disciplinas` (
  `id` int(11) NOT NULL,
  `curso_id` int(11) DEFAULT NULL,
  `nome_disciplina` varchar(100) DEFAULT NULL,
  `ano_escolar` int(11) DEFAULT NULL,
  `ano_realizacao` int(11) DEFAULT NULL,
  `carga_horaria` int(11) DEFAULT NULL,
  `frequencia` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `eletiva_disciplinas`
--

CREATE TABLE `eletiva_disciplinas` (
  `id` int(11) NOT NULL,
  `aluno_id` int(11) DEFAULT NULL,
  `nome_disciplina` varchar(100) DEFAULT NULL,
  `ano_escolar` int(11) DEFAULT NULL,
  `ano_realizacao` int(11) DEFAULT NULL,
  `carga_horaria` int(11) DEFAULT NULL,
  `frequencia` decimal(5,2) DEFAULT NULL,
  `turma` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `funcionario`
--

CREATE TABLE `funcionario` (
  `id` int(11) NOT NULL,
  `login` varchar(50) DEFAULT NULL,
  `senha` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `trilha_disciplinas`
--

CREATE TABLE `trilha_disciplinas` (
  `id` int(11) NOT NULL,
  `aluno_id` int(11) DEFAULT NULL,
  `nome_disciplina` varchar(100) DEFAULT NULL,
  `ano_escolar` int(11) DEFAULT NULL,
  `ano_realizacao` int(11) DEFAULT NULL,
  `carga_horaria` int(11) DEFAULT NULL,
  `frequencia` decimal(5,2) DEFAULT NULL,
  `turma` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `aluno`
--
ALTER TABLE `aluno`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `base_comum_disciplinas`
--
ALTER TABLE `base_comum_disciplinas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `aluno_id` (`aluno_id`);

--
-- Índices de tabela `certificado`
--
ALTER TABLE `certificado`
  ADD PRIMARY KEY (`id`),
  ADD KEY `aluno_id` (`aluno_id`);

--
-- Índices de tabela `curso_tecnico`
--
ALTER TABLE `curso_tecnico`
  ADD PRIMARY KEY (`id`),
  ADD KEY `aluno_id` (`aluno_id`);

--
-- Índices de tabela `curso_tecnico_disciplinas`
--
ALTER TABLE `curso_tecnico_disciplinas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `curso_id` (`curso_id`);

--
-- Índices de tabela `eletiva_disciplinas`
--
ALTER TABLE `eletiva_disciplinas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `aluno_id` (`aluno_id`);

--
-- Índices de tabela `funcionario`
--
ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `trilha_disciplinas`
--
ALTER TABLE `trilha_disciplinas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `aluno_id` (`aluno_id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `aluno`
--
ALTER TABLE `aluno`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `base_comum_disciplinas`
--
ALTER TABLE `base_comum_disciplinas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `certificado`
--
ALTER TABLE `certificado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `curso_tecnico`
--
ALTER TABLE `curso_tecnico`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `curso_tecnico_disciplinas`
--
ALTER TABLE `curso_tecnico_disciplinas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `eletiva_disciplinas`
--
ALTER TABLE `eletiva_disciplinas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `trilha_disciplinas`
--
ALTER TABLE `trilha_disciplinas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `base_comum_disciplinas`
--
ALTER TABLE `base_comum_disciplinas`
  ADD CONSTRAINT `base_comum_disciplinas_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES `aluno` (`id`);

--
-- Restrições para tabelas `certificado`
--
ALTER TABLE `certificado`
  ADD CONSTRAINT `certificado_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES `aluno` (`id`);

--
-- Restrições para tabelas `curso_tecnico`
--
ALTER TABLE `curso_tecnico`
  ADD CONSTRAINT `curso_tecnico_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES `aluno` (`id`);

--
-- Restrições para tabelas `curso_tecnico_disciplinas`
--
ALTER TABLE `curso_tecnico_disciplinas`
  ADD CONSTRAINT `curso_tecnico_disciplinas_ibfk_1` FOREIGN KEY (`curso_id`) REFERENCES `curso_tecnico` (`id`);

--
-- Restrições para tabelas `eletiva_disciplinas`
--
ALTER TABLE `eletiva_disciplinas`
  ADD CONSTRAINT `eletiva_disciplinas_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES `aluno` (`id`);

--
-- Restrições para tabelas `trilha_disciplinas`
--
ALTER TABLE `trilha_disciplinas`
  ADD CONSTRAINT `trilha_disciplinas_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES `aluno` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
