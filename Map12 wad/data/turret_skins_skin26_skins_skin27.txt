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
                        mMeshName: string = "ASSETS/Characters/HA_AP_ChaosTurret/Skins/Skin05/Particles/HA_BW_ChaosTurret.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/HA_AP_ChaosTurret/Skins/Skin05/Particles/HA_BW_ChaosTurret.skl"
                        mAnimationName: string = "ASSETS/Characters/HA_AP_ChaosTurret/Skins/Skin05/Particles/HA_BW_ChaosTurret_explode1.anm"
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
    0xeb564593 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.899999976
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.25
                        }
                    }
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Basic1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 700, 110, 700 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 700, 110, 700 }
                        }
                    }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                emissionMeshName: string = "Data/Particles/BW_Chaos_Turret_SparkShell_Tar_mesh.scb"
                blendMode: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 37.5, 85, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 37.5, 85, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Sparks_4x1.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.699999988
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.200000003
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.349999994
                }
                isSingleParticle: flag = true
                emitterName: string = "Explosion_01_Add"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0.325504988 }
                            { 1, 1, 1, 1 }
                            { 0.100000001, 0.100000001, 0.100000001, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaRef: u8 = 4
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 100, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 1.29999995, 1.29999995, 0 }
                            { 1, 1, 0 }
                            { 0.699999988, 0.699999988, 0 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Turret_Explosion_Flat_Tar.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.600000024
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "Explosion_Smoke1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 1500, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 1500, 100 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 14, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 14, 1 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 70, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 70, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 20, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.25
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                    }
                                    keyValues: list[f32] = {
                                        0.5
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 20, 20, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.470587999, 0, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.941175997, 0, 0, 1 }
                            { 0.470587999, 0, 0, 1 }
                            { 0.470587999, 0, 0, 0.792203009 }
                            { 0.235293999, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.200000003
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    0.699999988
                                    -0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 80, 0, 0 }
                            { 1600, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 115, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 115, 0, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 0.699999988, 0, 0 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Turret_Smoke_Tar.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLinger: option[f32] = {
                    0.100000001
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "White_GlowFlash1"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 40, 50 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.576470613 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.112545997
                            0.449999988
                            0.998000026
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 0.498039007, 1 }
                            { 1, 0.639216006, 0.0196080003, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 0 }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Cas_glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLinger: option[f32] = {
                    0.100000001
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "White_GlowFlash2"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 40, 50 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.576470613 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.112545997
                            0.449999988
                            0.998000026
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 0.498039007, 1 }
                            { 1, 0.639216006, 0.0196080003, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 0 }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Cas_glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.699999988
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.699999988
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.150000006
                }
                isSingleParticle: flag = true
                emitterName: string = "Explosion_1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 600, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 600, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 8, 5 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 40, 50, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 40, 50, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0.260403991 }
                            { 1, 1, 1, 0.800000012 }
                            { 0.100000001, 0.100000001, 0.100000001, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaRef: u8 = 4
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.600000024
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 100, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0.699999988, 0.699999988, 0 }
                            { 1, 1, 0 }
                            { 1.20000005, 1.20000005, 0 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Turret_Explosion_Flat_Tar.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "FlashCore1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 66
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 120, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 1.60000002, 1.60000002, 0 }
                        }
                    }
                }
                texture: string = "Data/Particles/SRU_chaos_flashCore.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    13
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    1
                }
                childParticleSetDefinition: embed = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = 0x0506bf3a
                        }
                    }
                }
                emitterName: string = "SparkHelix1"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1300, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.600000024
                                    0.699999988
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1300, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 3, 3 }
                }
                acceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -800, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 6, 0 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 80, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 80, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            90
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 4
                colorLookUpTypeY: u8 = 3
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.349999994
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 0, 0 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 8
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 31, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 31, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 0 }
                            { 0.100000001, 0.100000001, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Sparks_4x1.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    0.850000024
                }
                isSingleParticle: flag = true
                emitterName: string = "praxisRing"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/HA_AP_praxis_geo.sco"
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.100000001 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.850979984, 0.462745011, 0.121569, 0.100000001 }
                            { 1, 0.329412013, 0.0627449974, 0.100000001 }
                            { 1, 0.478430986, 0.129411995, 0.100000001 }
                        }
                    }
                }
                pass: i16 = 5
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2.5, 2.5, 2.5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2.5, 2.5, 2.5 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "Data/Particles/HA_Chaos_praxis.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "NailShapes"
                disabled: bool = true
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -35
                                        35
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        50
                                        90
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -35
                                        35
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/BW_Chaos_Turret_Tor_Tar_mesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.00575800007
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 15
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    180
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    -180
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.600000024
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.252398998
                            0.379079014
                            0.476967007
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.99981159, 0.99981159, 0.99981159 }
                            { 1.10079217, 1.10079217, 1.10079217 }
                            { 1.69705832, 1.69705832, 1.69705832 }
                            { 1.99038279, 1.99038279, 1.99038279 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Sparks_4x1.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.300000012, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    2
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.300000012, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.10000002
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    0.100000001
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "GlowFlash"
                disabled: bool = true
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 30, 0 }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.525490224, 0.20784314, 0.380392164 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.112545997
                            0.449999988
                            0.998000026
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 250, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Cas_glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.10000002
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    0.100000001
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "GlowFlash1"
                disabled: bool = true
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 30, 0 }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.525490224, 0.20784314, 0.380392164 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.112545997
                            0.449999988
                            0.998000026
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 250, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Cas_glow.dds"
            }
        }
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1.10000002
                }
                isSingleParticle: flag = true
                emitterName: string = "Flash"
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "FirefighterTristana"
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 40, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                particleColorTexture: string = "Data/Particles/color-rampdown.dds"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                meshRenderFlags: u8 = 0
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.501960814 }
                }
                pass: i16 = 2
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                texture: string = "Data/Particles/BW_Chaos_Turret_Cas_FlashCap_Mesh_2x2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                0xbc022424: pointer = 0x7f70a2b2 {
                    scale: embed = ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                1
                                210
                            }
                        }
                    }
                    birthRotation: embed = ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        360
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[f32] = {
                                1
                            }
                        }
                    }
                    particleBind: vec2 = { 1, 1 }
                }
            }
        }
        particleName: string = "bw_chaosturretfire_tar"
        particlePath: string = "Data/Particles/bw_chaosturretfire_tar"
        soundOnCreateDefault: string = "Play_sfx_Env_Map14_ChaosTurretChampionBasicAttack_hit"
    }
    0x12aa1560 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {
                    0.0500000007
                }
                emitterName: string = "misGeo2"
                importance: u8 = 2
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -78, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/BW_Chaos_Turret_Speedlines_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.368597001 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                isLocalOrientation: flag = false
                particleIsLocalOrientation: flag = true
                texture: string = "Data/Particles/BW_Chaos_Turret_SpeedLines.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "Data/Particles/BW_Chaos_Turret_SpeedLines_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1.5 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.0500000007
                }
                emitterName: string = "bullet2"
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "RocketTristana"
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/bw_chaos_turret_cannonball_mesh.scb"
                    }
                }
                blendMode: u8 = 3
                pass: i16 = 1
                isLocalOrientation: flag = false
                doesCastShadow: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -111, 1111 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, -111, 1111 }
                            { 0, -111, 1111 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_CannonBall.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.0500000007
                }
                isSingleParticle: flag = true
                emitterName: string = "HeatBall"
                disabled: bool = true
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "RocketTristana"
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/bw_chaos_turret_cannonball_mesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0, 0.380391985 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.325489998 }
                        }
                    }
                }
                pass: i16 = 2
                texture: string = "Data/Particles/BW_Chaos_CannonBall_heat.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[f32] = {
                            0.400000006
                            0.400000006
                            0.319999993
                            0.159999996
                            0.119999997
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "SmokeTrail1"
                birthVelocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 1 }
                            { 0, 0, 0 }
                            { 0, 0, 0.5 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.349999994
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.524999976 }
                            { 1, 1, 1, 0.360000014 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.349999994, 0.200000003, 0.100000001, 0 }
                            { 1, 0.882353008, 0.866666973, 1 }
                            { 1, 0.752941012, 0.576470971, 1 }
                            { 0.988234997, 0.823529005, 0.619607985, 0 }
                        }
                    }
                }
                pass: i16 = 30
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 1, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                        }
                        values: list[vec3] = {
                            { 0, 1, 30 }
                            { 45, 1, 30 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.600000024, 1, 1 }
                            { 0.5, 1, 1 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_BA_Mis_SmokeTrail.dds"
                texDiv: vec2 = { 4, 1 }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[f32] = {
                            0.400000006
                            0.400000006
                            0.319999993
                            0.159999996
                            0.119999997
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "SmokeTrail2"
                birthVelocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 1 }
                            { 0, 0, 0 }
                            { 0, 0, 0.5 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.349999994
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.524999976 }
                            { 1, 1, 1, 0.360000014 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.349999994, 0.200000003, 0.100000001, 0 }
                            { 1, 0.882353008, 0.866666973, 1 }
                            { 1, 0.752941012, 0.576470971, 1 }
                            { 0.988234997, 0.823529005, 0.619607985, 0 }
                        }
                    }
                }
                pass: i16 = 30
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 1, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                        }
                        values: list[vec3] = {
                            { 0, 1, 30 }
                            { 45, 1, 30 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.600000024, 1, 1 }
                            { 0.5, 1, 1 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_BA_Mis_SmokeTrail.dds"
                texDiv: vec2 = { 4, 1 }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 35
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            105
                            0
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0.5
                            0.25
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    5
                }
                emitterName: string = "Sparks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 250, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -2
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -2
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 250, 50 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 10 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 2 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -10
                                        10
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -10
                                        10
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 2 }
                            }
                        }
                    }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 4
                colorLookUpTypeY: u8 = 3
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 20
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 40, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 40, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 1 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Sparks.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    0.699999988
                }
                emitterName: string = "trail2"
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1000
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.819607973, 0.0941179991, 0 }
                            { 1, 0.576470971, 0.0901959985, 0.972549021 }
                            { 1, 0.470587999, 0.164706007, 0.87450999 }
                            { 1, 0.831372976, 0.541176021, 0.200000003 }
                            { 1, 0.87450999, 0.768626988, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isLocalOrientation: flag = false
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_BA_Mis_SmokeTrail.dds"
                texDiv: vec2 = { 6, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.0500000007
                }
                emitterName: string = "bullet3"
                disabled: bool = true
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "RocketTristana"
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/BW_Chaos_Turret_Speedlines_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.368597001 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                doesCastShadow: flag = true
                texture: string = "Data/Particles/BW_Chaos_Turret_SpeedLines.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "Data/Particles/BW_Chaos_Turret_SpeedLines_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1.5 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 200
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[f32] = {
                            0.300000012
                            0.300000012
                            0.24000001
                            0.120000005
                            0.0900000036
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.379999995
                }
                emitterName: string = "BlurTrail"
                birthVelocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 1 }
                            { 0, 0, 0 }
                            { 0, 0, 0.5 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.349999994
                            0.600000024
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 0.411764711, 0.0901960805, 0 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.324117661 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.264411777 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.349999994, 0.200000003, 0.100000001, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 31, 1, 1 }
                }
                texture: string = "Data/Particles/BW_Chaos_BA_Mis_BlurTrail.dds"
                texDiv: vec2 = { 3, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 200
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[f32] = {
                            0.300000012
                            0.300000012
                            0.24000001
                            0.120000005
                            0.0900000036
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.379999995
                }
                emitterName: string = "BlurTrail1"
                birthVelocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 1 }
                            { 0, 0, 0 }
                            { 0, 0, 0.5 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.349999994
                            0.600000024
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 0.411764711, 0.0901960805, 0 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.324117661 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.264411777 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.349999994, 0.200000003, 0.100000001, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 31, 1, 1 }
                }
                texture: string = "Data/Particles/BW_Chaos_BA_Mis_BlurTrail.dds"
                texDiv: vec2 = { 3, 1 }
            }
        }
        particleName: string = "BW_Chaos_Turret_BA_Tar"
        particlePath: string = "Data/Particles/BW_Chaos_Turret_BA_Tar"
        soundOnCreateDefault: string = "Play_sfx_Env_Map14_ChaosTurretMinionBasicAttack_cast"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_ChaosTurretChampionBasicAttack_missilelaunch"
    }
    0xc04038f8 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {
                    0.0500000007
                }
                emitterName: string = "misGeo2"
                importance: u8 = 2
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -78, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/BW_Chaos_Turret_Speedlines_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.368597001 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                isLocalOrientation: flag = false
                particleIsLocalOrientation: flag = true
                texture: string = "Data/Particles/BW_Chaos_Turret_SpeedLines.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "Data/Particles/BW_Chaos_Turret_SpeedLines_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1.5 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.0500000007
                }
                emitterName: string = "bullet2"
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "RocketTristana"
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/bw_chaos_turret_cannonball_mesh.scb"
                    }
                }
                blendMode: u8 = 3
                pass: i16 = 1
                isLocalOrientation: flag = false
                doesCastShadow: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -111, 1111 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, -111, 1111 }
                            { 0, -111, 1111 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_CannonBall.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.0500000007
                }
                isSingleParticle: flag = true
                emitterName: string = "HeatBall"
                disabled: bool = true
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "RocketTristana"
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/bw_chaos_turret_cannonball_mesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0, 0.380391985 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.325489998 }
                        }
                    }
                }
                pass: i16 = 2
                texture: string = "Data/Particles/BW_Chaos_CannonBall_heat.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 200
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[f32] = {
                            0.300000012
                            0.300000012
                            0.24000001
                            0.120000005
                            0.0900000036
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.379999995
                }
                emitterName: string = "BlurTrail"
                birthVelocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 1 }
                            { 0, 0, 0 }
                            { 0, 0, 0.5 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.349999994
                            0.600000024
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 0.411764711, 0.0901960805, 0 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.324117661 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.264411777 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.349999994, 0.200000003, 0.100000001, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 31, 1, 1 }
                }
                texture: string = "Data/Particles/BW_Chaos_BA_Mis_BlurTrail.dds"
                texDiv: vec2 = { 3, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 200
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[f32] = {
                            0.300000012
                            0.300000012
                            0.24000001
                            0.120000005
                            0.0900000036
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.379999995
                }
                emitterName: string = "BlurTrail1"
                birthVelocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 1 }
                            { 0, 0, 0 }
                            { 0, 0, 0.5 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.349999994
                            0.600000024
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 0.411764711, 0.0901960805, 0 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.324117661 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.264411777 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.349999994, 0.200000003, 0.100000001, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 31, 1, 1 }
                }
                texture: string = "Data/Particles/BW_Chaos_BA_Mis_BlurTrail.dds"
                texDiv: vec2 = { 3, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[f32] = {
                            0.400000006
                            0.400000006
                            0.319999993
                            0.159999996
                            0.119999997
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "SmokeTrail1"
                birthVelocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 1 }
                            { 0, 0, 0 }
                            { 0, 0, 0.5 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.349999994
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.524999976 }
                            { 1, 1, 1, 0.360000014 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.349999994, 0.200000003, 0.100000001, 0 }
                            { 1, 0.882353008, 0.866666973, 1 }
                            { 1, 0.752941012, 0.576470971, 1 }
                            { 0.988234997, 0.823529005, 0.619607985, 0 }
                        }
                    }
                }
                pass: i16 = 30
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 1, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                        }
                        values: list[vec3] = {
                            { 0, 1, 30 }
                            { 45, 1, 30 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.600000024, 1, 1 }
                            { 0.5, 1, 1 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_BA_Mis_SmokeTrail.dds"
                texDiv: vec2 = { 4, 1 }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[f32] = {
                            0.400000006
                            0.400000006
                            0.319999993
                            0.159999996
                            0.119999997
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "SmokeTrail2"
                birthVelocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 1 }
                            { 0, 0, 0 }
                            { 0, 0, 0.5 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.349999994
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.524999976 }
                            { 1, 1, 1, 0.360000014 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.349999994, 0.200000003, 0.100000001, 0 }
                            { 1, 0.882353008, 0.866666973, 1 }
                            { 1, 0.752941012, 0.576470971, 1 }
                            { 0.988234997, 0.823529005, 0.619607985, 0 }
                        }
                    }
                }
                pass: i16 = 30
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 1, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                        }
                        values: list[vec3] = {
                            { 0, 1, 30 }
                            { 45, 1, 30 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.600000024, 1, 1 }
                            { 0.5, 1, 1 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_BA_Mis_SmokeTrail.dds"
                texDiv: vec2 = { 4, 1 }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 35
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            105
                            0
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0.5
                            0.25
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    5
                }
                emitterName: string = "Sparks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 250, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -2
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -2
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 250, 50 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 10 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 2 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -10
                                        10
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -10
                                        10
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 2 }
                            }
                        }
                    }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 4
                colorLookUpTypeY: u8 = 3
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 20
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 40, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 40, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 1 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Sparks.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    0.699999988
                }
                emitterName: string = "trail2"
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1000
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.819607973, 0.0941179991, 0 }
                            { 1, 0.576470971, 0.0901959985, 0.972549021 }
                            { 1, 0.470587999, 0.164706007, 0.87450999 }
                            { 1, 0.831372976, 0.541176021, 0.200000003 }
                            { 1, 0.87450999, 0.768626988, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isLocalOrientation: flag = false
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_BA_Mis_SmokeTrail.dds"
                texDiv: vec2 = { 6, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.0500000007
                }
                emitterName: string = "bullet3"
                disabled: bool = true
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "RocketTristana"
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/BW_Chaos_Turret_Speedlines_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.368597001 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                doesCastShadow: flag = true
                texture: string = "Data/Particles/BW_Chaos_Turret_SpeedLines.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "Data/Particles/BW_Chaos_Turret_SpeedLines_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1.5 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 200
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[f32] = {
                            0.300000012
                            0.300000012
                            0.239999995
                            0.119999997
                            0.0900000036
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.379999995
                }
                emitterName: string = "BlurTrail"
                birthVelocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 1 }
                            { 0, 0, 0 }
                            { 0, 0, 0.5 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.349999994
                            0.600000024
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 0.411764711, 0.0901960805, 0 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.324117661 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.264411777 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.349999994, 0.200000003, 0.100000001, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 31, 1, 1 }
                }
                texture: string = "Data/Particles/BW_Chaos_BA_Mis_BlurTrail.dds"
                texDiv: vec2 = { 3, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 200
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[f32] = {
                            0.300000012
                            0.300000012
                            0.239999995
                            0.119999997
                            0.0900000036
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.379999995
                }
                emitterName: string = "BlurTrail1"
                birthVelocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 1 }
                            { 0, 0, 0 }
                            { 0, 0, 0.5 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 100, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.349999994
                            0.600000024
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 0.411764711, 0.0901960805, 0 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.34117648 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.324117661 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0.264411777 }
                            { 0.890196085, 0.411764711, 0.0901960805, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.349999994, 0.200000003, 0.100000001, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 31, 1, 1 }
                }
                texture: string = "Data/Particles/BW_Chaos_BA_Mis_BlurTrail.dds"
                texDiv: vec2 = { 3, 1 }
            }
        }
        particleName: string = "BW_Chaos_Turret_BA_Tar_Champ"
        particlePath: string = "Data/Particles/BW_Chaos_Turret_BA_Tar_Champ"
        soundOnCreateDefault: string = "Play_sfx_Env_Map14_ChaosTurretChampionBasicAttack_cast"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_ChaosTurretChampionBasicAttack_missilelaunch"
    }
    0x0443105f = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.400000006
                                    0.699999988
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "BoreSmoke_UpwardTrail"
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "FirefighterTristana"
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, -200, 40 }
                            { 0, -50, 20 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 2 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.733332992, 0.541176021, 0.376471013 }
                            { 0.713724971, 0.49019599, 0.305882007, 1 }
                            { 1, 0.952941, 0.882353008, 0.600000024 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 30, 0, 0 }
                            { 600, 300, 0 }
                        }
                    }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.79999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.79999995
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 70, 70, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 1 }
                            { 0.699999988, 0.699999988, 1 }
                            { 0.948176563, 0.948176563, 1 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Cas_Smoke_4x4.dds"
                numFrames: u16 = 16
                startFrame: u16 = 1
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.400000006
                                    0.600000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "BoreSmoke"
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "FirefighterTristana"
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 450 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, -200, 450 }
                            { 0, -50, 225 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 60, 2 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -15
                                        15
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -20
                                        20
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -55
                                        135
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.733332992, 0.541176021, 0.376471013 }
                            { 0.713724971, 0.49019599, 0.305882007, 1 }
                            { 1, 0.952941, 0.882353008, 0.600000024 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 30, 0, 0 }
                            { 600, 300, 0 }
                        }
                    }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.79999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.79999995
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 70, 70, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 1 }
                            { 0.699999988, 0.699999988, 1 }
                            { 0.948176563, 0.948176563, 1 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Cas_Smoke_4x4.dds"
                numFrames: u16 = 16
                startFrame: u16 = 1
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.400000006
                                    0.600000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "BoreSmoke1"
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "FirefighterTristana"
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 450 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, -200, 450 }
                            { 0, -50, 225 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 60, 2 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -15
                                        15
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -20
                                        20
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -55
                                        135
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.733332992, 0.541176021, 0.376471013 }
                            { 0.713724971, 0.49019599, 0.305882007, 1 }
                            { 1, 0.952941, 0.882353008, 0.600000024 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 30, 0, 0 }
                            { 600, 300, 0 }
                        }
                    }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.79999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.79999995
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 70, 70, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 1 }
                            { 0.699999988, 0.699999988, 1 }
                            { 0.948176563, 0.948176563, 1 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Cas_Smoke_4x4.dds"
                numFrames: u16 = 16
                startFrame: u16 = 1
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLinger: option[f32] = {
                    10.1000004
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "FlashCap_Mesh"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 10, 10 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/bw_chaos_turret_cas_flashcap_mesh.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.501960814 }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 360 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 4.5, 8 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 4.19999981, 3.1500001, 5.5999999 }
                            { 7.80000019, 5.8499999, 10.3999996 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 3 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Cas_FlashCap_Mesh_2x2.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                particleLinger: option[f32] = {
                    0.100000001
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "GlowFlash"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 50 }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.329411775, 0.0666666701, 0.56078434 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.112545997
                            0.449999988
                            0.998000026
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 0 }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Cas_glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                particleLinger: option[f32] = {
                    0.100000001
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "GlowFlash1"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 50 }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.329411775, 0.0666666701, 0.56078434 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.112545997
                            0.449999988
                            0.998000026
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 0 }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_Cas_glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLinger: option[f32] = {
                    10.1000004
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Flash_Mesh"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 10, 10 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/bw_chaos_turret_cas_flash_mesh.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.501960814 }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4.0999999, 1, 1.5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -0.699999988
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 2.86999989, 0.699999988, 1.04999995 }
                            { 4.0999999, 1, 1.5 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 3 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Chaos_Turret_cas_Flash_Mesh_4x1.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.25
                                    0.300000012
                                    0.5
                                    0.5
                                    0.800000012
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    0.300000012
                                    0.300000012
                                    0.5
                                    0.5
                                    0.800000012
                                    0.800000012
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
        }
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.0399999991
                }
                emitterName: string = "Flash"
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "FirefighterTristana"
                    }
                }
                particleColorTexture: string = "Data/Particles/color-rampdown.dds"
                blendMode: u8 = 4
                meshRenderFlags: u8 = 0
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.501960814 }
                }
                isRandomStartFrame: flag = true
                texture: string = "Data/Particles/BW_Chaos_Turret_Cas_FlashCap_Mesh_2x2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                0xbc022424: pointer = 0x7f70a2b2 {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 65
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        3
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[f32] = {
                                65
                            }
                        }
                    }
                    birthRotation: embed = ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        360
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[f32] = {
                                1
                            }
                        }
                    }
                    particleBind: vec2 = { 1, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.400000006
                                    0.699999988
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "Sparks"
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "FirefighterTristana"
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 0, 300 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 250, 0, 300 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 30, 30 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 30, 30, 30 }
                            }
                        }
                    }
                }
                particleColorTexture: string = "Data/Particles/color-addflame.dds"
                meshRenderFlags: u8 = 0
                colorLookUpScales: vec2 = { 1, 0.600000024 }
                texture: string = "Data/Particles/BW_Chaos_Turret_Sparkels.dds"
                startFrame: u16 = 4
                texDiv: vec2 = { 2, 3 }
                0xbc022424: pointer = 0x7f70a2b2 {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 3
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        2
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[f32] = {
                                3
                            }
                        }
                    }
                    scale: embed = ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.899999976
                                1
                            }
                            values: list[f32] = {
                                1
                                1
                                0
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "Data/Particles/BW_Chaos_Turret_BA_Cast"
        particlePath: string = "Data/Particles/BW_Chaos_Turret_BA_Cast"
    }
    0x0506bf3a = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.600000024
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "Smoke1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, -400, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, -400, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 4, 4 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 110, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 110, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 4, 0, 4 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec3] = {
                                { 4, 0, 4 }
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 1
                colorLookUpTypeY: u8 = 3
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.588235319 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.650979996, 0.254902005, 1 }
                            { 0.701960981, 0.411765009, 0.0784310028, 1 }
                            { 0.745097995, 0.396077991, 0.278430998, 1 }
                            { 0.215685993, 0.156863004, 0.301961005, 0.666666985 }
                            { 0.0980390012, 0.0784310028, 0.415686011, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 90 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -0.5
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                    1.79999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 70, 70, 0 }
                            { 14, 14, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0, 0 }
                            { 1, 1, 0 }
                            { 1.10000002, 1.10000002, 1 }
                            { 1.10000002, 1.10000002, 1 }
                            { 1, 1, 1 }
                            { 0.600000024, 0.600000024, 0 }
                        }
                    }
                }
                texture: string = "Data/Particles/BW_Turret_Smoke_Tar.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "BW_Chaos_Turret_Tar_CPart_Champ"
        particlePath: string = "Data/Particles/BW_Chaos_Turret_Tar_CPart_Champ"
        flags: u16 = 198
    }
}
