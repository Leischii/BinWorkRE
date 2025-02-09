#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Turret/Animations/Skin24" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Attack1_0" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Attack1.anm"
                }
            }
            "Idle1" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x2ca7d83e = SoundEventData {
                        mName: hash = 0x2ca7d83e
                        mSoundName: string = "Play_sfx_Env_Map14_OrderTurretChampionBasicAttack_idle"
                    }
                    0x2ba7d6ab = SoundEventData {
                        mName: hash = 0x2ba7d6ab
                        mStartFrame: f32 = 110
                        mSoundName: string = "Play_sfx_Env_Map14_OrderTurretChampionBasicAttack_idle"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Idle.anm"
                }
            }
            0xef96b4dc = ParametricClipData {
                mTrackDataName: hash = "Default"
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
            }
            "Attack1_180" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Attack1_180.anm"
                }
            }
            "Attack1_-180" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Attack1_-180.anm"
                }
            }
            "Destroyed" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x07030a82 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            0x13e8225f
                        }
                        mHideSubmeshList: list[hash] = {
                            "lambert7"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Idle.anm"
                }
            }
            "death" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideTurret" = SubmeshVisibilityEventData {
                        mName: hash = "HideTurret"
                        mHideSubmeshList: list[hash] = {
                            "lambert7"
                            0x13e8225f
                        }
                    }
                    "BREAK" = ParticleEventData {
                        mName: hash = "BREAK"
                        mEffectKey: hash = 0xc18ea1e3
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "root"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x07030a82 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 100
                        mHideSubmeshList: list[hash] = {
                            0x13e8225f
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_OrderTurret_Explode1.anm"
                }
            }
            0xeb61a374 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Attack1_min.anm"
                }
            }
            "Attack1_Min_180" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Attack1_min_180.anm"
                }
            }
            "Attack1_Min_-180" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin24/Animations/BW_AP_OrderTurret_Attack1_min_-180.anm"
                }
            }
            0x1fd7d087 = ParametricClipData {
                mTrackDataName: hash = "Default"
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
            }
            "Attack1" = ParametricClipData {
                mTrackDataName: hash = "Default"
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
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Default" = TrackData {}
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
