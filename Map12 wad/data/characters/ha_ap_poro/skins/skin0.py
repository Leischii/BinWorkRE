#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/HA_AP_Poro/HA_AP_Poro.bin"
    "DATA/Characters/HA_AP_Poro/Animations/Skin2.bin"
}
entries: map[hash,embed] = {
    "Characters/HA_AP_Poro/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "HA_AP_Poro"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/HA_AP_Poro/Animations/Skin2"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/HA_AP_Poro/Skins/Skin02/HA_AP_Poro_Skin02.skl"
            simpleSkin: string = "ASSETS/Characters/HA_AP_Poro/Skins/Skin02/HA_AP_Poro_Skin02.skn"
            texture: string = "ASSETS/Characters/HA_AP_Poro/Skins/Skin02/HA_AP_Poro_Skin02_TX_CM.dds"
            skinScale: f32 = 0.280000001
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        armorMaterial: string = "Flesh"
        defaultAnimations: list[string] = {
            "Buffbones"
        }
    }
}
