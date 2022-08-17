# catalog_tools
Work with PG catalog files

Project Gutenberg makes several catalog files available [on its website](https://www.gutenberg.org/cache/epub/feeds/). They are free for all to use.

All Project Gutenberg metadata are available digitally in the XML/RDF format. RDF files are updated daily. You may find code in the ["Gitenberg-dev" repo](https://github.com/gitenberg-dev/gitberg) useful for reading these.

[A CSV file](https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv) [zipped](https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv.gz) is compatible with Microsoft Excel. Note that titles with subtitles in the CSV file may span multiple lines. The process_csv.py script in this repo can be used to turn the titles onto single line titles. You can modify the script if you want to put subtitles into a separate column.

The MARC file available for download at PG should not be used, as it is 7 years old. A new MARC file generator is on the development roadmap.