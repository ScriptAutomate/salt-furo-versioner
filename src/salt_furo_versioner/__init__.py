from collections import namedtuple

Version = namedtuple("Version", "name,url")


def make_html_context(*, current_release, latest_version):
    unreleased = Version(name="main", url="./main")
    latest_version = Version(name=f"{latest_version}", url=f"./{latest_version}")
    current_version = Version(name=current_release, url=f"./{current_release}")

    versions = [
        Version(name="3004", url="./3004"),
        current_version,
        latest_version,
        unreleased,
    ]

    html_context = {
        "versions": versions,
        "current_version": current_version,
        "latest_version": latest_version,
    }
    return html_context
