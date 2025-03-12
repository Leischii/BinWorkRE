#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/HA_AP_Hermit_Robot/HA_AP_Hermit_Robot.bin"
    "DATA/Characters/HA_AP_Hermit_Robot/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "HA_AP_Hermit_Robot"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/HA_AP_Hermit_Robot/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/HA_AP_Hermit_Robot/Skins/Base/HA_AP_Hermit_Robot.skl"
            simpleSkin: string = "ASSETS/Characters/HA_AP_Hermit_Robot/Skins/Base/HA_AP_Hermit_Robot.skn"
            texture: string = "ASSETS/Characters/HA_AP_Hermit_Robot/Skins/Base/HA_AP_hermit_robot_TX_CM.tex"
            glossTexture: string = "ASSETS/Characters/HA_AP_Hermit_Robot/Skins/Base/HA_AP_hermit_robot_TX_GM.tex"
            skinScale: f32 = 1.20000005
            selfIllumination: f32 = 0.699999988
            reflectionMap: string = "ASSETS/Characters/HA_AP_Hermit_Robot/Skins/Base/HA_AP_hermit_robot_CubeMap.dds"
            reflectionOpacityDirect: f32 = 0.5
            reflectionOpacityGlancing: f32 = 0.699999988
            reflectionFresnel: f32 = 0.899999976
            reflectionFresnelColor: rgba = { 128, 204, 230, 255 }
        }
        mResourceResolver: link = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Resources"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Leaving01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Leaving01"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Leaving01"
        soundOnCreateDefault: string = "Play_sfx_env_map12_ha_ap_hermitrobot_leaving1"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Entering01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Entering01"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Entering01"
        soundPersistentDefault: string = "Play_sfx_env_map12_ha_ap_hermitrobot_entering1"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Annoyed01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Annoyed01"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Annoyed01"
        soundOnCreateDefault: string = "Play_sfx_env_map12_ha_ap_hermitrobot_annoyed"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Idle01"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle01"
        soundPersistentDefault: string = "Play_sfx_env_map12_ha_ap_hermitrobot_idle1"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle03" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Idle03"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle03"
        soundPersistentDefault: string = "Play_sfx_env_map12_ha_ap_hermitrobot_idle3"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle02" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Idle02"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle02"
        soundPersistentDefault: string = "Play_sfx_env_map12_ha_ap_hermitrobot_idle2"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle04" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Idle04"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle04"
        soundPersistentDefault: string = "Play_sfx_env_map12_ha_ap_hermitrobot_idle4"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0x398e2771 = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Annoyed01"
            0x6104140d = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Entering01"
            0xa92e0935 = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle01"
            0xa62e047c = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle02"
            0xa72e060f = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle03"
            0xa42e0156 = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle04"
            0xd902b9db = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Leaving01"
        }
    }
}
