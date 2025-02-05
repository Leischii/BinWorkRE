#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/brush_HA_C/brush_HA_C.bin"
    "DATA/Characters/brush_HA_A/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/brush_HA_C/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "brushHAC"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/brush_HA_A/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/brush_HA_C/Skins/Skin01/brush_BW_C.skl"
            simpleSkin: string = "ASSETS/Characters/brush_HA_C/Skins/Skin01/brush_BW_C.skn"
            texture: string = "ASSETS/Characters/brush_HA_A/Skins/Base/HA_Brush.dds"
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
    }
}
