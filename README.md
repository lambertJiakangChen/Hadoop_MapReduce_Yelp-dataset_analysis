## Objectives

This project involves performing distributed analytics on a large-scale dataset using Python on a Hadoop cluster. The dataset is a subset of Yelp's businesses, reviews, and user data. The dataset consists of five JSON files, which contain information about businesses across 8 metropolitan areas in the USA and Canada.
The dataset can be found and downloaded [here](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3) (registration to Kaggle is required).

There are four MapReduce algorithms in this project. The first set of scripts constructs an inverted index of the business categories; the second set computes frequency distributions about users; the third set finds top-K records; the fourth set analyzes the relationships between check-ins and businesses.

## Awareness
* You may clone this repository to your local directory. 
* Make sure your version Python >= 3.7.0.
* Change to CRLF line terminators for Windows.
* You need Docker installed on your local machine to run this project in the Docker-based Hadoop environment.
* The scripts are executed in a Hadoop cluster (Apache Hadoop 3.3.1).
* original file provided by [Kaggle](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3) with command as follow to copy to HDFS
```
hdfs dfs -put ./inputfilename /
```
* Copy back to local file system with command as follow
```
hdfs dfs -get /output/filename
```
## q1mapper & q1Reducer (Distributed Construction of the Inverted Index)
Original file provided by Kaggle ([*yelp_academic_dataset_business.json*](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3?select=yelp_academic_dataset_business.json))
Given a collection of businesses, an inverted index is a dictionary where each category is associated with a list of the business ids (comma-separated) that belong to that category. See the example below:

![Inverted index](Q1.png)

the algorithm computes the inverted index of the categories to businesses that are **open on the weekend** (Saturdays, Sundays, or both). The output of the MapReduce job consists of a number of lines as follows:
```
category	[id1, id2, id3, id4]
```

Ran the script as follows:
```
$ yarn jar /path-to-jar/hadoop-streaming-3.3.1.jar -files q1mapper.py,q1reducer.py -mapper /path-to-mapper/q1mapper.py -reducer /path-to-reducer/q1reducer.py -input /path-to-json-in-hdfs/yelp_academic_dataset_business.json -output /path-to-directory-in-hdfs/output
```
For example:
```
$ yarn jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -files q1mapper.py,q1reducer.py -mapper ./q1mapper.py -reducer ./q1reducer.py -input /yelp_academic_dataset_business.json -output /output
```

## q2mapper & q2reducer (Distributed Computation of Frequencies)
original file provided by Kaggle ([*yelp_academic_dataset_user.json*](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3?select=yelp_academic_dataset_user.json)), the algorithm computes the percent proportion of Yelp accounts created in each month (irrespective of the year). The output of the MapReduce job is formatted as follows:
```
month(integer)	proportion%
```

Run the script as follows:
```
$ yarn jar /path-to-jar/hadoop-streaming-3.3.1.jar -files q2mapper.py,q2reducer.py -mapper /path-to-mapper/q2mapper.py -reducer /path-to-reducer/q2reducer.py -input /path-to-json-in-hdfs/yelp_academic_dataset_user.json -output /path-to-directory-in-hdfs/output
```
For example:
```
$ yarn jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -files q2mapper.py,q2reducer.py -mapper ./q2mapper.py -reducer ./q2reducer.py -input /yelp_academic_dataset_user.json -output /output
```


## q3mapper & q3reducer (Distributed Computation of the Top-k Reviews)
Original file provided by Kaggle ([*yelp_academic_dataset_review.json*](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3?select=yelp_academic_dataset_review.json)). Yelp users can vote a review as useful, funny, or cool (UFC). The total number of UFC votes of a review is the sum of useful, funny, and cool votes it has received. The output of the MapReduce job is in descending order according to the date created as follows:
```
review_id	#UFC_votes
```
Run the script as follows:
```
$ yarn jar /path-to-jar/hadoop-streaming-3.3.1.jar -files q3mapper.py,q3reducer.py -mapper /path-to-mapper/q3mapper.py -reducer /path-to-reducer/q3reducer.py -input /path-to-json-in-hdfs/yelp_academic_dataset_review.json -output /path-to-directory-in-hdfs/output
```
For example:
```
$ yarn jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -files q3mapper.py,q3reducer.py -mapper ./q3mapper.py -reducer ./q3reducer.py -input /yelp_academic_dataset_review.json -output /output
```


## Q4. Distributed Generation of Checkin Logs (25%)
Original files provided by Kaggle ([*yelp_academic_dataset_checkin.json*](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3?select=yelp_academic_dataset_checkin.json) and [*yelp_academic_dataset_business.json*](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3?select=yelp_academic_dataset_business.json)).
MapReduce algorithm generates check-in logs in a distributed manner. Each line of the check-in logs contains a unique identifier (UID), the timestamp of the check-in, and the name of the business. The UID is a **random-generated unique string with 22 characters** including uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), underscore (_), and dash (-). The output of the MapReduce job is formatted as follows:

```
uid	timestamp	business_name
```
Run the script as follows:
```
$ yarn jar /path-to-jar/hadoop-streaming-3.3.1.jar -files q4mapper.py,q4reducer.py -mapper /path-to-mapper/q4mapper.py -reducer /path-to-reducer/q4reducer.py -input /path-to-json-in-hdfs/yelp_academic_dataset_business.json -input /path-to-json-in-hdfs/yelp_academic_dataset_checkin.json -output /path-to-directory-in-hdfs/output
```
For example:
```
$ yarn jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -files q4mapper.py,q4reducer.py -mapper ./q4mapper.py -reducer ./q4reducer.py -input /yelp_academic_dataset_business.json -input /yelp_academic_dataset_checkin.json -output /output
```
