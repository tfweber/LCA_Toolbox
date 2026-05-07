from pathlib import Path
import bw2data as bd
import bw2io as bi
from bw2io.importers.bonsai import BonsaiImporter

BONSAI_PATH = Path(r"C:\Users\TimWeber\databases\BONSAI_V2.1.6")
BONSAI_NAME = "BONSAI_V2.1.6"
PROJECT_NAME = "LCA_Toolbox"


def define_b3_map() -> dict:

    biosphere_db = bd.Database(bd.config.biosphere)

    co_fossil = biosphere_db.get(name="Carbon monoxide, fossil", categories=("air",))
    co2_non_fossil = biosphere_db.get(name="Carbon dioxide, non-fossil", categories=("air",))
    co2_fossil = biosphere_db.get(name="Carbon dioxide, fossil", categories=("air",))
    ch4_fossil = biosphere_db.get(name="Methane, fossil", categories=("air",))
    ch4_non_fossil = biosphere_db.get(name="Methane, non-fossil", categories=("air",))
    n2o = biosphere_db.get(name="Dinitrogen monoxide", categories=("air",))

    map_bonsai_b3 = {
        "Carbon_dioxide__fossil_Air": co2_fossil["code"],
        "Carbon_dioxide__biogenic_Air": co2_non_fossil["code"],
        "Methane__fossil_Air": ch4_fossil["code"],
        "Methane__biogenic_Air": ch4_non_fossil["code"],
        "Carbon_monoxide__fossil_Air": co2_non_fossil["code"],
        "Dinitrogen_monoxide_Air": n2o["code"],
    }

    return map_bonsai_b3


def main():

    # delete previous versions of the database
    try:
        del bd.databases[f"{BONSAI_NAME} biosphere"]
        del bd.databases[BONSAI_NAME]
        bd.Database(BONSAI_NAME).delete(warn=False)
        bd.Database(f"{BONSAI_NAME} biosphere").delete(warn=False)
    except KeyError:
        print("db not there")

    # install biosphere3 and set project
    bi.remote.install_project(
        project_key="ecoinvent-3.10-biosphere",
        project_name=PROJECT_NAME,
        overwrite_existing=False,
    )
    bd.projects.set_current(PROJECT_NAME)

    assert BONSAI_PATH.is_dir(), f"BONSAI folder not found at: {BONSAI_PATH}"

    mapping_b3 = define_b3_map()

    bonsai = BonsaiImporter(BONSAI_PATH, BONSAI_NAME, b3mapping=mapping_b3)
    bonsai.apply_strategies()
    bonsai.write_database()


if __name__ == "__main__":
    main()