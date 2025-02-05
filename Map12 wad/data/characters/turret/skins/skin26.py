#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Turret/Turret.bin"
    "DATA/Characters/Turret/Animations/Skin26.bin"
    "DATA/Turret_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin12_Skins_Skin13_Skins_Skin16_Skins_Skin17_Skins_Skin20_Skins_Skin22_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin4_Skins_Skin5_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Turret_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin12_Skins_Skin13_Skins_Skin16_Skins_Skin20_Skins_Skin22_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin4_Skins_Skin5_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Turret_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29.bin"
    "DATA/Turret_Skins_Skin26_Skins_Skin27.bin"
}
entries: map[hash,embed] = {
    "Characters/Turret/Skins/Skin26" = SkinCharacterDataProperties {
        championSkinName: string = "Turret_BW_Chaos_Blue"
        emoteLoadout: hash = 0x9029a33d
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Turret/Animations/Skin26"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Turret/Skins/Skin26/BW_AP_ChaosTurret.skl"
            simpleSkin: string = "ASSETS/Characters/Turret/Skins/Skin26/BW_AP_ChaosTurret.skn"
            0xd62df07c: bool = true
            texture: string = "ASSETS/Characters/Turret/Skins/Skin26/BW_AP_ChaosTurret_TX_CM_Blue.dds"
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
            "ASSETS/Characters/Turret/HUD/Turret_Blue_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Turret/HUD/Turret_Blue_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 7
        }
        mResourceResolver: link = "Characters/Turret/Skins/Skin26/Resources"
    }
    "Characters/Turret/Skins/Skin26/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0xec90fddd = 0x12aa1560
            0xf118ff29 = 0xc04038f8
            0x9ef2bde5 = 0xeb564593
            0x127fbf81 = 0xeb564593
            0x93390b0a = 0x0443105f
            0xb6e0e814 = 0x7f291070
            0x755c76df = 0x0443105f
            0xb2694786 = 0x0443105f
            0xb3694919 = 0x0443105f
            0xb4694aac = 0x0443105f
            0x91922da4 = 0xeb564593
            0x92922f37 = 0xeb564593
            0x8f922a7e = 0xeb564593
            0x236cfe8c = 0xc04038f8
            0x246d001f = 0xc04038f8
            0x216cfb66 = 0xc04038f8
            0xb13328d6 = 0xc04038f8
            0x7cd8b37b = 0xe154d820
            0x7dd8b50e = 0xe454dcd9
            0x7bd8b1e8 = 0xe254d9b3
            0x827fcadc = 0x6a177183
        }
    }
}
