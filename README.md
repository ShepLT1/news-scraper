# news-scraper

Python-based Hacker News scraper utilizing Beautiful Soup. Filters by number of pages and scores > 99.

## Usage

Clone the repository, open the news-scraper directory in your command line, & run the following command:

```console
python scraper.py <numberOfPages>
```

## Expected Response

```python
[
  {
    'link': 'https://www.phoronix.com/news/Wayland-Fractional-Scale-Ready',
    'title': 'Wayland Protocol Finally Ready for Fractional Scaling',
    'votes': 113
  },
  {
    'link': 'https://dl.acm.org/doi/10.1145/3548606.3560643',
    'title': 'Spreading deadly pathogens under the disguise of popular music',
    'votes': 107
  },
  {
    'link': 'https://mdubakov.medium.com/google-please-do-something-with-your-ads-and-seo-spam-99a6b039354c',
    'title': 'Google, please do something with your ads and SEO-spam',
    'votes': 105
  },
  ...
]
```
