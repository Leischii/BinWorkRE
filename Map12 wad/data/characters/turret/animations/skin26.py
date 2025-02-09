#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Turret/Animations/Skin26" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Attack1_0" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xa446cc48 = ParticleEventData {
                        mName: hash = 0xa446cc48
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
                    0x64b968b7 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            0x13e8225f
                            0x2da42ecb
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Attack1.anm"
                }
            }
            "Idle1" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xa62fdb34 = SoundEventData {
                        mName: hash = 0xa62fdb34
                        mSoundName: string = "Play_sfx_Env_Map14_ChaosTurretChampionBasicAttack_idle"
                        mIsLoop: bool = false
                    }
                    0x64b968b7 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            0x13e8225f
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Idle1.anm"
                }
            }
            "Attack1_180" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xa446cc48 = ParticleEventData {
                        mName: hash = 0xa446cc48
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
                    0x64b968b7 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            0x13e8225f
                            0x2da42ecb
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Attack1_180.anm"
                }
            }
            "Attack1_-180" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xa446cc48 = ParticleEventData {
                        mName: hash = 0xa446cc48
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
                    0x64b968b7 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            0x13e8225f
                            0x2da42ecb
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Attack1_-180.anm"
                }
            }
            0xef96b4dc = ParametricClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x64b968b7 = SubmeshVisibilityEventData {
                        mHideSubmeshList: list[hash] = {
                            0x13e8225f
                            0x2da42ecb
                        }
                    }
                }
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
            "Destroyed" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideTurret" = SubmeshVisibilityEventData {
                        mName: hash = "HideTurret"
                        mHideSubmeshList: list[hash] = {
                            "TurretBase"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_ChaosTurret_explode1.anm"
                }
            }
            "death" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideTurret" = SubmeshVisibilityEventData {
                        mName: hash = "HideTurret"
                        mHideSubmeshList: list[hash] = {
                            "TurretBase"
                            0x13e8225f
                            0x2da42ecb
                        }
                    }
                    "BREAK" = ParticleEventData {
                        mName: hash = "BREAK"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "root"
                            }
                        }
                        mIsLoop: bool = false
                        mIsDetachable: bool = true
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_ChaosTurret_explode1.anm"
                }
            }
            "Attack1_Min" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Attack1_min.anm"
                }
            }
            "Attack1_Min_180" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Attack1_min_180.anm"
                }
            }
            "Attack1_Min_-180" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin26/Animations/BW_AP_ChaosTurret_Attack1_min_-180.anm"
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
                        mClipName: hash = "Attack1_Min"
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
                        mValue: f32 = 150
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
