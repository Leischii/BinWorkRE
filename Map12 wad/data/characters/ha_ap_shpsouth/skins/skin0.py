#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/HA_AP_ShpSouth/HA_AP_ShpSouth.bin"
    "DATA/Characters/HA_AP_ShpSouth/Animations/Skin0.bin"
    "DATA/HA_AP_ShpSouth_Skins_Skin0_Skins_Skin1_Skins_Skin2.bin"
    "DATA/HA_AP_ShpSouth_Skins_Skin0_Skins_Skin2.bin"
}
entries: map[hash,embed] = {
    "Characters/HA_AP_ShpSouth/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "HA_AP_ShopSouth_Animated_Parts"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/HA_AP_ShpSouth/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/HA_AP_ShpSouth/Skins/Base/HA_AP_ShpSouth.skl"
            simpleSkin: string = "ASSETS/Characters/HA_AP_ShpSouth/Skins/Base/HA_AP_ShpSouth.skn"
            texture: string = "ASSETS/Characters/HA_AP_ShpSouth/Skins/Base/HA_AP_ShpSouth.dds"
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        mContextualActionData: link = 0x6e8c5219
        mResourceResolver: link = "Characters/HA_AP_ShpSouth/Skins/Skin0/Resources"
    }
    "Characters/HA_AP_ShpSouth/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0xbea25859 = "Characters/HA_AP_ShpSouth/Skins/Skin0/Particles/HA_AP_ShpSouth_Base_Close01"
            0xdde39875 = "Characters/HA_AP_ShpSouth/Skins/Skin0/Particles/HA_AP_ShpSouth_Base_Open01"
            "HA_Env_MB_shopSouth_groundGlow" = "Characters/HA_AP_ShpSouth/Skins/Skin0/Particles/HA_Env_MB_shopSouth_groundGlow"
            "HA_Env_MB_shopSouth_Range" = "Characters/HA_AP_ShpSouth/Skins/Skin0/Particles/HA_Env_MB_shopSouth_Range"
        }
    }
}
