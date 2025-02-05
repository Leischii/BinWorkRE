#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Nexus/Skins/Meta" = SkinCharacterMetaDataProperties {
        relativeColorSwapTable: list[i32] = {
            1
            0
            3
            2
            5
            4
            7
            6
            9
            8
            11
            10
            13
            12
            15
            14
            17
            16
            19
            18
            21
            20
            23
            22
            25
            24
            126
            127
            29
            28
            31
            30
            33
            32
        }
    }
    "Characters/Nexus/CharacterRecords/Root" = CharacterRecord {
        mCharacterName: string = "Nexus"
        baseHP: f32 = 5500
        baseStaticHPRegen: f32 = 20
        healthBarHeight: f32 = 500
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 0
        }
        attackSpeedRatio: f32 = 0
        perceptionBubbleRadius: option[f32] = {
            1350
        }
        name: string = "game_character_displayname_Nexus"
        selectionHeight: f32 = 117
        selectionRadius: f32 = 397.221985
        pathfindingCollisionRadius: f32 = 304
        unitTagsString: string = "Structure | Structure_Nexus"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
        }
    }
    0xc4235489 = CharacterRecord {
        mCharacterName: string = "Nexus"
        baseHP: f32 = 5500
        baseStaticHPRegen: f32 = 20
        healthBarHeight: f32 = 500
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 0
        }
        attackSpeedRatio: f32 = 0
        perceptionBubbleRadius: option[f32] = {
            1350
        }
        name: string = "game_character_displayname_Nexus"
        selectionHeight: f32 = 117
        selectionRadius: f32 = 397.221985
        pathfindingCollisionRadius: f32 = 350
        unitTagsString: string = "Structure | Structure_Nexus"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
        }
    }
}
