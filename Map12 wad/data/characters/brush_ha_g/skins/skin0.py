#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/brush_HA_G/brush_HA_G.bin"
    "DATA/Characters/brush_HA_A/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/brush_HA_G/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "brushHAG"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/brush_HA_A/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/brush_HA_G/Skins/Skin01/brush_BW_G.skl"
            simpleSkin: string = "ASSETS/Characters/brush_HA_G/Skins/Skin01/brush_BW_G.skn"
            texture: string = "ASSETS/Characters/brush_HA_A/Skins/Base/HA_Brush.dds"
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
    }
}
