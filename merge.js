const fs = require('fs');

const mainFile = 'c:/Users/Mahmoud/diagrams-/رقيب.drawio';
const srcFile = 'c:/Users/Mahmoud/diagrams-/Class_Diagram.drawio';

let mainXml = fs.readFileSync(mainFile, 'utf8');
let srcXml = fs.readFileSync(srcFile, 'utf8');

// Extract the diagram from srcXml
const diagramMatch = srcXml.match(/<diagram[^>]*>[\s\S]*?<\/diagram>/);
if (!diagramMatch) {
    console.error("No diagram found in src file.");
    process.exit(1);
}

const diagramContent = diagramMatch[0];

// Make sure it's not already in the main file to avoid duplication
if (mainXml.includes('id="class_diagram_erd"')) {
    console.log("Removing existing class_diagram_erd from main file.");
    mainXml = mainXml.replace(/<diagram[^>]*id="class_diagram_erd"[^>]*>[\s\S]*?<\/diagram>/g, '');
}

// Ensure the main file ends with </mxfile>
// Append the diagram right before </mxfile>
const updated = mainXml.replace('</mxfile>', `  ${diagramContent}\n</mxfile>`);

fs.writeFileSync(mainFile, updated, 'utf8');
console.log("Merged Class Diagram into main file successfully.");
