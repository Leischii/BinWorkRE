#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Inhibitor/Inhibitor.bin"
    "DATA/Characters/Inhibitor/Animations/Skin24.bin"
    "DATA/Inhibitor_Skins_Skin0_Skins_Skin1_Skins_Skin12_Skins_Skin14_Skins_Skin15_Skins_Skin18_Skins_Skin19_Skins_Skin20_Skins_Skin21_Skins_Skin24_Skins_Skin25_Skins_Skin4_Skins_Skin5_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Inhibitor_Skins_Skin24_Skins_Skin25.bin"
}
entries: map[hash,embed] = {
    "Characters/Inhibitor/Skins/Skin25" = SkinCharacterDataProperties {
        championSkinName: string = "Inhibitor_BW_Red"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Inhibitor/Animations/Skin24"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/BW_AP_OrderInhibitor.skl"
            simpleSkin: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/BW_AP_OrderInhibitor.skn"
            0xd62df07c: bool = true
            texture: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/BW_AP_OrderInhibitor_TX_CM_Red.tex"
            glossTexture: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/BW_AP_OrderInhibitor_TX_GM.tex"
            selfIllumination: f32 = 0.699999988
            fresnelColor: rgba = { 30, 43, 77, 255 }
            fresnel: f32 = 0.300000012
            reflectionMap: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/Basic_low_CubeMap.dds"
            reflectionOpacityDirect: f32 = 0.5
            reflectionFresnel: f32 = 0.899999976
            reflectionFresnelColor: rgba = { 146, 245, 232, 255 }
            initialSubmeshToHide: string = "Destroyed"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/BW_AP_OrderInhibitor_TX_CM_Red.tex"
                    submesh: string = "Destroyed"
                }
            }
        }
        armorMaterial: string = "Stone"
        particleOverride_DeathParticle: string = "Inhibitor_Explosion_Red.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/Inhibitor/HUD/Inhibitor_Red_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Inhibitor/HUD/Inhibitor_Red_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 3
        }
        mResourceResolver: link = "Characters/Inhibitor/Skins/Skin25/Resources"
    }
    "Characters/Inhibitor/Skins/Skin25/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0xc4961433 = 0x3fb63ec4
            0xcff78af8 = 0x603020bb
        }
    }
}
