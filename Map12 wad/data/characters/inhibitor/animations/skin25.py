#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    0x87ed6d07 = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Idle_Normal1" = AtomicClipData {
                mTickDuration: f32 = 0.333333343
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin25/Animations/SRUAP_ChaosInhibitor_idle_normal.anm"
                }
                mMaskDataName: hash = "base"
                mTrackDataName: hash = "Default"
                mFlags: u32 = 2
            }
            "Death_Base" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin25/Animations/SRUAP_ChaosInhibitor_death.anm"
                }
                mMaskDataName: hash = "Destroyed"
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "submesh" = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Destroyed"
                        }
                        mHideSubmeshList: list[hash] = {
                            "inhib"
                        }
                        mName: hash = "submesh"
                    }
                }
                mFlags: u32 = 8
            }
            0xe4cb0f58 = AtomicClipData {
                mTickDuration: f32 = 0.25
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin25/Animations/SRUAP_ChaosInhibitor_spawn.anm"
                }
                mMaskDataName: hash = "base"
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Spawn" = ParticleEventData {
                        mEffectName: string = "SRUAP_Chaos_Inhibitor_Spawn_sound.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsKillEvent: bool = false
                        mName: hash = "Audio_Spawn"
                    }
                    "Activate" = ParticleEventData {
                        mEffectName: string = "SRUAP_Chaos_Inhibitor_Activation_flash.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x95dabe4f
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mIsDetachable: bool = true
                        mName: hash = "Activate"
                        mStartFrame: f32 = 28
                    }
                }
                mFlags: u32 = 8
            }
            "Spawn" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0xe4cb0f58
                }
            }
            "Idle1" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Idle_Hold"
                    0xe4cb0f58
                    0x78a49bc0
                }
                mEventDataMap: map[hash,pointer] = {
                    0xbd5d7a8f = SoundEventData {
                        mSoundName: string = "Play_sfx_Env_map14_chaos_inhibitor_alive_loop"
                        mName: hash = 0xbd5d7a8f
                    }
                }
            }
            0xc3247102 = AtomicClipData {
                mTickDuration: f32 = 0.333333373
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin25/Animations/sruap_chaosinhibitor_idle_death.anm"
                }
                mMaskDataName: hash = "Destroyed"
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xa619546b = SoundEventData {
                        mSoundName: string = "Play_sfx_Env_Map14_chaos_inhibitor_dead_loop"
                        mName: hash = 0xa619546b
                    }
                }
                mFlags: u32 = 2
            }
            "death" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Death_Base"
                    0xc3247102
                }
            }
            "Idle_Hold" = AtomicClipData {
                mTickDuration: f32 = 0.333333373
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin25/Animations/sruap_chaosinhibitor_idle_hold.anm"
                }
                mMaskDataName: hash = "base"
                mTrackDataName: hash = "Default"
            }
            0x14f21665 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin25/Animations/sruap_chaosinhibitor_respawn.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "submesh" = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "inhib"
                        }
                        mHideSubmeshList: list[hash] = {
                            "Destroyed"
                        }
                        mName: hash = "submesh"
                        mStartFrame: f32 = 295
                    }
                    "Vfx" = ParticleEventData {
                        mEffectName: string = "SRUAP_Chaos_Inhibitor_Respawn.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x95dabe4f
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mIsDetachable: bool = true
                        mName: hash = "Vfx"
                    }
                    0x5492cec6 = SoundEventData {
                        mSoundName: string = "Play_sfx_Env_Map14_chaos_inhibitor_respawn_cast"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mName: hash = 0x5492cec6
                        mStartFrame: f32 = 2
                    }
                }
                mFlags: u32 = 4
            }
            "Idle_Normal2" = AtomicClipData {
                mTickDuration: f32 = 0.333333343
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin25/Animations/sruap_chaosinhibitor_idle_normal2.anm"
                }
                mEventDataMap: map[hash,pointer] = {
                    0xbd5d7a8f = SoundEventData {
                        mSoundName: string = "Play_sfx_Env_map14_chaos_inhibitor_alive_loop"
                        mName: hash = 0xbd5d7a8f
                    }
                }
                mMaskDataName: hash = "base"
                mTrackDataName: hash = "Default"
            }
            "Idle_Normal3" = AtomicClipData {
                mTickDuration: f32 = 0.333333343
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Inhibitor/Skins/Skin25/Animations/sruap_chaosinhibitor_idle_normal3.anm"
                }
                mEventDataMap: map[hash,pointer] = {
                    0xbd5d7a8f = SoundEventData {
                        mSoundName: string = "Play_sfx_Env_map14_chaos_inhibitor_alive_loop"
                        mName: hash = 0xbd5d7a8f
                    }
                }
                mMaskDataName: hash = "base"
                mTrackDataName: hash = "Default"
            }
            0x78a49bc0 = SelectorClipData {
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = "Idle_Normal1"
                        mProbability: f32 = 60
                    }
                    SelectorPairData {
                        mClipName: hash = "Idle_Normal2"
                        mProbability: f32 = 20
                    }
                    SelectorPairData {
                        mClipName: hash = "Idle_Normal3"
                        mProbability: f32 = 20
                    }
                }
                mFlags: u32 = 2
            }
            "Respawn" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0x14f21665
                    0x78a49bc0
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
            1509293449560356796 = TimeBlendData {
                mTime: f32 = 0
            }
            1509293449577134415 = TimeBlendData {
                mTime: f32 = 0
            }
            1509293449593912034 = TimeBlendData {
                mTime: f32 = 0
            }
            4188995922622193019 = TimeBlendData {
                mTime: f32 = 0
            }
            5971341806667724732 = TimeBlendData {
                mTime: f32 = 0
            }
            5971341806684502351 = TimeBlendData {
                mTime: f32 = 0
            }
            5971341806701279970 = TimeBlendData {
                mTime: f32 = 0
            }
            6043401131577472956 = TimeBlendData {
                mTime: f32 = 0
            }
            6043401131594250575 = TimeBlendData {
                mTime: f32 = 0
            }
            6043401131611028194 = TimeBlendData {
                mTime: f32 = 0
            }
            6115460456487221180 = TimeBlendData {
                mTime: f32 = 0
            }
            6115460456503998799 = TimeBlendData {
                mTime: f32 = 0
            }
            6115460456520776418 = TimeBlendData {
                mTime: f32 = 0
            }
            6115460459080752507 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364256212655483 = TimeBlendData {
                mTime: f32 = 0
            }
            16486287732941682620 = TimeBlendData {
                mTime: f32 = 0
            }
            16486287732958460239 = TimeBlendData {
                mTime: f32 = 0
            }
            16486287732975237858 = TimeBlendData {
                mTime: f32 = 0
            }
            16486287735535213947 = TimeBlendData {
                mTime: f32 = 0
            }
            17110474039877737851 = TimeBlendData {
                mTime: f32 = 0
            }
        }
    }
}
