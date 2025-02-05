#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/HABW_banner/HABW_banner.bin"
    "DATA/Characters/HABW_banner/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/HABW_banner/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "HABWbanner"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/HABW_banner/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/HABW_banner/Skins/Base/HABW_banner.skl"
            simpleSkin: string = "ASSETS/Characters/HABW_banner/Skins/Base/HABW_banner.skn"
            texture: string = "ASSETS/Characters/HABW_banner/Skins/Base/HABW_banner_TX_CM.dds"
            selfIllumination: f32 = 0.699999988
            castShadows: bool = false
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        armorMaterial: string = "Flesh"
    }
}
