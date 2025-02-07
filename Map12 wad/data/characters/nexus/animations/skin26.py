#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Nexus/Animations/Skin26" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Idle1" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x49de496d = SoundEventData {
                        mName: hash = 0x49de496d
                        mSoundName: string = "Play_sfx_Env_Map14_order_nexus_alive_loop"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x17ed2f2c = ParticleEventData {
                        mName: hash = 0x17ed2f2c
                        mEffectName: string = "BW_AP_Order_Nexus_Idle.troy"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x7ceee790
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Nexus/Skins/Skin26/Animations/BW_AP_ChaosNexus_Idle.anm"
                }
            }
            "death" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "submesh" = SubmeshVisibilityEventData {
                        mName: hash = "submesh"
                        mShowSubmeshList: list[hash] = {
                            0xf1183931
                        }
                        mHideSubmeshList: list[hash] = {
                            "OrderNexus"
                            0x4252de4b
                        }
                    }
                    "Audio_Death" = SoundEventData {
                        mName: hash = "Audio_Death"
                        mSoundName: string = "Play_sfx_Env_Global_EoG_OrderNexus_death_oc"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Nexus/Skins/Skin26/Animations/BW_AP_ChaosNexus_Death.anm"
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Default" = TrackData {}
        }
    }
}
