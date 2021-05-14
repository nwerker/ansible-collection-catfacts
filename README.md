# Ansible Collection - nwerker.catfacts

[![Code of conduct](https://img.shields.io/badge/code%20of%20conduct-Ansible-silver.svg)](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)
[![License](https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg)](LICENSE)

This ansible collection provides modules and roles for retrieving random cat facts via public available APIs. This obviously doesn't serve a meaningfull purpose other than for demonstration purposes, or you are just very interested in cat facts.

Following API Sources are supported. Big thanks to GitHub User [alexwohlbruck](https://github.com/alexwohlbruck) for contributing [cat-facts](https://github.com/alexwohlbruck/cat-facts)!

| Source | URL                            |
|--------|--------------------------------|
| '1'    | https://cat-fact.herokuapp.com |
| '2'    | https://catfact.ninja          |

## Requirements

- ansible version >= 2.10
- reachability to above mentioned APIs!

## Installation

To install nwerker.catfacts collection hosted on Galaxy:

```bash
ansible-galaxy collection install nwerker.catfacts
```

To upgrade to the latest version of nwerker.catfacts collection:

```bash
ansible-galaxy collection install nwerker.catfacts --force
```

## Usage

Please refer to the ansible-doc module documentation or README.md of each components

## Contributing

Don't hesitate to Fork / PR or open an issue.

## License

GNU General Public License v3.0

See [LICENSE](LICENSE) to see the full text.

