-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 10, 2021 at 12:20 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `digi`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `email` varchar(30) NOT NULL,
  `pwd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`email`, `pwd`) VALUES
('admin@gmail.com', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `fcnf`
--

CREATE TABLE `fcnf` (
  `id` int(11) NOT NULL,
  `fname` varchar(20) NOT NULL,
  `wname` varchar(20) NOT NULL,
  `crop` varchar(10) NOT NULL,
  `rate` int(3) NOT NULL,
  `quant` int(4) NOT NULL,
  `cost` int(10) NOT NULL,
  `status` int(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fcnf`
--

INSERT INTO `fcnf` (`id`, `fname`, `wname`, `crop`, `rate`, `quant`, `cost`, `status`) VALUES
(1, 'Agri', 'Chunu ', 'Wheat', 0, 0, 0, 1),
(2, 'Yash Gaurav', 'Munnu', '   ', 0, 0, 0, 0),
(3, 'Yash Gaurav', 'Ashish', '   ', 0, 0, 0, 0),
(6, 'Yash Gaurav', 'Ashish', '   ', 0, 0, 0, 0),
(7, 'Yash Gaurav', 'Ashish', 'Arhar Dal', 0, 0, 0, 0),
(8, 'Yash Gaurav', 'Ashish', '   ', 0, 0, 0, 0),
(9, 'Agri', 'Munnu', 'Rice', 0, 0, 0, 0),
(10, 'Agri', 'Chunu ', 'Moong Dal', 0, 20, 0, 0),
(11, 'Agri', 'Chunu ', 'Moong Dal', 0, 20, 0, 0),
(12, 'Agri', 'Chunu ', 'Moong Dal', 0, 20, 0, 0),
(13, 'Agri', 'Chunu ', 'Moong Dal', 0, 20, 0, 1),
(14, 'Agri', 'Chunu ', 'Moong Dal', 0, 20, 0, 0),
(15, 'Agri', 'Chunu ', 'Moong Dal', 0, 20, 0, 0),
(16, 'Agri', 'Munnu', 'None', 0, 26, 0, 1),
(17, 'Agri', 'Ashish', 'None', 0, 0, 0, 0),
(18, 'Agri', 'Ashish', 'None', 0, 0, 0, 0),
(19, 'Agri', 'Ashish', 'None', 0, 0, 0, 0),
(20, 'Yash Gaurav', 'Ashish', 'Arhar Dal', 0, 0, 0, 0),
(21, 'Yash Gaurav', 'Ashish', 'Arhar Dal', 0, 0, 0, 0),
(22, 'Yash Gaurav', 'Ashish', 'Arhar Dal', 0, 0, 0, 1),
(23, 'Yash Gaurav', 'Chunu ', '   ', 0, 0, 0, 2),
(24, 'Agri', 'Ashish', '   ', 0, 0, 0, 0),
(25, 'Yash Gaurav', 'Chunu ', '   ', 0, 0, 0, 0),
(26, 'Yash Gaurav', 'Chunu ', 'Moong Dal', 0, 20, 0, 0),
(27, 'hyuu', 'Chunu ', 'Moong Dal', 0, 20, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `fpic`
--

CREATE TABLE `fpic` (
  `fid` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `fpath` varchar(255) NOT NULL,
  `status` enum('1','0') NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fpic`
--

INSERT INTO `fpic` (`fid`, `fname`, `fpath`, `status`) VALUES
(1, '0.3331995866970643download1.jpg', 'uploaded_files/0.3331995866970643download1.jpg', '0'),
(2, '0.6950197233993901trukey.jpg', 'uploaded_files/0.6950197233993901trukey.jpg', '0'),
(3, '0.9123343009898902download1.jpg', 'uploaded_files/0.9123343009898902download1.jpg', '0'),
(4, '0.2686676404344237waterfall.jpg', 'uploaded_files/0.2686676404344237waterfall.jpg', '0'),
(7, '0.624304610762tree.jpg', 'uploaded_files/0.624304610762tree.jpg', '0'),
(8, '0.2932047609770.6950197233993901trukey.jpg', 'uploaded_files/0.2932047609770.6950197233993901trukey.jpg', '0');

-- --------------------------------------------------------

--
-- Table structure for table `freg`
--

CREATE TABLE `freg` (
  `id` int(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `contact` bigint(10) NOT NULL,
  `crop1` varchar(20) NOT NULL,
  `crop2` varchar(20) NOT NULL,
  `crop3` varchar(20) NOT NULL,
  `crop4` varchar(20) NOT NULL,
  `crop5` varchar(20) NOT NULL,
  `pwd` varchar(20) NOT NULL,
  `image` varchar(1000) NOT NULL,
  `location` varchar(255) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `freg`
--

INSERT INTO `freg` (`id`, `name`, `contact`, `crop1`, `crop2`, `crop3`, `crop4`, `crop5`, `pwd`, `image`, `location`, `address`) VALUES
(1, 'Yash Gaurav', 9430058611, 'Wheat', '', 'Moong Dal', '', 'Oats', '123456', '', '', ''),
(2, 'Agri', 8540082522, '', 'Rice', 'Moong Dal', 'Arhar Dal', '', '123456', '', '', ''),
(3, 'Raju Babu', 321654987, '', '', 'Moong Dal', 'Aarhar Dal', 'Oats', '123456', '', 'https://www.google.co.in/maps/place/Bokaro+Steel+City,+Jharkhand/@23.6676092,86.0490813,12z/data=!3m1!4b1!4m5!3m4!1s0x39f4230341010871:0xf89f21d9001d5036!8m2!3d23.6692956!4d86.151112', 'Bokaro, Ranchi'),
(4, 'hyuu', 562, 'Wheat', '', 'Moong Dal', '', '', '1235456', '', 'cdv', 'vsdv'),
(5, 'gv', 4254, '', 'Rice', '', '', '', 'kghm', '', 'gmgy', 'mygh');

-- --------------------------------------------------------

--
-- Table structure for table `rate`
--

CREATE TABLE `rate` (
  `wheat` int(5) NOT NULL,
  `rice` int(5) NOT NULL,
  `moong` int(5) NOT NULL,
  `arhar` int(5) NOT NULL,
  `oats` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rate`
--

INSERT INTO `rate` (`wheat`, `rice`, `moong`, `arhar`, `oats`) VALUES
(45, 42, 100, 56, 124);

-- --------------------------------------------------------

--
-- Table structure for table `wpic`
--

CREATE TABLE `wpic` (
  `fid` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `fpath` varchar(255) NOT NULL,
  `status` enum('1','0') NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wpic`
--

INSERT INTO `wpic` (`fid`, `fname`, `fpath`, `status`) VALUES
(1, '0.3331995866970643download1.jpg', 'uploaded_files/0.3331995866970643download1.jpg', '0'),
(3, '0.6950197233993901trukey.jpg', 'uploaded_files/0.6950197233993901trukey.jpg', '0'),
(5, '0.9123343009898902download1.jpg', 'uploaded_files/0.9123343009898902download1.jpg', '0'),
(6, '0.2686676404344237waterfall.jpg', 'uploaded_files/0.2686676404344237waterfall.jpg', '0');

-- --------------------------------------------------------

--
-- Table structure for table `wreg`
--

CREATE TABLE `wreg` (
  `id` int(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `contact` bigint(10) NOT NULL,
  `crop1` varchar(20) NOT NULL,
  `crop2` varchar(20) NOT NULL,
  `crop3` varchar(20) NOT NULL,
  `crop4` varchar(20) NOT NULL,
  `crop5` varchar(20) NOT NULL,
  `pwd` varchar(20) NOT NULL,
  `image` varchar(1000) NOT NULL,
  `location` varchar(255) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wreg`
--

INSERT INTO `wreg` (`id`, `name`, `contact`, `crop1`, `crop2`, `crop3`, `crop4`, `crop5`, `pwd`, `image`, `location`, `address`) VALUES
(1, 'Ashish', 8709569656, 'Wheat', '', '', 'Arhar Dal', 'Oats', '123456', '', '', ''),
(2, 'Chunu ', 9876543210, 'Wheat', 'Rice', 'Moong Dal', '', 'Oats', '123456', '', '', ''),
(3, 'Munnu', 123456789, '', 'Rice', 'Moong Dal', '', 'Oats', '123456', '', '', ''),
(4, 'Knnu', 9874563210, 'Wheat', 'Rice', 'Moong Dal', '', '', '123456', '', 'https://www.google.co.in/maps/place/Gaya,+Bihar/@28.553907,77.0909803,15z/data=!4m5!3m4!1s0x39f32a440a1b3c1f:0xcef6b223bdbf34a6!8m2!3d24.7913957!4d85.0002336', 'Gaya, Bihar');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `fcnf`
--
ALTER TABLE `fcnf`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `fpic`
--
ALTER TABLE `fpic`
  ADD PRIMARY KEY (`fid`);

--
-- Indexes for table `freg`
--
ALTER TABLE `freg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wpic`
--
ALTER TABLE `wpic`
  ADD PRIMARY KEY (`fid`);

--
-- Indexes for table `wreg`
--
ALTER TABLE `wreg`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `fcnf`
--
ALTER TABLE `fcnf`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `fpic`
--
ALTER TABLE `fpic`
  MODIFY `fid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `freg`
--
ALTER TABLE `freg`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `wpic`
--
ALTER TABLE `wpic`
  MODIFY `fid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `wreg`
--
ALTER TABLE `wreg`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
