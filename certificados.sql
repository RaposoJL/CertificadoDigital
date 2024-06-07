-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 04/06/2024 às 20:09
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `certificados`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `bdalunos`
--

CREATE TABLE `bdalunos` (
  `instituicao` varchar(100) NOT NULL,
  `nome_completo` varchar(100) NOT NULL,
  `nome_mae` varchar(100) NOT NULL,
  `nome_pai` varchar(100) NOT NULL,
  `municipio` varchar(60) NOT NULL,
  `nacionalidade` varchar(60) NOT NULL,
  `data_nascimento` varchar(250) NOT NULL,
  `CPF` varchar(11) NOT NULL,
  `rg` varchar(10) NOT NULL,
  `orgao_expedidor` varchar(6) NOT NULL,
  `curso` varchar(40) NOT NULL,
  `data_conclusão` varchar(250) NOT NULL,
  `id` int(11) NOT NULL,
  `turma` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `bdalunos`
--

INSERT INTO `bdalunos` (`instituicao`, `nome_completo`, `nome_mae`, `nome_pai`, `municipio`, `nacionalidade`, `data_nascimento`, `CPF`, `rg`, `orgao_expedidor`, `curso`, `data_conclusão`, `id`, `turma`) VALUES
('Ministro Fernando Lyra', 'Amanda Souza', 'Eduardo Souza', 'Carla Souza', 'Caruaru', 'Brasil', '2006-04-15 00:00:00', '401.515.720', '28395472', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 338, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'André Santos', 'Rogério Santos ', 'Beatriz Santos', 'Caruaru', 'Brasileira', '28 de julho de 2005', '135.826.490', '16807594', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 339, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Bruno Cardoso', 'Vinicius Cardoso ', 'Mariana Cardoso', 'Caruaru', 'Brasileira', '9 de dezembro de 2007', '824.637.281', '47610238', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 340, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Camila Castro', 'João Castro ', 'Renata Castro', 'Caruaru', 'Brasileira', '23 de junho de 2006', '976.158.934', '35926481', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 341, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Carolina Gonçalves', 'Ricardo Gonçalves ', 'Patrícia Gonçalves', 'Caruaru', 'Brasileira', '7 de novembro de 2005', '602.374.819', '59173824', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 342, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Eduardo Nunes', 'Carlos Nunes ', 'Vanessa Nunes', 'Caruaru', 'Brasileira', '31 de março de 2007', '247.890.563', '82415739', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 343, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Felipe Moreira', 'Paulo Moreira ', 'Cristina Moreira', 'Caruaru', 'Brasileira', '18 de setembro de 2006', '719.382.045', '73681942', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 344, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Fernanda Lima', 'Gustavo Lima ', 'Maria Rosa Lima ', 'Caruaru', 'Brasileira', '4 de fevereiro de 2005', '368.925.706', '94256187', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 345, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Gabriel Silva', 'Roberto Silva ', 'Carolina Silva ', 'Caruaru', 'Brasileira', '20 de agosto de 2007', '583.016.294', '21539876', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 346, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Gustavo Vieira', 'Marcos Vieira ', 'Adriana Vieira', 'Caruaru', 'Brasileira', '12 de janeiro de 2006', '690.431.578', '68324915', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 347, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Isabelly Victoria Ribeiro', 'Daniel Ribeiro ', 'Isabel Ribeiro ', 'Caruaru', 'Brasileira', '25 de maio de 2005', '813.257.649', '43769512', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 348, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Jéssica Oliveira', 'Ricardo Oliveira ', 'Cristina Oliveira ', 'Caruaru', 'Brasileira', '6 de outubro de 2007', '126.540.973', '57894326', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 349, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Juliana Costa', 'José Alberto Costa ', 'Viviane Costa ', 'Caruaru', 'Brasileira', '19 de abril de 2006', '435.607.189', '39615287', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 350, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Larissa Fernandes', 'Marcelo Fernandes ', 'Luciane Fernandes', 'Caruaru', 'Brasileira', '2 de agosto de 2005', '879.342.651', '14982763', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 351, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Letícia Ferreira', 'Thiago Ferreira ', 'SandraFerreira ', 'Caruaru', 'Brasileira', '13 de dezembro de 2007', '304.985.721', '26473819', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 352, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Lucas Rodrigues', 'Tiago Rodrigues ', 'Luciana Rodrigues', 'Caruaru', 'Brasileira', '26 de junho de 2006', '527.196.348', '91358642', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 353, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Luiza Oliveira', 'Rafael Oliveira ', 'Luana Oliveira ', 'Caruaru', 'Brasileira', '9 de novembro de 2005', '690.813.427', '63827915', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 354, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Marcelo Santos', 'Gustavo Santos ', 'Marisa Santos ', 'Caruaru', 'Brasileira', '22 de março de 2007', '217.954.680', '75296183', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 355, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Marina Pereira', 'Alexandre Pereira ', 'Ana Pereira', 'Caruaru', 'Brasileira', '5 de setembro de 2006', '854.239.106', '32168497', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 356, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Pedro Carvalho', 'Pedro Carvalho ', 'Rosário Carvalho', 'Caruaru', 'Brasileira', '19 de janeiro de 2005', '370.962.581', '48729631', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 357, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Rafaela Barbosa', 'Eduardo José Barbosa ', 'Flávia Barbosa ', 'Caruaru', 'Brasileira', '2 de julho de 2007', '549.803.217', '19347826', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 358, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Renata Costa', 'Miguel Costa ', 'Regina Costa ', 'Caruaru', 'Brasileira', '15 de novembro de 2006', '710.452.396', '84632971', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 359, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Ricardo Martins', 'Antonio Martins ', 'Débora Martins', 'Caruaru', 'Brasileira', '29 de abril de 2005', '136.895.704', '56287913', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 360, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Thiago Pereira', 'Guilherme Barbosa ', 'Gabriela Pereira', 'Caruaru', 'Brasileira', '10 de setembro de 2007', '983.217.540', '37542698', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 361, '3º TDS \"A\"'),
('Ministro Fernando Lyra', 'Tiago Almeida', 'Marcelo Pereira ', 'Carla Almeida', 'Caruaru', 'Brasileira', '24 de janeiro de 2006', '625.139.870', '69813257', 'PE', 'Desenvolvimento de sistemas', '2024-12-15 00:00:00', 362, '3º TDS \"A\"');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `login` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `login`, `senha`) VALUES
(1, 'Lucas', 'raposo'),
(2, 'Fabi', 'amorim'),
(3, 'Linaldo', 'pereira'),
(4, 'San', 'silva'),
(8, 'Iara', 'morais'),
(9, 'Lucie', 'belgica'),
(10, 'maria', 'senha'),
(11, 'Matheus', 'professor');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `bdalunos`
--
ALTER TABLE `bdalunos`
  ADD UNIQUE KEY `id` (`id`);

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `senha` (`senha`),
  ADD UNIQUE KEY `login` (`login`),
  ADD UNIQUE KEY `login_2` (`login`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `bdalunos`
--
ALTER TABLE `bdalunos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=363;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
