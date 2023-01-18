from collections import namedtuple

Version = namedtuple("Version", "name,url")


def _to_version(*, thing, url_prefix):
    if isinstance(thing, str):
        return Version(name=thing, url=f"{url_prefix}{thing}".lower())
    else:
        try:
            return Version(name=thing.name, url=f"{url_prefix}{thing.url}")
        except AttributeError:
            return Version(name=thing[0], url=f"{url_prefix}{thing[1]}")


def make_html_context(*, current_version, latest_version, versions, url_prefix="./"):
    if isinstance(versions, str):
        raise TypeError(
            f"other_versions {other_versions} was str, not list. Probably not what you wanted."
        )
    version_names = versions
    latest_version = Version(name=latest_version, url=f"{url_prefix}{latest_version}/")
    current_version = Version(name=current_version, url=f"{url_prefix}{current_version}/")

    versions = [
        _to_version(thing=version, url_prefix=url_prefix) for version in version_names
    ]

    html_context = {
        "versions": versions,
        "current_version": current_version,
        "latest_version": latest_version,
    }
    return html_context
