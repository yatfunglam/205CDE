-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 10, 2019 at 02:59 PM
-- Server version: 5.7.25-0ubuntu0.18.04.2
-- PHP Version: 7.2.15-0ubuntu0.18.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `L`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `AID` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`, `AID`) VALUES
('admin1', 'password', 1);

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `scid` int(10) NOT NULL,
  `cid` int(10) NOT NULL,
  `pid` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`scid`, `cid`, `pid`) VALUES
(1, 1, 4),
(2, 1, 5),
(3, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `cid` int(10) NOT NULL,
  `cname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telno` int(8) NOT NULL,
  `address` varchar(255) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`cid`, `cname`, `email`, `telno`, `address`, `username`, `password`) VALUES
(1, 'Chan Tai Ming', 'chantaiming@hotmail.com', 66668888, 'xxx road ,hk', 'chantaiman', '123456'),
(2, 'Chan Xiao Ming', 'chanxiaoming@hotmail.com', 98886666, 'ooo road ,hk', 'cxm', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `oid` int(10) NOT NULL,
  `cid` int(10) NOT NULL,
  `pid` int(10) NOT NULL,
  `datetime` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`oid`, `cid`, `pid`, `datetime`) VALUES
(1, 2, 5, '10-04-2019 13:56:01'),
(1, 2, 4, '10-04-2019 13:56:01');

-- --------------------------------------------------------

--
-- Table structure for table `product_book`
--

CREATE TABLE `product_book` (
  `pid` int(10) NOT NULL,
  `bkname` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `publishYear` int(4) NOT NULL,
  `publisher` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `Cat` set('Chinese','English') NOT NULL,
  `subcat` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_book`
--

INSERT INTO `product_book` (`pid`, `bkname`, `author`, `publishYear`, `publisher`, `price`, `Cat`, `subcat`) VALUES
(1, 'Les Miserable', 'Victor Hugo', 2013, 'Signet Book', 98, 'English', 'Literature'),
(2, 'Notre-Dame de Paris', 'Victor Hugo', 2015, 'Penguin Books Ltd', 97.8, 'English', 'Literature'),
(3, 'NieR:Automata: Long Story Short', 'Yoko Taro', 2018, 'Viz Media, Subs. of Shogakukan Inc', 78.5, 'English', 'Science Fiction '),
(4, 'Flying Fox of Snowy Mountains Vol. 1', 'Jin Yong', 1956, 'Ming Ho Publication', 52, 'Chinese', 'Martial arts'),
(5, 'Flying Fox of Snowy Mountains Vol. 2', 'Jin Yong', 1956, 'Ming Ho Publication', 52, 'Chinese', 'Martial arts'),
(6, 'A Deadly Secret', 'Jin Yong', 1956, 'Ming Ho Publication', 52, 'Chinese', 'Martial arts');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`AID`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `AID` (`AID`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`scid`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cid`),
  ADD UNIQUE KEY `cid` (`cid`),
  ADD UNIQUE KEY `email` (`email`,`telno`,`username`);

--
-- Indexes for table `product_book`
--
ALTER TABLE `product_book`
  ADD PRIMARY KEY (`pid`),
  ADD UNIQUE KEY `pid` (`pid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `AID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `scid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `cid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `product_book`
--
ALTER TABLE `product_book`
  MODIFY `pid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
