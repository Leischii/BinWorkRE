#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    0x202b438c = ContextualActionData {
        mCooldown: f32 = 1
        mSituations: map[hash,embed] = {
            "Ambient" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Ambient - 25s"
                        mConditions: list[pointer] = {
                            ContextualConditionCustomTimer {
                                mCustomTimer: f32 = 25
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Ambient3DGeneral"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            0xc59f257e: bool = true
                        }
                    }
                }
            }
            "Browsing" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Browsing - 22s"
                        mConditions: list[pointer] = {
                            ContextualConditionCustomTimer {
                                mCustomTimer: f32 = 22
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Browsing2DGeneral"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                }
            }
            "ShopClose" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Close"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Close3DGeneral"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Game Timer"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Close3DGameTimerTwentyFive"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "General"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Close3DGeneral"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                }
            }
            "ShopOpen" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Specific Faction/Race"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterMetadata {
                                        mCategory: string = "faction"
                                        mData: string = "piltover"
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mAllyEventName: string = "Open2DPiltover"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Specific Champion"
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
                            mMaxOccurences: u32 = 1
                            mAllyEventName: string = "Open2DBlitzcrank"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Game Timer"
                        mConditions: list[pointer] = {
                            ContextualConditionGameTimer {
                                mGameTimeInMinutes: f32 = 25
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 3
                            mAllyEventName: string = "Open2DGameTimerTwentyFive"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Open Count"
                        mConditions: list[pointer] = {
                            ContextualConditionShopOpenCount {
                                mShopOpenCount: u32 = 10
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 3
                            mAllyEventName: string = "Open2DCount10"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Nearby Ally Count"
                        mConditions: list[pointer] = {
                            ContextualConditionNearbyChampionCount {
                                mCount: u32 = 2
                                mCompareOp: u8 = 3
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 3
                            mAllyEventName: string = "Open2DNearbyAllyCountTwo"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Nearby Enemy Count"
                        mConditions: list[pointer] = {
                            ContextualConditionNearbyChampionCount {
                                mTeamCompareOp: u8 = 1
                                mCount: u32 = 2
                                mCompareOp: u8 = 3
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 3
                            mAllyEventName: string = "Open2DNearbyEnemyCountTwo"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Gold"
                        mConditions: list[pointer] = {
                            ContextualConditionHasGold {
                                mGold: f32 = 3000
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 3
                            mAllyEventName: string = "Open2DGold3000"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "General"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DGeneral"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            0xc59f257e: bool = true
                        }
                    }
                }
            }
            "Purchase" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "MinimumPrice"
                        mConditions: list[pointer] = {
                            ContextualConditionItemPriceMinimum {
                                mItemPriceMinimum: u32 = 2900
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 3
                            mAllyEventName: string = "Purchase2DMinimumPrice2900"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Specific Item"
                        mConditions: list[pointer] = {
                            ContextualConditionItemID {
                                mItems: list[hash] = {
                                    "Items/6609"
                                    "Items/226609"
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mAllyEventName: string = "Purchase2DChempunkChainsword"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "General"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Purchase2DGeneral"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                }
            }
        }
        mObjectPath: string = "Characters/HA_AP_Viking/CAC/Shopkeeper_CAC_Template"
    }
    "Characters/BW_AP_Bubbs/CAC/BW_AP_Bubbs" = ContextualActionData {
        mSituations: map[hash,embed] = {
            "Purchase" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Audio300Purchase"
                        mConditions: list[pointer] = {
                            ContextualConditionRuleCooldown {
                                mRuleCooldown: f32 = 15
                            }
                            ContextualConditionItemPriceMinimum {
                                mItemPriceMinimum: u32 = 300
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Purchase"
                        }
                    }
                }
            }
            "ShopOpen" = ContextualSituation {
                mChooseRandomValidRule: bool = true
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "AudioOpenCorki"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Corki/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "OpenCorki"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenDiana"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Diana/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "OpenDiana"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenDraven"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Draven/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "OpenDraven"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenEzreal"
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
                            mAllyEventName: string = "OpenEzreal"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenFizz"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Fizz/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "OpenFizz"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenGangplank"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Gangplank/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "OpenGangplank"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenHeimerdinger"
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
                            mAllyEventName: string = "OpenHeimerdinger"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenNami"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Nami/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "OpenNami"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenNautilus"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Nautilus/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "OpenNautilus"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenRumble"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Rumble/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "OpenRumble"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenSivir"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Sivir/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "OpenSivir"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenTahmKench"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/TahmKench/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "OpenTahmKench"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenUdyr"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Udyr/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "OpenUdyr"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "AudioOpenNormal"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open"
                        }
                    }
                }
            }
            "ShopClose" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "AudioCloseNormal"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Close"
                        }
                    }
                }
            }
            "Browsing" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "AudioBrowsingNormal"
                        mConditions: list[pointer] = {
                            ContextualConditionCustomTimer {
                                mCustomTimer: f32 = 17
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Browsing"
                        }
                    }
                }
            }
            "Ambient" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "AudioAmbientNormal"
                        mConditions: list[pointer] = {
                            ContextualConditionCustomTimer {
                                mCustomTimer: f32 = 28
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Ambient"
                        }
                    }
                }
            }
        }
        mObjectPath: string = "Characters/BW_AP_Bubbs/CAC/Shopkeeper_CAC_Template"
    }
    "Characters/HA_AP_Viking/CharacterRecords/Root" = CharacterRecord {
        mCharacterName: string = "BW_AP_Bubbs"
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 0
        }
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
        }
        flags: u32 = 8398144
    }
    "Characters/HA_AP_Viking/Skins/Meta" = SkinCharacterMetaDataProperties {}
}
