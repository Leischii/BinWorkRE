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
                        mMeshName: string = "ASSETS/Characters/HA_AP_OrderTurret/Skins/Skin05/Particles/HA_BW_OrderTurret.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/HA_AP_OrderTurret/Skins/Skin05/Particles/HA_BW_OrderTurret.skl"
                        mAnimationName: string = "ASSETS/Characters/HA_AP_OrderTurret/Skins/Skin05/Particles/HA_BW_OrderTurret_Explode1.anm"
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
    0x26cea5b9 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
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
                            0.300000012
                        }
                    }
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Sparks_Blue"
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
                            { 1, 1, 1, 0.345097989 }
                        }
                    }
                }
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
                texture: string = "Data/Particles/BW_Order_Turret_Sparks_4x1.dds"
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
                pass: i16 = 77
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
                texture: string = "Data/Particles/BW_Order_Turret_Explosion_Flat_Tar.dds"
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
                    constantValue: vec4 = { 0.5, 0.400000006, 0.899999976, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.800000012, 1.79999995, 1 }
                            { 0.5, 0.400000006, 0.899999976, 1 }
                            { 0.5, 0.400000006, 0.899999976, 0.792203009 }
                            { 0.25, 0.200000003, 0.449999988, 0 }
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
                    constantValue: f32 = 0.150000006
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
                    emitOffset: vec3 = { 0, 40, 0 }
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
                            { 1, 1, 0, 1 }
                            { 1, 0.607842982, 0.380391985, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 150, 0 }
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
                emitterName: string = "White_GlowFlash2"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 40, 0 }
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
                            { 1, 1, 0, 1 }
                            { 1, 0.607842982, 0.380391985, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 150, 0 }
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
                            { 0.603922009, 0.203922004, 1, 0.26039201 }
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
                    constantValue: vec3 = { 150, 150, 0 }
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
                            { 150, 150, 0 }
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
                texture: string = "Data/Particles/BW_Order_Turret_Explosion_Flat_Tar.dds"
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
                            { 0.984314024, 1, 0, 0 }
                            { 1, 0.666666985, 0, 1 }
                            { 0.168626994, 0.93333298, 1, 0 }
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
                texture: string = "Data/Particles/BW_Order_flashCore.dds"
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
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 6, 0 }
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
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
                texture: string = "Data/Particles/BW_Order_Turret_Cas_FlashCap_Mesh_2x2.dds"
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
        particleName: string = "bw_order_turret_fire_tar"
        particlePath: string = "Data/Particles/bw_order_turret_fire_tar"
        soundOnCreateDefault: string = "Play_sfx_Env_Map14_OrderTurretChampionBasicAttack_hit"
    }
    0x015b9de5 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.150000006
                }
                emitterName: string = "misGeo2"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/BW_Order_Turret_Bullet_Mis.scb"
                    }
                }
                blendMode: u8 = 3
                isLocalOrientation: flag = false
                particleIsLocalOrientation: flag = true
                doesCastShadow: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 311, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.800000012, 0.800000012, 0.800000012 }
                }
                texture: string = "Data/Particles/BW_Order_Turret_Bullet_Mis.dds"
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
                emitterName: string = "misGeo3"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -38, 0 }
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
                isLocalOrientation: flag = false
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.300000012, 0.899999976, 1 }
                }
                texture: string = "Data/Particles/BW_Order_Turret_SpeedLines.dds"
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
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.579999983
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
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.34117648 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.00784299988, 1, 0.937255025, 1 }
                            { 0.733332992, 0.200000003, 1, 1 }
                            { 1, 0.419607997, 0.188235, 1 }
                            { 0.745097995, 0, 0.0117650004, 0 }
                        }
                    }
                }
                pass: i16 = 3
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 31, 1, 1 }
                }
                texture: string = "Data/Particles/BW_Chaos_BA_Mis_BlurTrail.dds"
                texDiv: vec2 = { 3, 1 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.579999983
                }
                emitterName: string = "BlurTrail2"
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
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.34117648 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.00784299988, 1, 0.937255025, 1 }
                            { 0.733332992, 0.200000003, 1, 1 }
                            { 1, 0.419607997, 0.188235, 1 }
                            { 0.745097995, 0, 0.0117650004, 0 }
                        }
                    }
                }
                pass: i16 = 3
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
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.290196002, 1, 1, 1 }
                            { 1, 0.541176021, 0.447059005, 1 }
                            { 0.945097983, 0.521569014, 1, 1 }
                            { 0.76078397, 0.321568996, 0.835294008, 0.160784006 }
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
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.290196002, 1, 1, 1 }
                            { 1, 0.541176021, 0.447059005, 1 }
                            { 0.945097983, 0.521569014, 1, 1 }
                            { 0.76078397, 0.321568996, 0.835294008, 0.160784006 }
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
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 10 }
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
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.00784299988, 1, 0.937255025, 1 }
                            { 1, 0.419607997, 0.188235, 1 }
                            { 0.733332992, 0.200000003, 1, 1 }
                            { 0.0470589995, 0.952941, 1, 1 }
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
                texture: string = "Data/Particles/BW_Order_Turret_Sparks.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.200000003
                            0.25
                            1
                        }
                        values: list[vec4] = {
                            { 0.00784299988, 1, 0.937255025, 1 }
                            { 1, 0.419607997, 0.188235, 0.87450999 }
                            { 0.431373, 0.235293999, 0.498039007, 0.964706004 }
                            { 0.313724995, 0.196078002, 0.384314001, 0 }
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
        }
        particleName: string = "bw_order_turret_fire_mis"
        particlePath: string = "Data/Particles/bw_order_turret_fire_mis"
        soundOnCreateDefault: string = "Play_sfx_Env_Map14_OrderTurretMinionBasicAttack_cast"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_OrderTurretChampionBasicAttack_missilelaunch"
    }
    0x5aa19f81 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.150000006
                }
                emitterName: string = "misGeo2"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Data/Particles/BW_Order_Turret_Bullet_Mis.scb"
                    }
                }
                blendMode: u8 = 3
                isLocalOrientation: flag = false
                particleIsLocalOrientation: flag = true
                doesCastShadow: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 311, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.800000012, 0.800000012, 0.800000012 }
                }
                texture: string = "Data/Particles/BW_Order_Turret_Bullet_Mis.dds"
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
                emitterName: string = "misGeo3"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -38, 0 }
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
                isLocalOrientation: flag = false
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.300000012, 0.899999976, 1 }
                }
                texture: string = "Data/Particles/BW_Order_Turret_SpeedLines.dds"
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
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.579999983
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
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.34117648 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.00784299988, 1, 0.937255025, 1 }
                            { 0.733332992, 0.200000003, 1, 1 }
                            { 1, 0.419607997, 0.188235, 1 }
                            { 0.745097995, 0, 0.0117650004, 0 }
                        }
                    }
                }
                pass: i16 = 3
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 31, 1, 1 }
                }
                texture: string = "Data/Particles/BW_Chaos_BA_Mis_BlurTrail.dds"
                texDiv: vec2 = { 3, 1 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.579999983
                }
                emitterName: string = "BlurTrail2"
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
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.34117648 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.00784299988, 1, 0.937255025, 1 }
                            { 0.733332992, 0.200000003, 1, 1 }
                            { 1, 0.419607997, 0.188235, 1 }
                            { 0.745097995, 0, 0.0117650004, 0 }
                        }
                    }
                }
                pass: i16 = 3
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
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.290196002, 1, 1, 1 }
                            { 1, 0.541176021, 0.447059005, 1 }
                            { 0.945097983, 0.521569014, 1, 1 }
                            { 0.76078397, 0.321568996, 0.835294008, 0.160784006 }
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
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.290196002, 1, 1, 1 }
                            { 1, 0.541176021, 0.447059005, 1 }
                            { 0.945097983, 0.521569014, 1, 1 }
                            { 0.76078397, 0.321568996, 0.835294008, 0.160784006 }
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
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 10 }
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
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.00784299988, 1, 0.937255025, 1 }
                            { 1, 0.419607997, 0.188235, 1 }
                            { 0.733332992, 0.200000003, 1, 1 }
                            { 0.0470589995, 0.952941, 1, 1 }
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
                texture: string = "Data/Particles/BW_Order_Turret_Sparks.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.200000003
                            0.25
                            1
                        }
                        values: list[vec4] = {
                            { 0.00784299988, 1, 0.937255025, 1 }
                            { 1, 0.419607997, 0.188235, 0.87450999 }
                            { 0.431373, 0.235293999, 0.498039007, 0.964706004 }
                            { 0.313724995, 0.196078002, 0.384314001, 0 }
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
        }
        particleName: string = "BW_Order_Turret_Fire_Mis_Champ"
        particlePath: string = "Data/Particles/BW_Order_Turret_Fire_Mis_Champ"
        soundOnCreateDefault: string = "Play_sfx_Env_Map14_OrderTurretChampionBasicAttack_cast"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_OrderTurretChampionBasicAttack_missilelaunch"
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
