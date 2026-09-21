const fs = require('fs');

const mainFile = 'c:/Users/Mahmoud/diagrams-/رقيب.drawio';
const srcFile = 'c:/Users/Mahmoud/diagrams-/Class_Diagram.drawio';

let rawBuffer = fs.readFileSync(mainFile);
let isUtf16 = false;
if (rawBuffer.length > 1 && rawBuffer[1] === 0) {
    isUtf16 = true;
}

let mainXml = fs.readFileSync(mainFile, isUtf16 ? 'utf16le' : 'utf8');
let srcXml = fs.readFileSync(srcFile, 'utf8');

// Extract the diagram from srcXml
const diagramMatch = srcXml.match(/<diagram[^>]*>[\s\S]*?<\/diagram>/);
if (!diagramMatch) {
    console.error("No diagram found in src file.");
    process.exit(1);
}

const diagramContent = diagramMatch[0];

// Remove any existing class_diagram_erd to avoid duplicates
if (mainXml.includes('class_diagram_erd')) {
    mainXml = mainXml.replace(/<diagram[^>]*id="class_diagram_erd"[^>]*>[\s\S]*?<\/diagram>/g, '');
}

// Ensure the main file ends with </mxfile>
// Append the diagram right before </mxfile>
const updated = mainXml.replace('</mxfile>', `  ${diagramContent}\n</mxfile>`);

fs.writeFileSync(mainFile, updated, 'utf8');
console.log("Safely merged Class Diagram with proper encoding.");
