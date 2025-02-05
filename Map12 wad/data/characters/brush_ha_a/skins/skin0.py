#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/brush_HA_A/brush_HA_A.bin"
    "DATA/Characters/brush_HA_A/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/brush_HA_A/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "brush_HA_A"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/brush_HA_A/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/brush_HA_A/Skins/Skin01/brush_BW_A.skl"
            simpleSkin: string = "ASSETS/Characters/brush_HA_A/Skins/Skin01/brush_BW_A.skn"
            texture: string = "ASSETS/Characters/brush_HA_A/Skins/Base/HA_Brush.dds"
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
    }
}
