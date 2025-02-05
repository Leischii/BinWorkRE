#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Turret/Animations/Skin24" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Attack1_0" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Attack1.anm"
                }
                mTrackDataName: hash = "Default"
            }
            "Idle1" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x2ca7d83e = SoundEventData {
                        mSoundName: string = "Play_sfx_Env_Map14_OrderTurretChampionBasicAttack_idle"
                        mName: hash = 0x2ca7d83e
                    }
                    0x2ba7d6ab = SoundEventData {
                        mSoundName: string = "Play_sfx_Env_Map14_OrderTurretChampionBasicAttack_idle"
                        mName: hash = 0x2ba7d6ab
                        mStartFrame: f32 = 110
                    }
                }
                mFlags: u32 = 2
            }
            0xcc2030a0 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break1" = ParticleEventData {
                        mEffectName: string = "bw_order_turret_idle.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x12c9c116
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
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break2" = ParticleEventData {
                        mEffectName: string = "bw_order_turret_idle2.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xe3da48b0
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mFlags: u32 = 8
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
            "Attack1_180" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Attack1_180.anm"
                }
                mTrackDataName: hash = "Default"
            }
            "Attack1_-180" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Attack1_-180.anm"
                }
                mTrackDataName: hash = "Default"
            }
            "Respawn" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x3c4a5fc6 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "lambert7"
                        }
                        mName: hash = 0x3c4a5fc6
                    }
                    0xc39eccf0 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            0x13e8225f
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Idle.anm"
                }
            }
            "Destroyed" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideTurret" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "lambert7"
                        }
                        mName: hash = "HideTurret"
                    }
                    0x07030a82 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 80
                        mShowSubmeshList: list[hash] = {
                            0x13e8225f
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
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_OrderTurret_Explode1.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideTurret" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "lambert7"
                        }
                        mName: hash = "HideTurret"
                    }
                    0x07030a82 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 80
                        mShowSubmeshList: list[hash] = {
                            0x13e8225f
                        }
                    }
                    "BREAK" = ParticleEventData {
                        mEffectKey: hash = 0xc18ea1e3
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "root"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mName: hash = "BREAK"
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
            0x5fe86160 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_OrderTurret_Explode1.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideTurret" = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            "lambert7"
                        }
                        mName: hash = "HideTurret"
                    }
                    0x07030a82 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 80
                        mShowSubmeshList: list[hash] = {
                            0x13e8225f
                        }
                    }
                    "BREAK" = ParticleEventData {
                        mEffectKey: hash = 0xc18ea1e3
                        mEnemyEffectKey: hash = 0xc18ea1e3
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "root"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mName: hash = "BREAK"
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
            0xeb61a374 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Attack1_min.anm"
                }
                mTrackDataName: hash = "Default"
            }
            "Attack1_Min_180" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Attack1_min_180.anm"
                }
                mTrackDataName: hash = "Default"
            }
            "Attack1_Min_-180" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Attack1_min_-180.anm"
                }
                mTrackDataName: hash = "Default"
            }
            0x1fd7d087 = ParametricClipData {
                Updater: pointer = 0x41356ce8 {}
                mParametricPairDataList: list[embed] = {
                    ParametricPairData {
                        mClipName: hash = "Attack1_Min_-180"
                        mValue: f32 = -180
                    }
                    ParametricPairData {
                        mClipName: hash = 0xeb61a374
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
                        mValue: f32 = 200
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
