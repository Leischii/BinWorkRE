#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/HABW_banner/CharacterRecords/Root" = CharacterRecord {
        mCharacterName: string = "HABW_banner"
        baseHP: f32 = 435
        hpPerLevel: f32 = 85
        baseStaticHPRegen: f32 = 1.01999998
        hpRegenPerLevel: f32 = 0.129999995
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 0
            arBase: f32 = 202
            arPerLevel: f32 = 38
            arBaseStaticRegen: f32 = 1.38999999
            arRegenPerLevel: f32 = 0.129999995
        }
        baseDamage: f32 = 54.5
        damagePerLevel: f32 = 3.20000005
        baseArmor: f32 = 15
        armorPerLevel: f32 = 3.5
        baseSpellBlock: f32 = 30
        spellBlockPerLevel: f32 = 1.25
        baseMoveSpeed: f32 = 345
        attackRange: f32 = 175
        attackSpeedPerLevel: f32 = 3
        acquisitionRange: f32 = 600
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.0916666687
            }
            mAttackProbability: option[f32] = {
                0.5
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0.5
                }
                mAttackName: option[string] = {
                    "TemplateFighterBasicAttack2"
                }
            }
        }
        critAttacks: list[embed] = {
            AttackSlotData {
                mAttackDelayCastOffsetPercent: option[f32] = {
                    -0.0916666687
                }
                mAttackName: option[string] = {
                    "TemplateFighterCritAttack"
                }
            }
        }
        selectionHeight: f32 = 122
        selectionRadius: f32 = 1000
        pathfindingCollisionRadius: f32 = 30
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            passiveData: list[embed] = {
                ToolPassiveData {
                    name: string = "game_character_passiveName_TemplateFighter"
                }
            }
            searchTags: string = "Fighter,melee"
            championId: i32 = 997
            roles: string = "BRAWLER"
            magicRank: i32 = 2
            difficultyRank: i32 = 3
            description: string = "game_character_description_TemplateFighter"
            defenseRank: i32 = 5
            ChasingAttackRangePercent: f32 = 0.800000012
            attackRank: i32 = 8
        }
        flags: u32 = 8398152
    }
    "Characters/HABW_banner/Skins/Meta" = SkinCharacterMetaDataProperties {}
}
