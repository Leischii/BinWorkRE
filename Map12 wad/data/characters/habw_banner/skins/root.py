#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/HABW_banner/HABW_banner.bin"
    "DATA/Characters/HABW_banner/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/HABW_banner/Skins/Root" = SkinCharacterDataProperties {
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/HABW_banner/Animations/Skin0"
        }
        armorMaterial: string = "Flesh"
    }
}
