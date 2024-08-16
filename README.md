# Vietnam High School Graduation Examination Data Science

## Motivation
With the recent release of the 2024 high school graduation exam results, I decided to analyze the data to see if I could find any interesting insights. The data contains the results of all students who took the exam in 2024. The data includes the student's name, scores in subjects from mandatory (Math, Literature, Foreign Language) to optional (Physics, Chemistry, Biology, History, Geography, Civic Education). From the data, I will try to answer the following questions:
1. How to improve English scores for students in Vietnam?
2. Does economic wealth of a province entail better English performance?
3. Are students more interested in Social Science or Natural Science? Why?
4. Which subject combinations are the easiest to score for students?

## Data

1. Download data from [here](https://github.com/anhdung98/diem_thi_2024/releases/download/240717/diem_thi_thpt_2024.csv) and put it in the data folder as `data/diem_thi_thpt_2024.csv`.
2. Download GEOJSON data of Vietnam map from [here](https://github.com/ThongVM003/Datascrap/blob/master/diaphantinhenglish.geojson) and put it in the data folder as `data/vietnam.geojson`.


First, run the pip install command to install the necessary libraries.

```bash
pip install -r requirements.txt
```

Then, run the following command to start the Jupyter Notebook.

```bash
jupyter notebook
```

Then just run the notebook.

## Files in the Repository
- `data/diem_thi_thpt_2024.csv`: The data of the 2024 high school graduation exam results.
- `data/vietnam.geojson`: The GEOJSON data of Vietnam map.
- `notebook.ipynb`: The Jupyter Notebook containing the analysis.
- `requirements.txt`: The file containing the necessary libraries to run the notebook.
- `README.md`: The README file.
- `src/`: The folder containing the source code for the analysis.
    - `config.py`: The configuration file.
    - `data_ingestion.py`: The file containing the functions to load and clean the data.
    - `visualize.py`: The file containing the functions to visualize the data.
    - `model.py`: The file containing the functions to train the model.

## Summaries of the Analysis
1. The English scores of students in Vietnam vary drastically among provinces. The poor provinces do not get the newest and modern teaching methods, which leads to the low English scores, while big metropolitan areas are exceptional in their reward policy and presence of English centers. The government should invest more in education in these provinces to improve the English scores.

2. The economic wealth of a province does entail better English performance, in a logarithmic relationship. The provinces with higher GDP per capita tend to have higher English scores, but flattens out at higher GRDP.

3. Students are more interested in Social Science than Natural Science. The reason is that the Social Science subjects are easier to score than Natural Science subjects. The Social Science subjects have a higher average score than the Natural Science subjects.

4. The easiest subject combinations to score for students are Literature, History, and Civic Education. These subjects have the highest average scores among all subjects. This is also because of the preference of students for Social Science subjects.

## Blog

The full blog can be found [here](https://medium.com/@dinhngocan102003/vietnamese-high-school-exam-reveals-dark-truth-about-its-education-system-0b9f751e443f)