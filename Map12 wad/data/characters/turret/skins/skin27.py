#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Turret/Animations/Skin26.bin"
    "DATA/Characters/Turret/Turret.bin"
    "DATA/Turret_Skins_Skin1_Skins_Skin11_Skins_Skin14_Skins_Skin15_Skins_Skin18_Skins_Skin19_Skins_Skin21_Skins_Skin23_Skins_Skin26_Skins_Skin27_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin35_Skins_Skin7.bin"
    "DATA/Turret_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Turret_Skins_Skin1_Skins_Skin11_Skins_Skin14_Skins_Skin15_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin26_Skins_Skin27_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin35_Skins_Skin7.bin"
    "DATA/Turret_Skins_Skin1_Skins_Skin11_Skins_Skin14_Skins_Skin15_Skins_Skin18_Skins_Skin19_Skins_Skin21_Skins_Skin23_Skins_Skin26_Skins_Skin27_Skins_Skin29_Skins_Skin3_Skins_Skin31_Skins_Skin35_Skins_Skin7.bin"
    "DATA/Turret_Skins_Skin1_Skins_Skin11_Skins_Skin14_Skins_Skin15_Skins_Skin18_Skins_Skin19_Skins_Skin21_Skins_Skin23_Skins_Skin26_Skins_Skin27_Skins_Skin29_Skins_Skin3_Skins_Skin35_Skins_Skin7.bin"
    "DATA/Turret_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29.bin"
    "DATA/Turret_Skins_Skin26_Skins_Skin27.bin"
}
entries: map[hash,embed] = {
    "Characters/Turret/Skins/Skin27" = SkinCharacterDataProperties {
        championSkinName: string = "Turret_BW_Chaos_Red"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Turret/Animations/Skin26"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Turret/Skins/Skin26/BW_AP_ChaosTurret.skl"
            simpleSkin: string = "ASSETS/Characters/Turret/Skins/Skin26/BW_AP_ChaosTurret.skn"
            0xd62df07c: bool = true
            texture: string = "ASSETS/Characters/Turret/Skins/Skin26/BW_AP_ChaosTurret_TX_CM.dds"
            selfIllumination: f32 = 0.699999988
            brushAlphaOverride: f32 = 1
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            initialSubmeshToHide: string = "Rubble, Rubble_Submesh"
        }
        armorMaterial: string = "Stone"
        idleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "BW_Chaos_Turret_GemGlow.troy"
                boneName: string = "R_Buffbone_Glb_Hand_Loc"
            }
        }
        particleOverride_DeathParticle: string = "BW_Chaos_Turret_Explosion.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/Turret/HUD/Turret_Red_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Turret/HUD/Turret_Red_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 8
        }
        mResourceResolver: link = "Characters/Turret/Skins/Skin27/Resources"
    }
    "Characters/Turret/Skins/Skin27/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0xec90fddd = 0x53013e59
            0xf118ff29 = 0x38863ac1
            0x9ef2bde5 = 0x68210d01
            0x127fbf81 = 0x7943e3ed
            0xb6e0e814 = 0x7f291070
            0x755c76df = 0x0c94cea7
            0xb2694786 = 0x0d94d03a
            0xb3694919 = 0x0e94d1cd
            0xb4694aac = 0x0794c6c8
            0x91922da4 = 0x5a8de8c0
            0x92922f37 = 0x5b8dea53
            0x8f922a7e = 0x608df232
            0x236cfe8c = 0x35863608
            0x246d001f = 0x3686379b
            0x216cfb66 = 0x3b863f7a
            0xb13328d6 = 0x5597af25
            0x7cd8b37b = 0xe154d820
            0x7dd8b50e = 0xe454dcd9
            0x7bd8b1e8 = 0xe254d9b3
            0x73b92572 = 0x37aabda5
            0x448e201f = 0x0328dd7e
            0xd8251525 = 0xef412ed8
            0xe64adb92 = 0xe7adc389
            0x4af55a7c = 0x95895623
            0x827fcadc = 0x6a177183
        }
    }
}
