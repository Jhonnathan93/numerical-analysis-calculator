# Numerical Analysis Calculator

Django web application for computing and visualizing numerical methods for nonlinear equations, systems of equations, and interpolation.

## Table of contents

- [About](#about)
- [Features](#features)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Commands](#commands)
- [Architecture](#architecture)
- [Testing and quality](#testing-and-quality)
- [Build and deployment](#build-and-deployment)
- [CI/CD](#cicd)
- [Contributing](#contributing)
- [Branches](#branches)
- [FAQ](#faq)
- [Resources](#resources)
- [Gallery](#gallery)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## About

Numerical Analysis Calculator helps students and numerical-analysis learners solve problems through a web interface. It implements iterative methods for approximating roots and solving systems of equations, as well as interpolation techniques. Each calculation presents a result and an iteration table; several methods also generate a supporting plot.

The project is designed to run locally as a Django application. It does not currently include a public API, deployment workflow, or configuration for external services.

## Features

- Nonlinear-equation methods: Bisection, Fixed Point, False Position, Newton-Raphson, Secant, and Multiple Roots (v1 and v2).
- Systems-of-equations methods: Jacobi, Gauss-Seidel, and Successive Over-Relaxation (SOR).
- Interpolation methods: Vandermonde, Newton Divided Differences, Lagrange, and Linear, Quadratic, and Cubic Splines.
- Iteration tables, error handling, and plots to support result interpretation.

## Usage

1. Start the local server.
2. Open `http://127.0.0.1:8000/` in a browser.
3. Select a method, fill in its parameters, and submit the form.

For example, in the Bisection method enter a function, an interval `[a, b]`, an iteration limit, and a tolerance. The application returns an approximate root, an iteration table, and a plot when applicable.

```text
f(x), method parameters, and tolerance -> numerical approximation and iteration table
```

## Prerequisites

- Python 3.12. Later Python versions have not been tested.
- `pip`.
- A modern web browser.

Dependencies are pinned in [requirements.txt](requirements.txt), including Django 5.1.

## Installation

Clone the repository:

```bash
git clone https://github.com/Jhonnathan93/numerical-analysis-calculator.git
cd numerical-analysis-calculator
```

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**macOS and Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

The project does not require environment variables or `.env` files to run locally. Django uses the configuration in `calculator/settings.py` and Django's default SQLite database. For production, configure these environment variables in the hosting platform:

| Variable | Purpose | Required in production |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Django secret key. | Yes |
| `DJANGO_DEBUG` | Enables debug mode when set to `true`; defaults to `false` on Vercel. | No |

Do not commit virtual environments, the generated local database (`db.sqlite3`), cache files, or production secrets. Before deployment, configure `DJANGO_SECRET_KEY` and manage secrets outside the repository. `ALLOWED_HOSTS` already includes Vercel domains.

## Commands

| Goal | Command |
| --- | --- |
| Start the local server | `python manage.py runserver` |
| Run tests | `python manage.py test` |
| Create migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Validate Django configuration | `python manage.py check` |

## Architecture

```text
calculator/          Django configuration, root URLs, and shared templates
home/                Views and informational pages
methods/
  methods/           Numerical algorithm implementations
  utils/             Equation, matrix, plot, and response utilities
  views/             Views connecting forms, algorithms, and templates
  templates/         Interfaces for each method
```

| Component | Responsibility |
| --- | --- |
| `methods/methods` | Executes numerical-analysis algorithms. |
| `methods/utils` | Parses equations, processes matrices, generates plots, and standardizes responses. |
| `methods/views` | Receives form input, invokes methods, and renders results. |
| `methods/templates` | Presents forms, tables, and results to users. |

## Testing and quality

Run the tests registered with Django:

```bash
python manage.py test
```

The repository does not define linting, formatting, type-checking, or coverage-threshold tools. Use `python manage.py check` as a basic configuration check before submitting changes.

## Build and deployment

Django does not need a build phase for local development. To prepare a production instance, install the dependencies, apply migrations, and configure a WSGI or ASGI server using `calculator.wsgi` or `calculator.asgi`.

```bash
python manage.py migrate
python manage.py collectstatic
```

Configure `DEBUG = False`, `ALLOWED_HOSTS`, static files, and the appropriate secret variables before exposing the application. The repository does not include deployment configuration or a specific health check.

## CI/CD

There are no continuous-integration or continuous-delivery workflows versioned in this repository. If one is added, it should run at least `python manage.py check` and `python manage.py test` for every change.

## Contributing

Contributions are welcome.

1. Create a branch focused on one change.
2. Implement the change and add or update tests when appropriate.
3. Run `python manage.py check` and `python manage.py test`.
4. Open a pull request with a clear description of the changed behavior.

## Branches

The current primary branch is `main`. No branch policy or merge strategy is documented in the repository; agree on the branch name and integration strategy with maintainers before making large changes.

## FAQ

### Where can I access the methods?

From the home page or under the `/methods/` route after starting the server.

### What happens if the data is invalid?

The application displays an error response generated during validation or calculation. Check that the function, intervals, tolerance, and iteration limit are valid for the selected method.

## Resources

- [Project repository](https://github.com/Jhonnathan93/numerical-analysis-calculator)
- [Django documentation](https://docs.djangoproject.com/)

## Gallery

The repository does not currently maintain screenshots or demonstrations.

## Acknowledgments

Thanks to the Django community and the numerical-analysis academic resources that provide references for these methods.

## License

The repository does not include a license file. Therefore, no reuse permissions are explicitly granted.
