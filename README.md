# Badgeyay

![Badgeyay](/frontend/public/images/Badgeyay-artwork.png)

[![Gitter](https://img.shields.io/badge/chat-on%20gitter-ff006f.svg?style=flat-square)](https://gitter.im/fossasia/badgeyay)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1ac554483fac462797ffa5a8b9adf2fa?style=flat-square)](https://www.codacy.com/app/fossasia/badgeyay)
[![Build Status](https://api.travis-ci.org/fossasia/badgeyay.svg?branch=development&style=flat-square)](https://travis-ci.org/fossasia/badgeyay)
[![Mailing](https://img.shields.io/badge/Mailing-List-red.svg)](https://groups.google.com/forum/#!forum/open-event)

> **Badgeyay provides an interface to event organizers for generating badges of events from concerts to conferences and meet-ups.**

Badgeyay is a badge generator with a simple web UI to add data and generate printable badges in a PDF.

The user can:

- Choose the size of the badges
- Choose the background of the badges and upload the logo and the background image
- Upload a CSV file or manually enter CSV data such as name, attendee type, designation, nickname/handle, and organization or project

---

## Demo

![Badgeyay Demo](/docs/backend/installation/demo.gif)

---

## Getting Started

Badgeyay consists of a frontend and a backend service.

### Prerequisites
- Git
- Python (for backend)
- Node.js and npm (for frontend)

### Installation

Follow the detailed installation guides below:

- [Frontend Installation Guide](/docs/frontend/installation/README.md)
- [Backend Installation Guide](/docs/backend/installation/README.md)

---

## Communication

- Join our **[mailing list](https://groups.google.com/forum/#!forum/open-event)** to discuss questions regarding the project  
  > https://groups.google.com/forum/#!forum/open-event

- Our chat channel is on **[Gitter](https://gitter.im/fossasia/badgeyay)**  
  > https://gitter.im/fossasia/badgeyay

---

## Installation

Badgeyay's frontend and backend can be deployed easily. Detailed installation instructions are provided below:

1. [Badgeyay Frontend](/docs/frontend/installation/README.md)
2. [Badgeyay Backend](/docs/backend/installation/README.md)
3. **Installing git pre-push hook:**
   - Run `scripts/install-hook.py`. It will copy contents of `scripts/pre-push-hook.py` to `.git/hooks/pre-push`.
   - Ensure `.git/hooks/pre-push.sample` exists before performing this step.
   - This hook runs linting checks before pushing commits.

---

## Technology Stack

- Backend Web Framework: [Flask](http://flask.pocoo.org/)
- Frontend Web Framework: [Ember.js](https://emberjs.com/)

---

## Branch Policy

- **development**  
  All development happens here. Pull requests should be made against this branch and must pass all checks.

- **master**  
  Contains stable, released code.

---

## Contributing

We welcome contributions from everyone.  
Please read our [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

---

## Code of Conduct

This project follows a [Code of Conduct](CODE_OF_CONDUCT.md).  
By participating, you are expected to uphold it.

---

## License

This project is licensed under the **[GNU General Public License v3](/LICENSE)**.

> To obtain the software under a different license, please contact [FOSSASIA](http://blog.fossasia.org/contact/).
