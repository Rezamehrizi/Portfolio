---
title: "Detection of Change Points in Piecewise Polynomial Signals Using Trend Filtering"
authors:
- admin
- Shojaeddin Chenouri
date: "2021-05-01"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2021-06-01"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: "arXiv e-prints"
publication_short: ""

abstract: While many approaches have been proposed for discovering abrupt changes in piecewise constant signals, few methods are available to capture these changes in piecewise polynomial signals. In this paper, we propose a change point detection method, PRUTF, based on trend filtering. By providing a comprehensive dual solution path for trend filtering, PRUTF allows us to discover change points of the underlying signal for either a given value of the regularization parameter or a specific number of steps of the algorithm. We demonstrate that the dual solution path constitutes a Gaussian bridge process that enables us to derive an exact and efficient stopping rule for terminating the search algorithm. We also prove that the estimates produced by this algorithm are asymptotically consistent in pattern recovery. This result holds even in the case of staircases (consecutive change points of the same sign) in the signal. Finally, we investigate the performance of our proposed method for various signals and then compare its performance against some state-of-the-art methods in the context of change point detection. We apply our method to three real-world datasets including the UK House Price Index (HPI), the GISS surface Temperature Analysis (GISTEMP) and the Coronavirus disease (COVID-19) pandemic.

# Summary. An optional shortened abstract.
summary: This paper introduces PRUTF, a method using trend filtering for change point detection in piecewise polynomial signals. PRUTF offers a dual solution path for efficient stopping rules and consistent pattern recovery, even in the presence of consecutive change points. Its effectiveness is demonstrated across various signals and compared with state-of-the-art methods using real-world datasets.

tags:
- Source Themes
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://arxiv.org/pdf/2009.08573.pdf
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: ''
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---

