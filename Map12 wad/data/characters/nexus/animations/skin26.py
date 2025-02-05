#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Nexus/Animations/Skin26" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Idle1" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Nexus/Skins/Skin26/Animations/BW_AP_OrderNexus_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x49de496d = SoundEventData {
                        mSoundName: string = "Play_sfx_Env_Map14_order_nexus_alive_loop"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mName: hash = 0x49de496d
                    }
                    0x17ed2f2c = ParticleEventData {
                        mEffectName: string = "BW_AP_Order_Nexus_Idle.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x7ceee790
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mName: hash = 0x17ed2f2c
                    }
                }
                mFlags: u32 = 2
            }
            "death" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Nexus/Skins/Skin26/Animations/BW_AP_OrderNexus_Death.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "submesh" = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            0xf1183931
                        }
                        mHideSubmeshList: list[hash] = {
                            "OrderNexus"
                            0x4252de4b
                        }
                        mName: hash = "submesh"
                    }
                    0x1ba70171 = ParticleEventData {
                        mName: hash = 0x1ba70171
                        mStartFrame: f32 = 132
                        mEffectName: string = "SRU_Order_nexus_swirlies.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x1ba70171
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x1ca70304 = ParticleEventData {
                        mName: hash = 0x1ca70304
                        mStartFrame: f32 = 138
                        mEffectName: string = "SRU_Order_nexus_swirlies.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x1ca70304
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x595bd859 = ParticleEventData {
                        mName: hash = 0x595bd859
                        mStartFrame: f32 = 135
                        mEffectName: string = "SRU_Order_nexus_swirlies.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x595bd859
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x1ea7062a = ParticleEventData {
                        mName: hash = 0x1ea7062a
                        mStartFrame: f32 = 147
                        mEffectName: string = "SRU_Order_nexus_swirlies.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x1ea7062a
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x5f5be1cb = ParticleEventData {
                        mName: hash = 0x5f5be1cb
                        mStartFrame: f32 = 130
                        mEndFrame: f32 = 160
                        mEffectName: string = "SRU_Order_nexus_swirlies.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x5f5be1cb
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    "Audio_Death" = SoundEventData {
                        mSoundName: string = "Play_sfx_Env_Global_EoG_OrderNexus_death_oc"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mName: hash = "Audio_Death"
                    }
                    "Explosion" = ParticleEventData {
                        mEffectName: string = "BW_Order_Nexus_Explosion.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Default" = TrackData {}
        }
    }
}
