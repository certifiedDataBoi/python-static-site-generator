import typer
from site import Site

def main(source="content", dest="dist"):
    config = {"source":source, "dest":dest}
    source, dest = {**config}
    mainSite = Site(source, dest).build()

typer.run(main())