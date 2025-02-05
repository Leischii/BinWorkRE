#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/HA_AP_Chains_Long/Animations/Skin0" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "E_WIND_STRONG" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0500000007
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_E_WIND_STRONG.anm"
                }
            }
            "Idle1" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_E_WIND_STRONG.anm"
                }
            }
            0x676ee449 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_E_BREAK.anm"
                }
            }
            "E_Broken" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_E_BROKEN.anm"
                }
            }
            "N_Wind_Strong" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0500000007
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_N_WIND_STRONG.anm"
                }
            }
            0xf31dab74 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_N_BREAK.anm"
                }
            }
            "N_Broken" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_N_BROKEN.anm"
                }
            }
            0xd1bfca4f = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_S_BREAK.anm"
                }
            }
            "S_Broken" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_S_BROKEN.anm"
                }
            }
            "S_WIND_STRONG" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0500000007
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_S_WIND_STRONG.anm"
                }
            }
            0x1841bff3 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_W_BREAK.anm"
                }
            }
            "W_Broken" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_W_BROKEN.anm"
                }
            }
            "W_WIND_STRONG" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0500000007
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HA_AP_Chains_Long/Skins/Base/Animations/SIM_W_WIND_STRONG.anm"
                }
            }
            0x12b23e20 = SequencerClipData {
                mFlags: u32 = 8
                mClipNameList: list[hash] = {
                    0x676ee449
                    "E_Broken"
                }
            }
            0x54be08b1 = SequencerClipData {
                mFlags: u32 = 8
                mClipNameList: list[hash] = {
                    0xf31dab74
                    "N_Broken"
                }
            }
            0xab04b9ba = SequencerClipData {
                mFlags: u32 = 8
                mClipNameList: list[hash] = {
                    0xd1bfca4f
                    "S_Broken"
                }
            }
            0xaf430e9e = SequencerClipData {
                mFlags: u32 = 8
                mClipNameList: list[hash] = {
                    0x1841bff3
                    "W_Broken"
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Default" = TrackData {}
        }
    }
}
