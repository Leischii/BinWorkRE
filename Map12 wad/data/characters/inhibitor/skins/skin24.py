#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Inhibitor/Inhibitor.bin"
    "DATA/Characters/Inhibitor/Animations/Skin24.bin"
    "DATA/Inhibitor_Skins_Skin0_Skins_Skin1_Skins_Skin12_Skins_Skin14_Skins_Skin15_Skins_Skin18_Skins_Skin19_Skins_Skin20_Skins_Skin21_Skins_Skin24_Skins_Skin25_Skins_Skin4_Skins_Skin5_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Inhibitor_Skins_Skin24_Skins_Skin25.bin"
    "DATA/Inhibitor_Skins_Skin22_Skins_Skin23_Skins_Skin26_Skins_Skin27.bin"
}
entries: map[hash,embed] = {
    "Characters/Inhibitor/Skins/Skin24" = SkinCharacterDataProperties {
        championSkinName: string = "Inhibitor_BW_Blue"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Inhibitor/Animations/Skin24"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/BW_AP_OrderInhibitor.skl"
            simpleSkin: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/BW_AP_OrderInhibitor.skn"
            0xd62df07c: bool = true
            texture: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/BW_AP_OrderInhibitor_TX_CM.dds"
            glossTexture: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/BW_AP_OrderInhibitor_TX_GM.dds"
            selfIllumination: f32 = 0.699999988
            fresnelColor: rgba = { 77, 77, 26, 255 }
            fresnel: f32 = 0.300000012
            reflectionMap: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/Basic_low_CubeMap.dds"
            reflectionOpacityDirect: f32 = 0.5
            reflectionFresnel: f32 = 0.899999976
            reflectionFresnelColor: rgba = { 232, 245, 148, 255 }
            initialSubmeshToHide: string = "Destroyed"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/BW_AP_OrderInhibitor_TX_CM.dds"
                    submesh: string = "Destroyed"
                }
            }
        }
        armorMaterial: string = "Stone"
        idleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "BW_AP_Order_Inhib_idle.troy"
            }
        }
        particleOverride_DeathParticle: string = "BW_Order_Inhibitor_Explosion.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/Inhibitor/HUD/Inhibitor_Blue_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Inhibitor/HUD/Inhibitor_Blue_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 3
        }
        mResourceResolver: link = "Characters/Inhibitor/Skins/Skin24/Resources"
    }
    "Characters/Inhibitor/Skins/Skin24/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0xc4961433 = 0x3fb63ec4
            0x1c9c39c3 = 0x603020bb
            0x90a3a0e4 = 0x603020bb
        }
    }
}
