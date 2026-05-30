return (
  <div
    style={{
      width: "100vw",
      height: "100vh",
      background: "black",
      position: "relative",
    }}
  >
    <h1
      style={{
        position: "absolute",
        top: "10px",
        width: "100%",
        textAlign: "center",
        color: "white",
        zIndex: 10,
        margin: 0,
      }}
    >
      PsycheGraph AI
    </h1>

    <CytoscapeComponent
      elements={elements}
      layout={{
        name: "cose",
      }}
      style={{
        width: "100vw",
        height: "100vh",
      }}
      stylesheet={[
        {
          selector: "node",
          style: {
            label: "data(label)",
            "background-color": "#61bffc",
            color: "white",
            width: 50,
            height: 50,
            "font-size": 12,
            "text-valign": "center",
            "text-halign": "center",
          },
        },
        {
          selector: "edge",
          style: {
            width: 2,
            label: "data(label)",
            "line-color": "#999",
            "target-arrow-color": "#999",
            "target-arrow-shape": "triangle",
            "curve-style": "bezier",
            color: "white",
            "font-size": 8,
          },
        },
      ]}
    />
  </div>
);