#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Inhibitor/Animations/Skin24" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Death_Base" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "submesh" = SubmeshVisibilityEventData {
                        mName: hash = "submesh"
                        mShowSubmeshList: list[hash] = {
                            "Destroyed"
                        }
                        mHideSubmeshList: list[hash] = {
                            "inhib"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin22/Animations/HA_OrderInhib_death.anm"
                }
            }
            0x41fd684f = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "base"
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xbd5d7a8f = SoundEventData {
                        mName: hash = 0xbd5d7a8f
                        mSoundName: string = "Play_sfx_Env_map14_order_inhibitor_alive_loop"
                    }
                    0x14dbe152 = ParticleEventData {
                        mName: hash = 0x14dbe152
                        mEffectName: string = "BW_AP_Order_Inhib_Idle.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xc5edc656
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/Animations/BW_AP_OrderInhibitor_Idle.anm"
                }
            }
            "Attack1" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/Animations/BW_AP_OrderInhibitor_Idle.anm"
                }
            }
            "Idle_Hold" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/Animations/BW_AP_OrderInhibitor_Idle.anm"
                }
            }
            "Respawn" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0xa33449ff
                    0x41fd684f
                }
            }
            0x14f21665 = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Respawn"
                mEventDataMap: map[hash,pointer] = {
                    "Flash" = ParticleEventData {
                        mName: hash = "Flash"
                        mEffectName: string = "HA_Order_Inhibitor_Respawn.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x95dabe4f
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mIsDetachable: bool = true
                    }
                    "submesh" = SubmeshVisibilityEventData {
                        mName: hash = "submesh"
                        mStartFrame: f32 = 300
                        mShowSubmeshList: list[hash] = {
                            "inhib"
                        }
                        mHideSubmeshList: list[hash] = {
                            "Destroyed"
                        }
                    }
                    "audio_respawn" = SoundEventData {
                        mName: hash = "audio_respawn"
                        mStartFrame: f32 = 75
                        mSoundName: string = "Play_sfx_Env_Map14_order_inhibitor_respawn_cast"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin22/Animations/HA_OrderInhib_respawn.anm"
                }
            }
            "Spawn" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0x14f21665
                }
            }
            0xe4cb0f58 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin24/Animations/BW_AP_OrderInhibitor_Idle.anm"
                }
            }
            "death" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Death_Base"
                    0xc3247102
                }
            }
            0xc3247102 = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.200000003
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin22/Animations/HA_OrderInhib_idle_dead.anm"
                }
            }
            "Idle1" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Idle_Hold"
                    0xe4cb0f58
                    0x41fd684f
                }
            }
            0xa33449ff = ParallelClipData {
                mClipNameList: list[hash] = {
                    0x14f21665
                    0x41fd684f
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
            "base" = MaskData {
                mWeightList: list[f32] = {
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Default" = TrackData {}
            "Respawn" = TrackData {
                mPriority: u8 = 1
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            1509293451443990786 = TimeBlendData {
                mTime: f32 = 0
            }
            4755071473358762242 = TimeBlendData {
                mTime: f32 = 0
            }
            4755071474068659579 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030502951525755 = TimeBlendData {
                mTime: f32 = 0
            }
            7075563044061081858 = TimeBlendData {
                mTime: f32 = 0
            }
            7075563044770979195 = TimeBlendData {
                mTime: f32 = 0
            }
            14061488190312814181 = TimeBlendData {
                mTime: f32 = 0
            }
            14061488191068530767 = TimeBlendData {
                mTime: f32 = 0
            }
            14061488191608812313 = TimeBlendData {
                mTime: f32 = 0
            }
            14061488193235349762 = TimeBlendData {
                mTime: f32 = 0
            }
            14061488193799917400 = TimeBlendData {
                mTime: f32 = 0
            }
            14061488193945247099 = TimeBlendData {
                mTime: f32 = 0
            }
            17110474037001021519 = TimeBlendData {
                mTime: f32 = 0
            }
            17110474037541303065 = TimeBlendData {
                mTime: f32 = 0
            }
            17110474039167840514 = TimeBlendData {
                mTime: f32 = 0
            }
            17110474039877737851 = TimeBlendData {
                mTime: f32 = 0
            }
        }
    }
}
