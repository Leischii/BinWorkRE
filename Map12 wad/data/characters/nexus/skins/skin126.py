#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Nexus/Nexus.bin"
    "DATA/Characters/Nexus/Animations/Skin26.bin"
    "DATA/Nexus_Skins_Root_Skins_Skin10_Skins_Skin11_Skins_Skin14_Skins_Skin15_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin26_Skins_Skin27_Skins_Skin3_Skins_Skin6_Skins_Skin7_Skins_Skin9.bin"
}
entries: map[hash,embed] = {
    0x8bc164bf = SkinCharacterDataProperties {
        championSkinName: string = "Nexus_BW_Blue_Red"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Nexus/Animations/Skin26"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Nexus/Skins/Skin26/BW_AP_OrderNexus.skl"
            simpleSkin: string = "ASSETS/Characters/Nexus/Skins/Skin26/BW_AP_OrderNexus.skn"
            texture: string = "ASSETS/Characters/Nexus/Skins/Skin26/BW_AP_OrderNexus_TX_CM_red.dds"
            glossTexture: string = "ASSETS/Characters/Nexus/Skins/Skin26/BW_AP_OrderNexus_TX_GM.dds"
            selfIllumination: f32 = 0.699999988
            fresnelColor: rgba = { 26, 26, 77, 255 }
            fresnel: f32 = 0.300000012
            castShadows: bool = false
            reflectionMap: string = "ASSETS/Characters/Nexus/Skins/Skin26/Basic_low_CubeMap.dds"
            reflectionOpacityDirect: f32 = 0.5
            reflectionFresnel: f32 = 0.899999976
            reflectionFresnelColor: rgba = { 179, 179, 245, 255 }
            initialSubmeshToHide: string = "OrderNexusDestroyed"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Nexus/Skins/Skin26/BW_AP_OrderNexus_TX_CM_red.dds"
                    submesh: string = "OrderNexusDestroyed"
                }
            }
        }
        armorMaterial: string = "Stone"
        particleOverride_DeathParticle: string = "BW_Order_Nexus_Explosion.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/Nexus/HUD/Nexus_Red_Square.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Nexus/HUD/Nexus_Red_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 7
        }
        mResourceResolver: link = "Characters/Nexus/Skins/Root/Resources"
    }
}
