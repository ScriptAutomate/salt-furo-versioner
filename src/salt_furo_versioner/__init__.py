from collections import namedtuple

Version = namedtuple("Version", "name,url")


def make_html_context(*, current_release, latest_version, versions, url_prefix="./"):
    if isinstance(versions, str):
        raise TypeError(
            f"other_versions {other_versions} was str, not list. Probably not what you wanted."
        )
    version_names = versions
    latest_version = Version(name=latest_version, url=f"{url_prefix}{latest_version}/")
    current_version = Version(name=current_release, url=f"{url_prefix}{current_release}/")

    versions = [
        Version(name=f"{version}", url=f"{url_prefix}{version}/") for version in version_names
    ]

    html_context = {
        "versions": versions,
        "current_version": current_version,
        "latest_version": latest_version,
    }
    return html_context
