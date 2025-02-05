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
            texture: string = "ASSETS/Characters/HA_AP_Hermit_Robot/Skins/Base/HA_AP_hermit_robot_TX_CM.DDS"
            skinScale: f32 = 1.20000005
            castShadows: bool = false
            selfIllumination: f32 = 0.699999988
        }
        mResourceResolver: link = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Resources"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Leaving01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Leaving01"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Leaving01"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Entering01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Entering01"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Entering01"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Annoyed01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Annoyed01"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Annoyed01"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Idle01"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle01"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle03" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Idle03"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle03"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle02" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Idle02"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle02"
    }
    "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle04" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Robot_Base_Idle04"
        particlePath: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0/Particles/HA_AP_Hermit_Robot_Base_Idle04"
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
