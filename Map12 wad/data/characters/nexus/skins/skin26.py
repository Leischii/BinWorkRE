#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Nexus/Nexus.bin"
    "DATA/Characters/Nexus/Animations/Skin26.bin"
    "DATA/Nexus_Skins_Root_Skins_Skin10_Skins_Skin11_Skins_Skin14_Skins_Skin15_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin26_Skins_Skin27_Skins_Skin3_Skins_Skin6_Skins_Skin7_Skins_Skin9.bin"
}
entries: map[hash,embed] = {
    "Characters/Nexus/Skins/Skin26" = SkinCharacterDataProperties {
        championSkinName: string = "Nexus_BW_Blue"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Nexus/Animations/Skin26"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Nexus/Skins/Skin26/BW_AP_OrderNexus.skl"
            simpleSkin: string = "ASSETS/Characters/Nexus/Skins/Skin26/BW_AP_OrderNexus.skn"
            0xd62df07c: bool = true
            texture: string = "ASSETS/Characters/Nexus/Skins/Skin26/BW_AP_OrderNexus_TX_CM.dds"
            glossTexture: string = "ASSETS/Characters/Nexus/Skins/Skin26/BW_AP_OrderNexus_TX_GM.dds"
            selfIllumination: f32 = 0.699999988
            fresnelColor: rgba = { 77, 77, 26, 255 }
            fresnel: f32 = 0.300000012
            castShadows: bool = false
            reflectionOpacityDirect: f32 = 0.5
            reflectionFresnel: f32 = 0.899999976
            reflectionFresnelColor: rgba = { 232, 245, 148, 255 }
            initialSubmeshToHide: string = "OrderNexusDestroyed"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Nexus/Skins/Skin26/BW_AP_OrderNexus_TX_CM.dds"
                    submesh: string = "OrderNexusDestroyed"
                }
            }
        }
        armorMaterial: string = "Stone"
        particleOverride_DeathParticle: string = "Nexus_Explosion_Blue.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/Nexus/HUD/Nexus_Blue_Square.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Nexus/HUD/Nexus_Blue_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 8
        }
        mResourceResolver: link = "Characters/Nexus/Skins/Root/Resources"
    }
}
