-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 14, 2019 at 07:56 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projectbadili`
--
CREATE DATABASE IF NOT EXISTS `projectbadili` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `projectbadili`;

-- --------------------------------------------------------

--
-- Table structure for table `chicken`
--

CREATE TABLE `chicken` (
  `id` int(11) NOT NULL,
  `name_of_farmer` varchar(256) NOT NULL,
  `age_in_day` varchar(64) NOT NULL,
  `no_of_weeks` varchar(64) NOT NULL,
  `type_of_feed` varchar(256) NOT NULL,
  `type_of_vaccines` varchar(32) NOT NULL,
  `comments` varchar(1024) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chicken`
--

INSERT INTO `chicken` (`id`, `name_of_farmer`, `age_in_day`, `no_of_weeks`, `type_of_feed`, `type_of_vaccines`, `comments`) VALUES
(1, '1', '1', '1', '1', '1', '1');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL,
  `email` varchar(256) NOT NULL,
  `firstname` varchar(64) NOT NULL,
  `lastname` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`, `firstname`, `lastname`) VALUES
(1, '1', '1', '1@1.com', '1', '1'),
(5, 'dd', 'dd', 'd@d.com', 'd', 'dd'),
(7, 'dd2', '33', 'd@d.com', 'd', 'dd'),
(9, '12', '12', '12', '12', ''),
(11, '56', '1', '12', '1', '1'),
(12, '22', '22', '22@22.co', 'Da', 'ge'),
(13, 'David', 'ger', 'ger@ger.com', 'David', 'Ger');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `chicken`
--
ALTER TABLE `chicken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name_of_farmer` (`name_of_farmer`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `chicken`
--
ALTER TABLE `chicken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `chicken`
--
ALTER TABLE `chicken`
  ADD CONSTRAINT `chicken_ibfk_1` FOREIGN KEY (`name_of_farmer`) REFERENCES `users` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
