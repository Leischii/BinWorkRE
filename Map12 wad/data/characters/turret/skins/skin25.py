#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Turret/Turret.bin"
    "DATA/Turret_Skins_Skin24_Skins_Skin25.bin"
    "DATA/Turret_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29.bin"
    "DATA/Characters/Turret/Animations/Skin24.bin"
    "DATA/Turret_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin12_Skins_Skin13_Skins_Skin16_Skins_Skin17_Skins_Skin20_Skins_Skin22_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin4_Skins_Skin5_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Turret_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin12_Skins_Skin13_Skins_Skin16_Skins_Skin20_Skins_Skin22_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin4_Skins_Skin5_Skins_Skin8_Skins_Skin9.bin"
}
entries: map[hash,embed] = {
    "Characters/Turret/Skins/Skin25" = SkinCharacterDataProperties {
        championSkinName: string = "Turret_BW_Order_Red"
        emoteLoadout: hash = 0x9029a33d
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Turret/Animations/Skin24"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Turret/Skins/Skin24/BW_AP_OrderTurret.skl"
            simpleSkin: string = "ASSETS/Characters/Turret/Skins/Skin24/BW_AP_OrderTurret.skn"
            0xd62df07c: bool = true
            texture: string = "ASSETS/Characters/Turret/Skins/Skin24/BW_AP_OrderTurret_TX_CM_Red.dds"
            selfIllumination: f32 = 0.699999988
            brushAlphaOverride: f32 = 1
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            initialSubmeshToHide: string = "Rubble"
        }
        armorMaterial: string = "Stone"
        idleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "BW_Order_Turret_PearlGlow.troy"
                boneName: string = "C_Buffbone_Glb_Ball_Loc"
            }
        }
        particleOverride_DeathParticle: string = "BW_Order_Turret_Explosion.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/Turret/HUD/Turret_Red_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Turret/HUD/Turret_Red_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 7
        }
        mResourceResolver: link = "Characters/Turret/Skins/Skin25/Resources"
    }
    "Characters/Turret/Skins/Skin25/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0xec90fddd = 0x015b9de5
            0xf118ff29 = 0x5aa19f81
            0x9ef2bde5 = 0x26cea5b9
            0x127fbf81 = 0x26cea5b9
            0xb6e0e814 = 0xc2fe2a9d
            0x91922da4 = 0x26cea5b9
            0x92922f37 = 0x26cea5b9
            0x8f922a7e = 0x26cea5b9
            0x236cfe8c = 0x5aa19f81
            0x246d001f = 0x5aa19f81
            0x216cfb66 = 0x5aa19f81
            0xb13328d6 = 0x5aa19f81
            0x7cd8b37b = 0xe154d820
            0x7dd8b50e = 0xe454dcd9
            0x7bd8b1e8 = 0xe254d9b3
            0xc18ea1e3 = 0x1b3ad53c
        }
    }
}
