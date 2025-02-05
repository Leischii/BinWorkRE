#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    0x6a177183 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4.25
                }
                particleLinger: option[f32] = {
                    14.25
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Break"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Turret/Skins/Skin26/BW_AP_ChaosTurret.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Turret/Skins/Skin26/BW_AP_ChaosTurret.skl"
                        mAnimationName: string = "ASSETS/Characters/Turret/Skins/Skin26/Particles/HA_BW_ChaosTurret_explode1.anm"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Turret/Skins/Skin26/Particles/BW_AP_ChaosTurret_TX_CM_Rubble.dds"
            }
        }
        particleName: string = "HA_AP_ChaosTurret_Skin05_Break"
        particlePath: string = "Characters/Turret/Skins/Skin26/Particles/HA_AP_ChaosTurret_Skin05_Break"
        flags: u16 = 198
    }
}
