$classes = @{
    "Parents" = @("parent_id", "name", "email", "password", "phone", "account_status", "creation_date")
    "Children" = @("child_id", "parent_id", "name", "age", "gender", "interests", "profile_picture")
    "Categories" = @("category_id", "category_name", "description")
    "Channels" = @("channel_id", "category_id", "name", "url", "description", "logo", "content_type", "content_topic", "content_language", "country", "presenter_name", "presenter_gender", "presenter_nationality", "presenter_age_group", "target_age_group", "creation_date", "system_status", "date_added", "last_updated")
    "Ratings" = @("rating_id", "channel_id", "parent_id", "age_appropriateness", "educational_value", "language_safety", "violence_level", "ads_level", "total_score", "notes", "rating_date")
    "Suggestions" = @("suggestion_id", "parent_id", "channel_name", "channel_url", "suggestion_description", "status", "suggestion_date")
    "Blocked_Channels" = @("record_id", "parent_id", "channel_id", "block_date")
    "Allowed_Channels" = @("record_id", "child_id", "channel_id", "date_added")
    "Change_Reports" = @("report_id", "parent_id", "channel_id", "change_description", "status", "report_date")
}

$positions = @{
    "Parents" = @(1000, 500)
    "Children" = @(1000, 1000)
    "Categories" = @(1800, 500)
    "Channels" = @(1800, 1000)
    "Ratings" = @(1400, 750)
    "Suggestions" = @(500, 500)
    "Blocked_Channels" = @(1400, 250)
    "Allowed_Channels" = @(1400, 1250)
    "Change_Reports" = @(2200, 750)
}

$xml_output = @()
$xml_output += '<mxGraphModel dx="2248" dy="5352" grid="1" gridSize="10" guides="0" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2000" pageHeight="2000" math="0" shadow="0">'
$xml_output += '  <root>'
$xml_output += '    <mxCell id="0" />'
$xml_output += '    <mxCell id="1" parent="0" />'

$global:cell_id_counter = 2

function get_id {
    $global:cell_id_counter += 1
    return "cell_$global:cell_id_counter"
}

$entity_style = "rounded=0;whiteSpace=wrap;html=1;strokeWidth=3;labelBackgroundColor=none;fontColor=#000000;fontStyle=1;fontSize=21;fontFamily=Helvetica;"
$attr_style = "ellipse;whiteSpace=wrap;html=1;strokeWidth=3;labelBackgroundColor=none;fontColor=#000000;fontStyle=1;fontSize=21;fontFamily=Helvetica;"
$edge_style = "edgeStyle=none;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=3;endArrow=none;endFill=0;fontFamily=Helvetica;fontSize=21;fontStyle=1"
$rel_style = "shape=rhombus;perimeter=rhombusPerimeter;whiteSpace=wrap;html=1;align=center;strokeWidth=3;fontSize=21;labelBackgroundColor=none;fontColor=#000000;fontStyle=1;fontFamily=Helvetica;rotation=0;"

$entity_ids = @{}

foreach ($entity in $classes.Keys) {
    $ent_id = get_id
    $entity_ids[$entity] = $ent_id
    $ex = $positions[$entity][0]
    $ey = $positions[$entity][1]
    
    $xml_output += "    <mxCell id=""$ent_id"" parent=""1"" style=""$entity_style"" value=""$entity"" vertex=""1""><mxGeometry height=""60"" width=""200"" x=""$ex"" y=""$ey"" as=""geometry"" /></mxCell>"
    
    $attrs = $classes[$entity]
    $radius = 200
    $angle_step = 2 * [math]::PI / $attrs.Count
    
    for ($i = 0; $i -lt $attrs.Count; $i++) {
        $attr = $attrs[$i]
        $attr_id = get_id
        $ax = $ex + 50 + $radius * [math]::Cos($i * $angle_step)
        $ay = $ey + $radius * [math]::Sin($i * $angle_step)
        
        $display_attr = $attr
        $entityPrefix = $entity.ToLower()
        if ($attr.EndsWith("_id") -and $entityPrefix.StartsWith($attr.Substring(0, $attr.IndexOf("_id")))) {
            $display_attr = "&lt;u&gt;$attr&lt;/u&gt;"
        }
            
        $xml_output += "    <mxCell id=""$attr_id"" parent=""1"" style=""$attr_style"" value=""$display_attr"" vertex=""1""><mxGeometry height=""40"" width=""160"" x=""$ax"" y=""$ay"" as=""geometry"" /></mxCell>"
        
        $edge_id = get_id
        $xml_output += "    <mxCell id=""$edge_id"" parent=""1"" source=""$ent_id"" target=""$attr_id"" style=""$edge_style"" edge=""1""><mxGeometry relative=""1"" as=""geometry"" /></mxCell>"
    }
}

$relationships = @(
    @("Parents", "manage", "Children", "1", "m"),
    @("Categories", "contain", "Channels", "1", "m"),
    @("Parents", "submit", "Ratings", "1", "m"),
    @("Channels", "receive", "Ratings", "1", "m"),
    @("Parents", "submit", "Suggestions", "1", "m"),
    @("Parents", "block", "Blocked_Channels", "1", "m"),
    @("Channels", "are_blocked", "Blocked_Channels", "1", "m"),
    @("Children", "access", "Allowed_Channels", "1", "m"),
    @("Channels", "are_allowed", "Allowed_Channels", "1", "m"),
    @("Parents", "report", "Change_Reports", "1", "m"),
    @("Channels", "are_reported", "Change_Reports", "1", "m")
)

foreach ($rel in $relationships) {
    $e1 = $rel[0]
    $rel_name = $rel[1]
    $e2 = $rel[2]
    
    $rel_id = get_id
    $ex1 = $positions[$e1][0]
    $ey1 = $positions[$e1][1]
    $ex2 = $positions[$e2][0]
    $ey2 = $positions[$e2][1]
    
    $rx = ($ex1 + $ex2) / 2
    $ry = ($ey1 + $ey2) / 2
    
    $rx_pos = $rx + 50
    $ry_pos = $ry - 25
    
    $xml_output += "    <mxCell id=""$rel_id"" parent=""1"" style=""$rel_style"" value=""$rel_name"" vertex=""1""><mxGeometry height=""110"" width=""150"" x=""$rx_pos"" y=""$ry_pos"" as=""geometry"" /></mxCell>"
    
    $e1_id = $entity_ids[$e1]
    $edge1_id = get_id
    $xml_output += "    <mxCell id=""$edge1_id"" parent=""1"" source=""$e1_id"" target=""$rel_id"" style=""$edge_style"" edge=""1""><mxGeometry relative=""1"" as=""geometry"" /></mxCell>"
    
    $e2_id = $entity_ids[$e2]
    $edge2_id = get_id
    $xml_output += "    <mxCell id=""$edge2_id"" parent=""1"" source=""$rel_id"" target=""$e2_id"" style=""$edge_style"" edge=""1""><mxGeometry relative=""1"" as=""geometry"" /></mxCell>"
}

$xml_output += '  </root>'
$xml_output += '</mxGraphModel>'

$xml_output -join "`n" | Out-File -FilePath "erd_class.xml" -Encoding UTF8
