-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 12, 2016 at 10:06 PM
-- Server version: 5.5.52-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `hrc`
--

-- --------------------------------------------------------

--
-- Table structure for table `event`
--

CREATE TABLE IF NOT EXISTS `event` (
  `EID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Event ID',
  `type` varchar(20) NOT NULL,
  `attendance` int(11) NOT NULL,
  `finance` float NOT NULL,
  `response_rate` float NOT NULL COMMENT 'Survey Response Rate',
  PRIMARY KEY (`EID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=33 ;

-- --------------------------------------------------------

--
-- Table structure for table `survey`
--

CREATE TABLE IF NOT EXISTS `survey` (
  `SID` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `location` varchar(50) NOT NULL,
  `eventype` varchar(50) NOT NULL,
  `title` varchar(35) NOT NULL,
  `date` varchar(30) NOT NULL,
  `residency` varchar(50) NOT NULL,
  `race` varchar(50) NOT NULL,
  `sex` varchar(20) NOT NULL,
  `age` varchar(10) NOT NULL,
  `govt` varchar(30) NOT NULL COMMENT 'Government Official',
  `q1` varchar(20) NOT NULL COMMENT 'I found this program topic to be timely, stimulating  and engaging',
  `q2` varchar(20) NOT NULL COMMENT 'The organization of the event was user friendly?',
  `q3` varchar(20) NOT NULL COMMENT 'I found the speaker(s)/panel/film to be  knowledgeable and relevant',
  `q4` varchar(20) NOT NULL COMMENT 'I was able to ask questions, receive answers and  comment',
  `q5` varchar(20) NOT NULL COMMENT 'The speaker/presenter/panel was effective',
  `q6` varchar(20) NOT NULL COMMENT 'The handout materials were useful',
  `q7` varchar(20) NOT NULL COMMENT 'There was opportunity for questions?',
  `q8` varchar(20) NOT NULL COMMENT 'The overall program was what I expected',
  `q9` varchar(20) NOT NULL COMMENT 'The information was relevant?',
  `q10` varchar(500) NOT NULL COMMENT 'What were the strengths of the workshop?',
  `q11` varchar(500) NOT NULL COMMENT 'What were the weaknesses of the workshop?21',
  `q12` varchar(20) NOT NULL COMMENT 'The accommodations(location, seating, sound,  lighting, room) were adequate',
  `q13` varchar(20) NOT NULL COMMENT 'The refreshments were adequate',
  `q14` varchar(20) NOT NULL COMMENT 'The event coordinators were pleasant and helpful',
  `q15` varchar(20) NOT NULL COMMENT 'The event began and ended on time',
  `q16` varchar(20) NOT NULL COMMENT 'Would you recommend this event to others? 0 means no, 1 means yes.',
  `q17` varchar(500) NOT NULL COMMENT 'Additional Comments',
  PRIMARY KEY (`SID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=30 ;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `UID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'User ID',
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
