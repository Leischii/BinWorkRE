#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/HA_AP_ShpNorth/HA_AP_ShpNorth.bin"
    "DATA/Characters/HA_AP_ShpNorth/Animations/Skin0.bin"
    "DATA/HA_AP_ShpNorth_Skins_Skin0_Skins_Skin1_Skins_Skin2.bin"
    "DATA/HA_AP_ShpNorth_Skins_Skin0_Skins_Skin2.bin"
}
entries: map[hash,embed] = {
    "Characters/HA_AP_ShpNorth/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "HA_AP_ShpNorth"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/HA_AP_ShpNorth/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/HA_AP_ShpNorth/Skins/Base/HA_AP_ShpNorth.skl"
            simpleSkin: string = "ASSETS/Characters/HA_AP_ShpNorth/Skins/Base/HA_AP_ShpNorth.skn"
            texture: string = "ASSETS/Characters/HA_AP_ShpNorth/Skins/Base/HA_AP_ShpNorth.dds"
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        mContextualActionData: link = 0x44d080e1
        mResourceResolver: link = "Characters/HA_AP_ShpNorth/Skins/Skin0/Resources"
    }
    "Characters/HA_AP_ShpNorth/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0x076e1b3b = "Characters/HA_AP_ShpNorth/Skins/Skin0/Particles/HA_AP_ShpNorth_Base_Close01"
            0x44a1652c = "Characters/HA_AP_ShpNorth/Skins/Skin0/Particles/HA_AP_ShpNorth_Base_Lantern"
            0xfc6cac07 = "Characters/HA_AP_ShpNorth/Skins/Skin0/Particles/HA_AP_ShpNorth_Base_Open01"
            "HA_Env_MB_shopNorth_Range" = "Characters/HA_AP_ShpNorth/Skins/Skin0/Particles/HA_Env_MB_shopNorth_Range"
        }
    }
}
