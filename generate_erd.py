import json
import math

classes = {
    "Parents": ["parent_id", "name", "email", "password", "phone", "account_status", "creation_date"],
    "Children": ["child_id", "parent_id", "name", "age", "gender", "interests", "profile_picture"],
    "Categories": ["category_id", "category_name", "description"],
    "Channels": ["channel_id", "category_id", "name", "url", "description", "logo", "content_type", "content_topic", "content_language", "country", "presenter_name", "presenter_gender", "presenter_nationality", "presenter_age_group", "target_age_group", "creation_date", "system_status", "date_added", "last_updated"],
    "Ratings": ["rating_id", "channel_id", "parent_id", "age_appropriateness", "educational_value", "language_safety", "violence_level", "ads_level", "total_score", "notes", "rating_date"],
    "Suggestions": ["suggestion_id", "parent_id", "channel_name", "channel_url", "suggestion_description", "status", "suggestion_date"],
    "Blocked_Channels": ["record_id", "parent_id", "channel_id", "block_date"],
    "Allowed_Channels": ["record_id", "child_id", "channel_id", "date_added"],
    "Change_Reports": ["report_id", "parent_id", "channel_id", "change_description", "status", "report_date"]
}

xml_output = []
xml_output.append('<mxGraphModel dx="2248" dy="5352" grid="1" gridSize="10" guides="0" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2000" pageHeight="2000" math="0" shadow="0">')
xml_output.append('  <root>')
xml_output.append('    <mxCell id="0" />')
xml_output.append('    <mxCell id="1" parent="0" />')

cell_id_counter = 2

def get_id():
    global cell_id_counter
    cell_id_counter += 1
    return f"cell_{cell_id_counter}"

positions = {
    "Parents": (1000, 500),
    "Children": (1000, 1000),
    "Categories": (1800, 500),
    "Channels": (1800, 1000),
    "Ratings": (1400, 750),
    "Suggestions": (500, 500),
    "Blocked_Channels": (1400, 250),
    "Allowed_Channels": (1400, 1250),
    "Change_Reports": (2200, 750)
}

entity_style = "rounded=0;whiteSpace=wrap;html=1;strokeWidth=3;labelBackgroundColor=none;fontColor=#000000;fontStyle=1;fontSize=21;fontFamily=Helvetica;"
attr_style = "ellipse;whiteSpace=wrap;html=1;strokeWidth=3;labelBackgroundColor=none;fontColor=#000000;fontStyle=1;fontSize=21;fontFamily=Helvetica;"
edge_style = "edgeStyle=none;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=3;endArrow=none;endFill=0;fontFamily=Helvetica;fontSize=21;fontStyle=1"
rel_style = "shape=rhombus;perimeter=rhombusPerimeter;whiteSpace=wrap;html=1;align=center;strokeWidth=3;fontSize=21;labelBackgroundColor=none;fontColor=#000000;fontStyle=1;fontFamily=Helvetica;rotation=0;"

entity_ids = {}

# Create entities and attributes
for entity, attrs in classes.items():
    ent_id = get_id()
    entity_ids[entity] = ent_id
    ex, ey = positions[entity]
    xml_output.append(f'    <mxCell id="{ent_id}" parent="1" style="{entity_style}" value="{entity}" vertex="1"><mxGeometry height="60" width="200" x="{ex}" y="{ey}" as="geometry" /></mxCell>')
    
    radius = 200
    angle_step = 2 * math.pi / len(attrs)
    for i, attr in enumerate(attrs):
        attr_id = get_id()
        ax = ex + 50 + radius * math.cos(i * angle_step)
        ay = ey + radius * math.sin(i * angle_step)
        
        display_attr = attr
        if "_id" in attr and entity.lower().startswith(attr.split("_id")[0]):
            display_attr = f"&lt;u&gt;{attr}&lt;/u&gt;"
            
        xml_output.append(f'    <mxCell id="{attr_id}" parent="1" style="{attr_style}" value="{display_attr}" vertex="1"><mxGeometry height="40" width="160" x="{ax}" y="{ay}" as="geometry" /></mxCell>')
        
        edge_id = get_id()
        xml_output.append(f'    <mxCell id="{edge_id}" parent="1" source="{ent_id}" target="{attr_id}" style="{edge_style}" edge="1"><mxGeometry relative="1" as="geometry" /></mxCell>')

relationships = [
    ("Parents", "manage", "Children", "1", "m"),
    ("Categories", "contain", "Channels", "1", "m"),
    ("Parents", "submit", "Ratings", "1", "m"),
    ("Channels", "receive", "Ratings", "1", "m"),
    ("Parents", "submit", "Suggestions", "1", "m"),
    ("Parents", "block", "Blocked_Channels", "1", "m"),
    ("Channels", "are_blocked", "Blocked_Channels", "1", "m"),
    ("Children", "access", "Allowed_Channels", "1", "m"),
    ("Channels", "are_allowed", "Allowed_Channels", "1", "m"),
    ("Parents", "report", "Change_Reports", "1", "m"),
    ("Channels", "are_reported", "Change_Reports", "1", "m")
]

# Create relationships and edges
for e1, rel_name, e2, card1, card2 in relationships:
    rel_id = get_id()
    ex1, ey1 = positions[e1]
    ex2, ey2 = positions[e2]
    rx = (ex1 + ex2) / 2
    ry = (ey1 + ey2) / 2
    
    xml_output.append(f'    <mxCell id="{rel_id}" parent="1" style="{rel_style}" value="{rel_name}" vertex="1"><mxGeometry height="110" width="150" x="{rx+50}" y="{ry-25}" as="geometry" /></mxCell>')
    
    edge1_id = get_id()
    xml_output.append(f'    <mxCell id="{edge1_id}" parent="1" source="{entity_ids[e1]}" target="{rel_id}" style="{edge_style}" edge="1"><mxGeometry relative="1" as="geometry" /></mxCell>')
    
    edge2_id = get_id()
    xml_output.append(f'    <mxCell id="{edge2_id}" parent="1" source="{rel_id}" target="{entity_ids[e2]}" style="{edge_style}" edge="1"><mxGeometry relative="1" as="geometry" /></mxCell>')

xml_output.append('  </root>')
xml_output.append('</mxGraphModel>')

with open('erd_class.xml', 'w') as f:
    f.write("\\n".join(xml_output))
