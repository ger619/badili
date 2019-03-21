-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 21, 2019 at 02:14 PM
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
-- Database: `aftermath`
--
CREATE DATABASE IF NOT EXISTS `aftermath` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `aftermath`;

-- --------------------------------------------------------

--
-- Table structure for table `farm`
--

CREATE TABLE `farm` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `age_in_days` int(3) NOT NULL,
  `age_in_weeks` int(3) NOT NULL,
  `timestamp` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `farm`
--

INSERT INTO `farm` (`id`, `user_id`, `age_in_days`, `age_in_weeks`, `timestamp`) VALUES
(1, 1, 1, 1, '0000-00-00 00:00:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `feed`
--

CREATE TABLE `feed` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `age_in_weeks` int(3) NOT NULL,
  `type_of_feed` enum('Chick','Growers','Layer','') DEFAULT NULL,
  `intake_per_day` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `type_of_feed` varchar(64) NOT NULL,
  `intake_of_bird` varchar(64) NOT NULL,
  `age_in_day` varchar(64) NOT NULL,
  `age_in_weeks` varchar(64) NOT NULL,
  `vaccine` varchar(64) NOT NULL,
  `mode_of_vaccine` varchar(64) NOT NULL,
  `temperature` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `type_of_feed`, `intake_of_bird`, `age_in_day`, `age_in_weeks`, `vaccine`, `mode_of_vaccine`, `temperature`) VALUES
(1, 'chicken mash', '12-15', '1', '1', 'Mareks Newcastle+Infectitious Bronchitis', 'Subbcutaneos, Aerosol Spray', 0),
(2, 'chicken mash\r\n', '15-21', '14', '2', 'Gumboro - 1st Dose', 'Drinking Water', 0),
(3, 'chicken mash', '21-35', '21', '3', 'Newcastle 1st Dose', 'Eye drop or drinking water', 0),
(4, 'Chic Mash', '35-50', '24', '4', 'Gumboro -2nd Dose', 'Drinking water', 0),
(5, '75% Chic Mash and 25% Chic Mash', '35-50', '3w-6w', '5', 'Fowl Pox', 'Wing  Web Stabs (Only in hot areas)', 0),
(6, '75% Chic Mash and 25% Chic Growers', '35-50', '8w', '6', 'Newcastle -2nd Dose, Fowl typhoid', 'Eyedrops or drinking water, Instramuscular injection', 0),
(7, '50% Chic Mash and 50% Growers Mash', '55-60', '18w', '7', 'Newcastles (3rd dose at point of lay)', 'Eye drops or drinking water (Repeat every 3months)', 0),
(8, '50% Chic Mash and 50% Growers Mash', '55-60', '19w', '8', 'De-worming', 'Drinking Water (Repeat every 3months)', 0),
(9, '25% Chic Mash and 75% Growers Mash', '68-80', '', '9', '', '', 0),
(10, '100% Growers Mash', '68-80', '', '10-15', '', '', 0),
(16, '25% Layers Mash 75% Growers Mash', '68-80', '', '16', '', '', 0),
(17, '50% Layers Mash 50% Growers Mash', '68-80', '', '17', '', '', 0),
(28, '100% Growers Mash', '120 -140', '', '28', '', '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `temperature`
--

CREATE TABLE `temperature` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `age_in_weeks` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(32) NOT NULL,
  `password` varchar(256) DEFAULT NULL,
  `email` varchar(32) NOT NULL,
  `firstname` varchar(32) NOT NULL,
  `lastname` varchar(32) NOT NULL,
  `reg_time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`, `firstname`, `lastname`, `reg_time`) VALUES
(1, 'David', 'ger', 'ger@ger.com', '1', '1', '2019-03-20 09:05:38.753166');

-- --------------------------------------------------------

--
-- Table structure for table `vaccines`
--

CREATE TABLE `vaccines` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `age_in_days` int(3) NOT NULL,
  `mode_of_admin` varchar(11) NOT NULL,
  `comments` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `farm`
--
ALTER TABLE `farm`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `age_in_days` (`age_in_days`);

--
-- Indexes for table `feed`
--
ALTER TABLE `feed`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `temperature`
--
ALTER TABLE `temperature`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vaccines`
--
ALTER TABLE `vaccines`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `age_in_days` (`age_in_days`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `farm`
--
ALTER TABLE `farm`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `feed`
--
ALTER TABLE `feed`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `temperature`
--
ALTER TABLE `temperature`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `vaccines`
--
ALTER TABLE `vaccines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `feed`
--
ALTER TABLE `feed`
  ADD CONSTRAINT `feed_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `temperature`
--
ALTER TABLE `temperature`
  ADD CONSTRAINT `temperature_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `vaccines`
--
ALTER TABLE `vaccines`
  ADD CONSTRAINT `vaccines_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `vaccines_ibfk_2` FOREIGN KEY (`age_in_days`) REFERENCES `farm` (`age_in_days`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
