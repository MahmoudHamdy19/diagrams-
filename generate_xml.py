import textwrap

actors = [
    ('A1', 'System Admin', 30, 300),
    ('A2', 'Parent', 30, 800),
    ('A3', 'Child', 30, 1150),
    ('A4', 'Guest', 30, 1350),
    ('A5', 'AI System', 1180, 1040),
]

base_ucs = [
    ('U1', 'Manage Users', 200, 100, '#E1D5E7', '#9673A6'),
    ('U2', 'Manage Categories', 200, 220, '#E1D5E7', '#9673A6'),
    ('U3', 'Manage Channels', 200, 360, '#E1D5E7', '#9673A6'),
    ('U4', 'Manage Reports & Proposals', 200, 500, '#E1D5E7', '#9673A6'),
    ('U5', 'View Statistics', 200, 620, '#E1D5E7', '#9673A6'),
    
    ('U6', 'Manage Account', 200, 680, '#D5E8D4', '#82B366'),
    ('U7', 'Manage Children Profiles', 200, 740, '#D5E8D4', '#82B366'),
    ('U8', 'Search & View Channels', 200, 800, '#D5E8D4', '#82B366'),
    ('U9', 'Propose New Channel', 200, 860, '#D5E8D4', '#82B366'),
    ('U10', 'Evaluate & Manage Channels', 200, 920, '#D5E8D4', '#82B366'),
    ('U11', 'Report Channel Content', 200, 980, '#D5E8D4', '#82B366'),
    ('U12', 'Manage Child\'s Allowed Lists', 200, 1040, '#D5E8D4', '#82B366'),
    ('U13', 'Verify Channel Suitability (AI)', 850, 1040, '#FFF2CC', '#D6B656'),
    
    ('U14', 'Login to Child Profile', 200, 1120, '#F8CECC', '#B85450'),
    ('U15', 'View Allowed Channels', 200, 1170, '#F8CECC', '#B85450'),
    ('U16', 'Watch Videos', 200, 1220, '#F8CECC', '#B85450'),
    
    ('U17', 'Register / Login', 200, 1300, '#DAE8FC', '#6C8EBF'),
    ('U18', 'Search Public Channels', 200, 1350, '#DAE8FC', '#6C8EBF'),
]

ext_ucs = [
    # Manage Users Ext
    ('U1_1', 'View Users', 450, 70, '#E1D5E7', '#9673A6', 'U1'),
    ('U1_2', 'Block User', 450, 130, '#E1D5E7', '#9673A6', 'U1'),
    # Manage Categories Ext
    ('U2_1', 'Add Category', 450, 180, '#E1D5E7', '#9673A6', 'U2'),
    ('U2_2', 'Edit Category', 450, 230, '#E1D5E7', '#9673A6', 'U2'),
    ('U2_3', 'Delete Category', 450, 280, '#E1D5E7', '#9673A6', 'U2'),
    # Manage Channels Ext
    ('U3_1', 'View Channel', 450, 330, '#E1D5E7', '#9673A6', 'U3'),
    ('U3_2', 'Add Channel', 450, 380, '#E1D5E7', '#9673A6', 'U3'),
    ('U3_3', 'Edit Channel', 650, 330, '#E1D5E7', '#9673A6', 'U3'),
    ('U3_4', 'Block Channel', 650, 380, '#E1D5E7', '#9673A6', 'U3'),
    # Manage Reports Ext
    ('U4_1', 'View', 450, 450, '#E1D5E7', '#9673A6', 'U4'),
    ('U4_2', 'Accept Proposal', 450, 500, '#E1D5E7', '#9673A6', 'U4'),
    ('U4_3', 'Reject Proposal', 450, 550, '#E1D5E7', '#9673A6', 'U4'),
    ('U4_4', 'Block Channel (Report)', 650, 500, '#E1D5E7', '#9673A6', 'U4'),
    
    # Parent Ext
    ('U6_1', 'Edit Profile', 450, 680, '#D5E8D4', '#82B366', 'U6'),
    ('U7_1', 'Create Profile', 450, 730, '#D5E8D4', '#82B366', 'U7'),
    ('U7_2', 'Edit Profile', 450, 780, '#D5E8D4', '#82B366', 'U7'),
    
    ('U10_1', 'Add Rating', 450, 880, '#D5E8D4', '#82B366', 'U10'),
    ('U10_2', 'Block Channel', 450, 930, '#D5E8D4', '#82B366', 'U10'),
    ('U10_3', 'Unblock Channel', 450, 980, '#D5E8D4', '#82B366', 'U10'),
    ('U10_4', 'Favorite Channel', 650, 905, '#D5E8D4', '#82B366', 'U10'),
    ('U10_5', 'Unfavorite Channel', 650, 955, '#D5E8D4', '#82B366', 'U10'),
]

misc_ext = [
    ('E_EXT_M1', 'U10', 'U8'),
    ('E_EXT_M2', 'U11', 'U8'),
    ('E_EXT_M3', 'U16', 'U15'),
]
misc_inc = [
    ('E_INC_M1', 'U15', 'U14'),
    ('E_INC_M2', 'U12', 'U13'),
]

xml = f'''<mxfile host="app.diagrams.net">
  <diagram name="Raqeeb Use Case" id="raqeeb_uc">
    <mxGraphModel dx="1400" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="1600" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="System" value="Raqeeb System" style="swimlane;whiteSpace=wrap;html=1;startSize=30;labelBackgroundColor=none;fillColor=#877C74;strokeColor=#457B9D;fontColor=#FFFFFF;fontSize=14;fontStyle=1" vertex="1" parent="1">
          <mxGeometry x="150" y="40" width="900" height="1450" as="geometry" />
        </mxCell>
'''

for a_id, a_name, x, y in actors:
    xml += f'        <mxCell id="{a_id}" value="{a_name}" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#877C74;strokeColor=#457B9D;fontColor=#1D3557;fontStyle=1;fontSize=14;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="30" height="60" as="geometry" /></mxCell>\n'

for u_id, u_name, x, y, fc, sc in base_ucs:
    xml += f'        <mxCell id="{u_id}" value="{u_name}" style="ellipse;whiteSpace=wrap;html=1;fillColor={fc};strokeColor={sc};fontColor=#000000;fontSize=12;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="160" height="40" as="geometry" /></mxCell>\n'

for u_id, u_name, x, y, fc, sc, parent_uc in ext_ucs:
    xml += f'        <mxCell id="{u_id}" value="{u_name}" style="ellipse;whiteSpace=wrap;html=1;fillColor={fc};strokeColor={sc};fontColor=#000000;fontSize=12;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="140" height="40" as="geometry" /></mxCell>\n'
    e_id = f'E_EXT_{u_id}'
    xml += f'        <mxCell id="{e_id}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;strokeWidth=2;endArrow=open;endFill=0;strokeColor=#457B9D;" edge="1" parent="1" source="{u_id}" target="{parent_uc}"><mxGeometry relative="1" as="geometry" /></mxCell>\n'
    xml += f'        <mxCell id="{e_id}_L" value="&amp;lt;&amp;lt;extend&amp;gt;&amp;gt;" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];labelBackgroundColor=none;fontColor=#1D3557;fontSize=15;fontStyle=1;fontFamily=Helvetica;" vertex="1" connectable="0" parent="{e_id}"><mxGeometry relative="1" as="geometry" /></mxCell>\n'

for u in ['U1','U2','U3','U4','U5']:
    xml += f'        <mxCell id="E_A1_{u}" style="endArrow=none;html=1;strokeColor=#457B9D;" edge="1" parent="1" source="A1" target="{u}"><mxGeometry relative="1" as="geometry" /></mxCell>\n'
for u in ['U6','U7','U8','U9','U10','U11','U12','U13']:
    xml += f'        <mxCell id="E_A2_{u}" style="endArrow=none;html=1;strokeColor=#457B9D;" edge="1" parent="1" source="A2" target="{u}"><mxGeometry relative="1" as="geometry" /></mxCell>\n'
for u in ['U14','U15','U16']:
    xml += f'        <mxCell id="E_A3_{u}" style="endArrow=none;html=1;strokeColor=#457B9D;" edge="1" parent="1" source="A3" target="{u}"><mxGeometry relative="1" as="geometry" /></mxCell>\n'
for u in ['U17','U18']:
    xml += f'        <mxCell id="E_A4_{u}" style="endArrow=none;html=1;strokeColor=#457B9D;" edge="1" parent="1" source="A4" target="{u}"><mxGeometry relative="1" as="geometry" /></mxCell>\n'

xml += f'        <mxCell id="E_A5_U13" style="endArrow=none;html=1;strokeColor=#457B9D;" edge="1" parent="1" source="A5" target="U13"><mxGeometry relative="1" as="geometry" /></mxCell>\n'

for e_id, src, dst in misc_ext:
    xml += f'        <mxCell id="{e_id}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;strokeWidth=2;endArrow=open;endFill=0;strokeColor=#457B9D;" edge="1" parent="1" source="{src}" target="{dst}"><mxGeometry relative="1" as="geometry" /></mxCell>\n'
    xml += f'        <mxCell id="{e_id}_L" value="&amp;lt;&amp;lt;extend&amp;gt;&amp;gt;" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];labelBackgroundColor=none;fontColor=#1D3557;fontSize=15;fontStyle=1;fontFamily=Helvetica;" vertex="1" connectable="0" parent="{e_id}"><mxGeometry relative="1" as="geometry" /></mxCell>\n'

for e_id, src, dst in misc_inc:
    xml += f'        <mxCell id="{e_id}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;strokeWidth=2;endArrow=open;endFill=0;strokeColor=#457B9D;" edge="1" parent="1" source="{src}" target="{dst}"><mxGeometry relative="1" as="geometry" /></mxCell>\n'
    xml += f'        <mxCell id="{e_id}_L" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];labelBackgroundColor=none;fontColor=#1D3557;fontSize=15;fontStyle=1;fontFamily=Helvetica;" vertex="1" connectable="0" parent="{e_id}"><mxGeometry relative="1" as="geometry" /></mxCell>\n'

xml += '''      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
'''

with open(r'c:\Users\Mahmoud\diagrams-\رقيب.drawio', 'w', encoding='utf-8') as f:
    f.write(xml)

print('Success')
