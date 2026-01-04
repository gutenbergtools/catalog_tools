# catalog_tools
Work with PG catalog files

Project Gutenberg makes several catalog files available [on its website](https://www.gutenberg.org/cache/epub/feeds/). They are free for all to use.

All Project Gutenberg metadata are available digitally in the MARC, MARCXML, and XML/RDF format. The MARC record extract is generated weekly from the Project Gutenberg Postgres database. This process uses a python script which recreates each MARC record from the entire collection of titles, excluding non-textual titles such as maps, audio files, data sets and so on.  Further info is on the MARC extract is available at (https://github.com/gutenbergtools/ebookconverter/blob/v10/MARC.md). RDF files are updated daily. You may find code in the ["Gitenberg-dev" repo](https://github.com/gitenberg-dev/gitberg) useful for reading these.

[A CSV file](https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv) [zipped](https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv.gz) is compatible with Microsoft Excel. Note that titles with subtitles in the CSV file may span multiple lines. The process_csv.py script in this repo can be used to turn the titles onto single line titles. You can modify the script if you want to put subtitles into a separate column.
