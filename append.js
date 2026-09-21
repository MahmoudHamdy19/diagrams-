const fs = require("fs");

const tables = [
  {
    id: "Parents",
    name: "Parents",
    x: 100, y: 100,
    cols: ["+ parent_id: PK", "+ name", "+ email", "+ password", "+ phone", "+ account_status", "+ creation_date"]
  },
  {
    id: "Children",
    name: "Children",
    x: 500, y: 100,
    cols: ["+ child_id: PK", "+ parent_id: FK", "+ name", "+ age", "+ gender", "+ interests", "+ profile_picture"]
  },
  {
    id: "Categories",
    name: "Categories",
    x: 900, y: 100,
    cols: ["+ category_id: PK", "+ category_name", "+ description"]
  },
  {
    id: "Channels",
    name: "Channels",
    x: 900, y: 300,
    cols: ["+ channel_id: PK", "+ category_id: FK", "+ name", "+ url", "+ description", "+ logo", "+ content_type", "+ content_topic", "+ content_language", "+ country", "+ presenter_name", "+ presenter_gender", "+ presenter_nationality", "+ presenter_age_group", "+ target_age_group", "+ creation_date", "+ system_status", "+ date_added", "+ last_updated"]
  },
  {
    id: "Ratings",
    name: "Ratings",
    x: 500, y: 400,
    cols: ["+ rating_id: PK", "+ channel_id: FK", "+ parent_id: FK", "+ age_appropriateness", "+ educational_value", "+ language_safety", "+ violence_level", "+ ads_level", "+ total_score", "+ notes", "+ rating_date"]
  },
  {
    id: "Suggestions",
    name: "Suggestions",
    x: 100, y: 400,
    cols: ["+ suggestion_id: PK", "+ parent_id: FK", "+ channel_name", "+ channel_url", "+ suggestion_description", "+ status", "+ suggestion_date"]
  },
  {
    id: "Blocked",
    name: "Blocked Channels",
    x: 500, y: 800,
    cols: ["+ record_id: PK", "+ parent_id: FK", "+ channel_id: FK", "+ block_date"]
  },
  {
    id: "Allowed",
    name: "Allowed Channels",
    x: 900, y: 900,
    cols: ["+ record_id: PK", "+ child_id: FK", "+ channel_id: FK", "+ date_added"]
  },
  {
    id: "Reports",
    name: "Change Reports",
    x: 100, y: 750,
    cols: ["+ report_id: PK", "+ parent_id: FK", "+ channel_id: FK", "+ change_description", "+ status", "+ report_date"]
  }
];

const edges = [
  { source: "Parents", target: "Children", label: "1..*" },
  { source: "Categories", target: "Channels", label: "1..*" },
  { source: "Parents", target: "Ratings", label: "1..*" },
  { source: "Channels", target: "Ratings", label: "1..*" },
  { source: "Parents", target: "Suggestions", label: "1..*" },
  { source: "Parents", target: "Blocked", label: "1..*" },
  { source: "Channels", target: "Blocked", label: "1..*" },
  { source: "Children", target: "Allowed", label: "1..*" },
  { source: "Channels", target: "Allowed", label: "1..*" },
  { source: "Parents", target: "Reports", label: "1..*" },
  { source: "Channels", target: "Reports", label: "1..*" }
];

let xml = `    <diagram name="Class Diagram" id="class_diagram_erd">
    <mxGraphModel dx="1000" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="1200" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />\n`;

tables.forEach(t => {
    let h = 26 + (t.cols.length * 26);
    let w = 280;
    xml += `        <mxCell id="${t.id}" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;strokeWidth=3;fontSize=17;" value="${t.name}" vertex="1" parent="1">
          <mxGeometry x="${t.x}" y="${t.y}" width="${w}" height="${h}" as="geometry" />
        </mxCell>\n`;
    
    t.cols.forEach((col, i) => {
        let cy = 26 + (i * 26);
        xml += `        <mxCell id="${t.id}_${i}" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontSize=17;strokeWidth=3;" value="${col}" vertex="1" parent="${t.id}">
          <mxGeometry y="${cy}" width="${w}" height="26" as="geometry" />
        </mxCell>\n`;
    });
});

edges.forEach((e, i) => {
    xml += `        <mxCell id="E_${i}" edge="1" parent="1" source="${e.source}" target="${e.target}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;endFill=0;strokeWidth=3;fillColor=#dae8fc;strokeColor=#6c8ebf;">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="EL_${i}" value="${e.label}" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontStyle=1;fontSize=16;" vertex="1" connectable="0" parent="E_${i}">
          <mxGeometry x="0" y="0" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>\n`;
});

xml += `      </root>
    </mxGraphModel>
  </diagram>\n</mxfile>`;

const filename = "c:/Users/Mahmoud/diagrams-/رقيب.drawio";
let mainFile = fs.readFileSync(filename, "utf8");

// Since we sliced off the old diagram AND </mxfile>, we just append xml
let updated = mainFile + xml;

// Write back as UTF-8
fs.writeFileSync(filename, updated, "utf8");

console.log("Successfully appended English class diagram.");
