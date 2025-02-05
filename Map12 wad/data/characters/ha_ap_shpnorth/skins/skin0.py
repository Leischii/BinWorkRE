#PROP_text
type: string = "PROP"
version: u32 = 2
linked: list[string] = {
    "DATA/Characters/HA_AP_ShpNorth/HA_AP_ShpNorth.bin"
    "DATA/Characters/HA_AP_ShpNorth/Animations/Skin1.bin"
}
entries: map[hash,embed] = {
    "Characters/HA_AP_ShpNorth/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "HA_AP_ShpNorth_Skin01"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/HA_AP_ShpNorth/Animations/Skin1"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/HA_AP_ShpNorth/Skins/Base/HA_AP_ShpNorth.skl"
            simpleSkin: string = "ASSETS/Characters/HA_AP_ShpNorth/Skins/Base/HA_AP_ShpNorth.skn"
            texture: string = "ASSETS/Characters/HA_AP_ShpNorth/Skins/Base/HA_AP_ShpNorth.dds"
            skinScale: f32 = 1.64999998
            selfIllumination: f32 = 0.699999988
            castShadows: bool = false
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
    }
}
