#PROP_text
type: string = "PROP"
version: u32 = 2
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/HA_AP_Hermit/CharacterRecords/Root" = CharacterRecord {
        mCharacterName: string = "BW_AP_Finn"
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
    "Characters/HA_AP_Hermit/Skins/Meta" = SkinCharacterMetaDataProperties {}
}
