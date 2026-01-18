use pyo3_stub_gen::Result;
// use pyo3_stub_gen::StubInfo;
// use std::path::Path;

fn main() -> Result<()> {
    // let path = Path::new("./pyproject.toml");
    // let stub = StubInfo::from_pyproject_toml(path)?;
    let stub = _rs::stub_info()?;
    /*for (name, module) in stub.modules.iter() {
      println!("{}", name);
    }*/
    stub.generate()?;
    Ok(())
}
