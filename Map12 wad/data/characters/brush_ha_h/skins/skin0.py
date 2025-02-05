#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/brush_HA_H/brush_HA_H.bin"
    "DATA/Characters/brush_HA_A/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/brush_HA_H/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "brushHAH"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/brush_HA_A/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/brush_HA_H/Skins/Skin01/brush_BW_H.skl"
            simpleSkin: string = "ASSETS/Characters/brush_HA_H/Skins/Skin01/brush_BW_H.skn"
            texture: string = "ASSETS/Characters/brush_HA_A/Skins/Base/HA_Brush.dds"
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
    }
}
