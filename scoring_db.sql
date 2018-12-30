CREATE DATABASE scoring;
USE scoring;
CREATE TABLE scoring_db
(
  file VARCHAR(150) NOT NULL,
  score INT signed NOT NULL,
  retrieval DATE NOT NULL
);
-- Retrieve All Scores
SELECT * FROM scoring_db;

-- Retrieve All Scores from Custom Date Range
SELECT * FROM scoring_db WHERE retrieval BETWEEN "2018-10-29" AND "2018-11-26";

-- Retrieve Highest Score For a Given File
SELECT file, MAX(score) score FROM scoring_db GROUP BY file ORDER BY score DESC;

-- Retrieve Lowest Score for a Given File
SELECT file, MIN(score) score FROM scoring_db GROUP BY file ORDER BY score ASC;

-- Retrieve Average Score for a Given File
SELECT file, AVG(score) score FROM scoring_db GROUP BY file ORDER BY score DESC;
