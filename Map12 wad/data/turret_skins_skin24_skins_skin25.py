#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    0x1b3ad53c = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {
                    14
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Break"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Turret/Skins/Skin24/BW_AP_OrderTurret.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Turret/Skins/Skin24/BW_AP_OrderTurret.skl"
                        mAnimationName: string = "ASSETS/Characters/Turret/Skins/Skin24/Particles/HA_BW_OrderTurret_Explode1.anm"
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
                texture: string = "ASSETS/Characters/Turret/Skins/Skin24/Particles/BW_AP_OrderTurret_TX_CM_Rubble.dds"
            }
        }
        particleName: string = "TurretHABackup_Skin05_Break"
        particlePath: string = "Characters/Turret/Skins/Skin24/Particles/TurretHABackup_Skin05_Break"
        flags: u16 = 198
    }
}
