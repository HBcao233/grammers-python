use pyo3::Python;
use pyo3::types::PyList;
use grammers_tl_types_pyo3::TLObject;

#[test]
fn test_tlobject_pretty_format() {
    Python::initialize();
    Python::attach(|py|{
        let list = PyList::new(py, [1, 2, 3]).unwrap();
        // list.append(1).unwrap();
        let res = TLObject::pretty_format(&list.into_any(), None).unwrap();
        eprintln!("{:?}", res);
        assert_eq!(res, "[\n    1,\n    2,\n    3,\n]");
    });
}
