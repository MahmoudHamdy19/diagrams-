const fs = require("fs");

const tables = [
  {
    id: "Parents",
    name: "أولياء الأمور",
    x: 100, y: 100,
    cols: ["+ رقم ولي الأمر: PK", "+ الاسم", "+ البريد الإلكتروني", "+ كلمة المرور", "+ رقم الجوال", "+ حالة الحساب", "+ تاريخ الإنشاء"]
  },
  {
    id: "Children",
    name: "الأطفال",
    x: 500, y: 100,
    cols: ["+ رقم الطفل: PK", "+ رقم ولي الأمر: FK", "+ اسم الطفل", "+ العمر", "+ الجنس", "+ الاهتمامات", "+ صورة الملف الشخصي"]
  },
  {
    id: "Categories",
    name: "تصنيفات القنوات",
    x: 900, y: 100,
    cols: ["+ رقم التصنيف: PK", "+ اسم التصنيف", "+ وصف التصنيف"]
  },
  {
    id: "Channels",
    name: "القنوات",
    x: 900, y: 300,
    cols: ["+ رقم القناة: PK", "+ رقم التصنيف: FK", "+ اسم القناة", "+ رابط القناة", "+ وصف القناة", "+ صورة القناة", "+ نوع المحتوى", "+ موضوع المحتوى", "+ لغة المحتوى", "+ دولة القناة", "+ اسم مقدم المحتوى", "+ جنس مقدم المحتوى", "+ جنسية مقدم المحتوى", "+ عمر مقدم المحتوى", "+ الفئة العمرية المستهدفة", "+ تاريخ إنشاء القناة", "+ حالة القناة", "+ تاريخ الإضافة", "+ تاريخ آخر تحديث"]
  },
  {
    id: "Ratings",
    name: "تقييمات القنوات",
    x: 500, y: 400,
    cols: ["+ رقم التقييم: PK", "+ رقم القناة: FK", "+ رقم ولي الأمر: FK", "+ تقييم العمر المناسب", "+ تقييم القيمة التعليمية", "+ تقييم سلامة اللغة", "+ تقييم مستوى العنف", "+ تقييم مستوى الإعلانات", "+ درجة التقييم الإجمالية", "+ الملاحظات", "+ تاريخ التقييم"]
  },
  {
    id: "Suggestions",
    name: "مقترحات القنوات",
    x: 100, y: 400,
    cols: ["+ رقم المقترح: PK", "+ رقم ولي الأمر: FK", "+ اسم القناة", "+ رابط القناة", "+ وصف المقترح", "+ حالة المقترح", "+ تاريخ المقترح"]
  },
  {
    id: "Blocked",
    name: "القنوات المحجوبة",
    x: 500, y: 750,
    cols: ["+ رقم السجل: PK", "+ رقم ولي الأمر: FK", "+ رقم القناة: FK", "+ تاريخ الحجب"]
  },
  {
    id: "Allowed",
    name: "القنوات المسموحة",
    x: 900, y: 850,
    cols: ["+ رقم السجل: PK", "+ رقم الطفل: FK", "+ رقم القناة: FK", "+ تاريخ الإضافة"]
  },
  {
    id: "Reports",
    name: "بلاغات التغيير",
    x: 100, y: 700,
    cols: ["+ رقم البلاغ: PK", "+ رقم ولي الأمر: FK", "+ رقم القناة: FK", "+ وصف التغيير", "+ حالة البلاغ", "+ تاريخ البلاغ"]
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

let xml = `  <diagram name="Class Diagram" id="class_diagram_erd">
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

// We will read the file and append the tab.
const filename = "رقيب.drawio";
const mainFile = fs.readFileSync(filename, "utf8");
const updated = mainFile.replace("</mxfile>", xml);
fs.writeFileSync(filename, updated, "utf8");
console.log("Appended Class Diagram tab.");
