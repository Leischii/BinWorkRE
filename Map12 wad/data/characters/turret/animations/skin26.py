#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Turret/Animations/Skin26" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Attack1_0" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Attack1.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xb4b80421 = ParticleEventData {
                        mEffectName: string = "BW_Chaos_Turret_BA_Cast.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x7a76b4ae
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mIsDetachable: bool = true
                    }
                    0x64696ddb = ParticleEventData {
                        mEffectKey: hash = 0xc04038f8
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x7a76b4ae
                            }
                        }
                        mStartFrame: f32 = 4
                    }
                }
            }
            "Idle1" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Idle1.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xa62fdb34 = SoundEventData {
                        mSoundName: string = "Play_sfx_Env_Map14_ChaosTurretChampionBasicAttack_idle"
                        mIsLoop: bool = false
                        mName: hash = 0xa62fdb34
                    }
                }
                mFlags: u32 = 2
            }
            0xcc2030a0 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Idle1.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break1" = ParticleEventData {
                        mEffectName: string = "bw_chaos_turret_idledmg_01.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x30ce08c5
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mFlags: u32 = 8
            }
            0xf5c65fef = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Idle1.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break2" = ParticleEventData {
                        mEffectName: string = "bw_chaos_turret_idledmg_02.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x30ce08c5
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mFlags: u32 = 8
            }
            "Attack1_180" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Attack1_180.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x64696ddb = ParticleEventData {
                        mEffectKey: hash = 0xc04038f8
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x7a76b4ae
                            }
                        }
                        mStartFrame: f32 = 4
                    }
                }
            }
            "Attack1_-180" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Attack1_-180.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x64696ddb = ParticleEventData {
                        mEffectKey: hash = 0xc04038f8
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x7a76b4ae
                            }
                        }
                        mStartFrame: f32 = 4
                    }
                }
            }
            0xef96b4dc = ParametricClipData {
                Updater: pointer = 0x41356ce8 {}
                mParametricPairDataList: list[embed] = {
                    ParametricPairData {
                        mClipName: hash = "Attack1_-180"
                        mValue: f32 = -180
                    }
                    ParametricPairData {
                        mClipName: hash = "Attack1_0"
                    }
                    ParametricPairData {
                        mClipName: hash = "Attack1_180"
                        mValue: f32 = 180
                    }
                }
                mTrackDataName: hash = "Default"
            }
            "Respawn" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x3c4a5fc6 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "TurretBase"
                        }
                        mName: hash = 0x3c4a5fc6
                    }
                    0xc39eccf0 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            0x13e8225f
                            0x2da42ecb
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Idle1.anm"
                }
            }
            "Destroyed" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Idle1.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideTurret" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "TurretBase"
                        }
                        mName: hash = "HideTurret"
                    }
                    0x07030a82 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 80
                        mShowSubmeshList: list[hash] = {
                            0x13e8225f
                            0x2da42ecb
                        }
                    }
                    "Smoke" = ParticleEventData {
                        mName: hash = "Smoke"
                        mEffectName: string = "BW_Turret_Rubble_Dust.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "root"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mFlags: u32 = 2
            }
            "death" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_ChaosTurret_explode1.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideTurret" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "TurretBase"
                        }
                        mName: hash = "HideTurret"
                    }
                    "BREAK" = ParticleEventData {
                        mEffectKey: hash = 0x827fcadc
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "root"
                            }
                        }
                        mIsLoop: bool = false
                        mIsDetachable: bool = true
                        mName: hash = "BREAK"
                    }
                    0x07030a82 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 80
                        mShowSubmeshList: list[hash] = {
                            0x13e8225f
                            0x2da42ecb
                        }
                    }
                    "Smoke" = ParticleEventData {
                        mName: hash = "Smoke"
                        mEffectName: string = "BW_Turret_Rubble_Dust.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "root"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mFlags: u32 = 8
            }
            0x502619a4 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_ChaosTurret_explode1.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideTurret" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "TurretBase"
                        }
                        mName: hash = "HideTurret"
                    }
                    "BREAK" = ParticleEventData {
                        mEffectKey: hash = 0x827fcadc
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "root"
                            }
                        }
                        mIsLoop: bool = false
                        mIsDetachable: bool = true
                        mName: hash = "BREAK"
                    }
                    0x07030a82 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 80
                        mShowSubmeshList: list[hash] = {
                            0x13e8225f
                            0x2da42ecb
                        }
                    }
                    "Smoke" = ParticleEventData {
                        mName: hash = "Smoke"
                        mEffectName: string = "BW_Turret_Rubble_Dust.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "root"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mFlags: u32 = 8
            }
            "Attack1_Min" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Attack1_min.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x64696ddb = ParticleEventData {
                        mEffectKey: hash = 0xc04038f8
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x7a76b4ae
                            }
                        }
                        mStartFrame: f32 = 4
                    }
                }
            }
            "Attack1_Min_180" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Attack1_min_180.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x64696ddb = ParticleEventData {
                        mEffectKey: hash = 0xc04038f8
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x7a76b4ae
                            }
                        }
                        mStartFrame: f32 = 4
                    }
                }
            }
            "Attack1_Min_-180" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Attack1_min_-180.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x64696ddb = ParticleEventData {
                        mEffectKey: hash = 0xc04038f8
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x7a76b4ae
                            }
                        }
                        mStartFrame: f32 = 4
                    }
                }
            }
            0x1fd7d087 = ParametricClipData {
                Updater: pointer = 0x41356ce8 {}
                mParametricPairDataList: list[embed] = {
                    ParametricPairData {
                        mClipName: hash = "Attack1_Min_-180"
                        mValue: f32 = -180
                    }
                    ParametricPairData {
                        mClipName: hash = "Attack1_Min"
                    }
                    ParametricPairData {
                        mClipName: hash = "Attack1_Min_180"
                        mValue: f32 = 180
                    }
                }
                mTrackDataName: hash = "Default"
            }
            "Attack1" = ParametricClipData {
                Updater: pointer = 0x0cf99c50 {}
                mParametricPairDataList: list[embed] = {
                    ParametricPairData {
                        mClipName: hash = 0x1fd7d087
                        mValue: f32 = 150
                    }
                    ParametricPairData {
                        mClipName: hash = 0xef96b4dc
                        mValue: f32 = 600
                    }
                }
                mTrackDataName: hash = "Default"
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Default" = TrackData {}
            "attack" = TrackData {
                mPriority: u8 = 1
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            6715790923503192131 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11374364253792454723 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
        }
    }
}
