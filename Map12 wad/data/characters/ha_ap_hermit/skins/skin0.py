#PROP_text
type: string = "PROP"
version: u32 = 2
linked: list[string] = {
    "DATA/Characters/HA_AP_Hermit/HA_AP_Hermit.bin"
    "DATA/Characters/BW_AP_Finn/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/HA_AP_Hermit/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "HA_AP_Hermit"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/BW_AP_Finn/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/HA_AP_Hermit/Skins/Base/HA_AP_Hermit.skl"
            simpleSkin: string = "ASSETS/Characters/HA_AP_Hermit/Skins/Base/HA_AP_Hermit.skn"
            texture: string = "ASSETS/Characters/HA_AP_Hermit/Skins/Base/HA_AP_Hermit.dds"
            skinScale: f32 = 1.5
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        mContextualActionData: link = "Characters/HA_AP_Hermit/CAC/HA_AP_Hermit"
        mResourceResolver: link = "Characters/HA_AP_Hermit/Skins/Skin0/Resources"
    }
    "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_ReadVarA" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Base_Idle02_ReadVarA"
        particlePath: string = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_ReadVarA"
    }
    "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_Leadin01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Base_Idle02_Leadin01"
        particlePath: string = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_Leadin01"
    }
    "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_ReadVarB" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Base_Idle02_ReadVarB"
        particlePath: string = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_ReadVarB"
    }
    "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Leaving01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Base_Leaving01"
        particlePath: string = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Leaving01"
    }
    "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Base_Idle01"
        particlePath: string = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle01"
    }
    "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_Pointing" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Base_Idle02_Pointing"
        particlePath: string = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_Pointing"
    }
    "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Entering01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Base_Entering01"
        particlePath: string = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Entering01"
    }
    "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_Fidget" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Base_Idle02_Fidget"
        particlePath: string = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_Fidget"
    }
    "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Annoyed01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Base_Annoyed01"
        particlePath: string = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Annoyed01"
    }
    "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle01_Leadin01" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Base_Idle01_Leadin01"
        particlePath: string = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle01_Leadin01"
    }
    "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_Underbench" = VfxSystemDefinitionData {
        visibilityRadius: f32 = 1000
        particleName: string = "HA_AP_Hermit_Base_Idle02_Underbench"
        particlePath: string = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_Underbench"
    }
    "Characters/HA_AP_Hermit/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0xfcc6184a = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Annoyed01"
            0xc9d95f58 = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Entering01"
            0x4a0dc598 = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle01"
            0xe4242c67 = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle01_Leadin01"
            0xee94460b = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_Fidget"
            0x7797e72c = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_Leadin01"
            0x0d6b9c1c = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_Pointing"
            0xa24a523a = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_ReadVarA"
            0xa14a50a7 = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_ReadVarB"
            0xc2023492 = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Idle02_Underbench"
            0xf59bcd60 = "Characters/HA_AP_Hermit/Skins/Skin0/Particles/HA_AP_Hermit_Base_Leaving01"
        }
    }
    "Characters/HA_AP_Hermit/CAC/HA_AP_Hermit" = ContextualActionData {
        mCooldown: f32 = 1
        mSituations: map[hash,embed] = {
            "Purchase" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Purchase"
                        mConditions: list[pointer] = {
                            ContextualConditionItemPriceMinimum {
                                mItemPriceMinimum: u32 = 300
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Purchase2DGeneral"
                        }
                    }
                }
            }
            "ShopOpen" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "OpenRich"
                        mConditions: list[pointer] = {
                            ContextualConditionHasGold {
                                mGold: f32 = 3000
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mAllyEventName: string = "Open2DGold3000"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenMulti"
                        mConditions: list[pointer] = {
                            ContextualConditionShopOpenCount {
                                mShopOpenCount: u32 = 7
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mAllyEventName: string = "Open2DCountSeven"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenHeimerdinger"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Heimerdinger/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DHeimerdinger"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenBlitzcrank"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Blitzcrank/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DBlitzcrank"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenJayce"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Jayce/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DJayce"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenOrianna"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Orianna/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DOrianna"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenCaitlyn"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Caitlyn/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DCaitlyn"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenVi"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Vi/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DVi"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenZilean"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Zilean/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DZilean"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenEzreal"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Ezreal/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DEzreal"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenLissandra"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Lissandra/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DLissandra"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenSejuani"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Sejuani/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DSejuani"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenAshe"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Ashe/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DAshe"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenJinx"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Jinx/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DJinx"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "ShopOpen"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DGeneral"
                        }
                    }
                }
            }
            "ShopClose" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "CloseForgotItems"
                        mConditions: list[pointer] = {
                            ContextualConditionItemPurchased {}
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Close3DNoPurchase"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "ShopClose"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Close3D"
                        }
                    }
                }
            }
            "Browsing" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Browsing"
                        mConditions: list[pointer] = {
                            ContextualConditionCustomTimer {
                                mCustomTimer: f32 = 22
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Browsing2DGeneral"
                        }
                    }
                }
            }
            "Ambient" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Ambient"
                        mConditions: list[pointer] = {
                            ContextualConditionCustomTimer {
                                mCustomTimer: f32 = 28
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Ambient3DGeneral"
                        }
                    }
                }
            }
        }
        mObjectPath: string = "Characters/HA_AP_Hermit/CAC/HA_AP_Hermit"
    }
}
