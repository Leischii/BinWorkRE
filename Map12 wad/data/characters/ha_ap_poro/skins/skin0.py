#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/HA_AP_Poro/HA_AP_Poro.bin"
    "DATA/Characters/HA_AP_Poro/Animations/Skin0.bin"
    "DATA/HA_AP_Poro_Skins_Skin0_Skins_Skin3_Skins_Skin4.bin"
}
entries: map[hash,embed] = {
    "Characters/HA_AP_Poro/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "HA_AP_Poro"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/HA_AP_Poro/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/HA_AP_Poro/Skins/Base/HA_AP_Poro.skl"
            simpleSkin: string = "ASSETS/Characters/HA_AP_Poro/Skins/Base/HA_AP_Poro.skn"
            texture: string = "ASSETS/Characters/HA_AP_Poro/Skins/Base/HA_AP_Poro_2.tex"
            skinScale: f32 = 0.280000001
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        armorMaterial: string = "Flesh"
        defaultAnimations: list[string] = {
            "Buffbones"
        }
        mResourceResolver: link = "Characters/HA_AP_Poro/Skins/Skin0/Resources"
    }
}
