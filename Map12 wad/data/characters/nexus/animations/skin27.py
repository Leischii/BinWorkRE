#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    0xcd671934 = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Idle1" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Nexus/Skins/Skin27/Animations/BW_AP_ChaosNexus_Idle.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x49de496d = SoundEventData {
                        mSoundName: string = "Play_sfx_Env_Map14_chaos_nexus_alive_loop"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mName: hash = 0x49de496d
                    }
                    "submesh" = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "ChaosNexus"
                        }
                        mHideSubmeshList: list[hash] = {
                            0x5f403879
                        }
                        mName: hash = "submesh"
                    }
                }
                mFlags: u32 = 2
            }
            "death" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Nexus/Skins/Skin27/Animations/BW_AP_ChaosNexus_Death.anm"
                }
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "submesh" = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            0x5f403879
                        }
                        mHideSubmeshList: list[hash] = {
                            "ChaosNexus"
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
                        mSoundName: string = "Play_sfx_Env_Global_EoG_ChaosNexus_death_cast"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mName: hash = "Audio_Death"
                    }
                    "Explosion" = ParticleEventData {
                        mEffectName: string = "BW_Chaos_Nexus_Explosion.troy"
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
