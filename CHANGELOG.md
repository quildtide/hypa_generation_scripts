# CHANGELOG

## v2.0.0a (2023-02-07)
Base mod has no changes

### Submods
#### Legion 1.29.0.1
- Is now correctly disabled when you disable HyPA.

## v2.0.0 (2023-02-06)
This HyPA update has a high chance of breaking things. Initial testing has shown that things are working fine. There is a decent likelihood that issues will have to be addressed as they appear in the near future.

- Update unit info with:
  - Base game balance 116982
    - Support for `Custom_58`
      - This will fix compatibility with AIs and effect mods

- Support removed from deprecated mods:
  - Celestial Expansion and Celestial Expansion Addon

- Support updated for mods:
  - Legion 1.29.0-116982
  - Bug Faction 1.30
  - Second Wave 0.14.1
  - Section 17 0.7.0
  - Upgradable Turrets 1.13
  - Dozer 1.1.1

### Submods
Legion support was moved from the main HyPA mod to a dependency submod for improved license compliance capabilities. Players should not notice any differences in behavior.

#### Legion 1.29.0.0
- Supports Legion 1.29.0-116982

### Compatibility Patches

#### Thorosmen 2.3.9.0
- Supports Thorosmen 2.3.9

#### Telemazer go BRRR 0.3.0.0
- Supports Telemazer go BRRR 0.3.0


## v1.4.2 (2023-05-19)
- Support updated for mods:
  - Legion 1.27.0-116931
  - Bug Faction 1.16

### Compatibility Patches

#### Celestial Expansion 2.5.0.0
- Supports Celestial Expansion 2.5.0-up0 and Celestial Expansion Additional 2.5.0-up0

#### Thorosmen 2.1.4.0
- Supports Thorosmen 2.1.4

#### Telemazer go BRRR 0.2.0.1
- Fix dependency issues

## v1.4.1 (2023-04-21)
- Mod description edited to include Legion license information.

## v1.4.0 (2023-04-21)
- Update unit info with:
  - Base game balance 116931

- Second-class support (via compatibility patch) added for:
  - Telemazer go BRRR v0.2.0

### Compatibility Patches

#### Celestial Expansion v2.0.0.0
- Supports Celestial Expansion v2.0.0-up0 and Celestial Expansion Additional v2.0.0-up0

#### Telemazer go BRRR v0.2.0.0
- Supports Telemazer go BRRR v0.2.0

#### Thorosmen v2.1.2.0
- Supports Thorosmen v2.1.2


## v1.3.1 (2023-04-16)
- New mod compatibility patch system for handling second-class support
- Thorosmen support from main HyPA mod to a compatibility patch
  - Manhattans should behave normally again
  - MLA Anti-nukes should work properly against Legion Nukes.
- Second-class support (via compatibility patch) added for:
  - Celestial Expansion v1.0.3-up1
  - Celestial Expansion Additional v1.0.7-up0

### Compatibility Patches

#### Thorosmen v2.1.0.0
- Supports Thorosmen v2.1.0

#### Celestial Expansion v1.0.3.0
- Supports Celestial Expansion v1.0.3-up1 and Celestial Expansion Additional v1.0.7-up0

### Redenbacher-EX
- Redenbacher-EX updates will be unbound from HyPA updates
  - Future Redenbacher-EX updates may be created on an ad-hoc basis
  - Future Redenbacher-EX updates will have their own changelog.
  - Future Redenbacher-EX updates will have different versioning from HyPA.
  - Redenbacher-EX is unlikely to have compatibility patch support for mods that require it.

## v1.3.0 (2023-03-18)
- Temporarily disable support for Thorosmen
  - This will improve support for other supported mods, such as Legion
  - Support for Thorosmen will be brought back in the near future

## v1.2.0 (2023-02-20)

- Fix a mod order bug that primarily affects Section 17
  - The Experimental Gantry will be buildable again
  - Experimentals will not be buildable from T2 factories

- Support updated for mods:
  - Second Wave v0.12.3
  - Thorosmen v1.9.0

### Known Issues

- Thorosmen has Class 2 Support due to partial conflicts with Section 17
  - The following units are built from the Section 17 Experimental Gantry instead of their normal methods:
    - Lawnmower
    - Toblerone
    - LZ 130 Hindenburg
    - Thorondor
  - These units cannot be built without Section 17 enabled in addition to Thorosmen


## v1.1.4a (2023-02-14)

- Support maintained (no relevant changes) for mod:
  - Thorosmen v1.8.8

## v1.1.4 (2023-02-11)
### HyPA
- Fix missing lobby chat text

## v1.1.3 (2023-02-11)

- Support updated for mods:
  - Section 17 v0.5.0
  - Dozer v1.0.2

### HyPA
- Lobby chat now contains a warning that HyPA is active + an explanation
- A message is sent at the start of a match explaining that HyPA is active + an explanation
- Commander health multiplier: 3 -> 2
- Commander metal value multiplier: 3 -> 2
- Pseudo-production weapon recharge rates: 1.5x -> 2.0x:
  - Legion Necromancer
  - Bug Matriarch
  - Section 17 Sigma (Avengers and Slammers)
  - Section 17 Dox Materializer
- Bug Matriarch death spawns Bug Boomers instead of Legion Purgers (upstream mod still awaiting fix)

## v1.1.2 (2023-01-31)
- Fix base game patch number mistake in Changelog and modinfo.json

## v1.1.1 (2023-01-31)

- Support maintained (no relevant changes) for mod:
  - Thorosmen 1.8.6

### HyPA
- Commander health is now multiplied by 3
- Commander metal value is now multiplied by 3
- Lob now recharges and fires 2x faster instead of 1.5x
  
### Redenbacher-EX
- Fixed Bug Commander not receiving Commander buffs

## v1.1.0 (2023-01-20)

- Support added for new mods:
  - Bug faction 1.11
  - Upgradable Turrets 1.11
  - Thorosmen 1.8.5

## v1.0.1 (2022-12-27)

- Update unit info with:
  - Base game balance 116400
  - Legion 1.26.0-116242
  - Second Wave 0.12.0
  - Section 17 0.4.0

## v1.0.0 (2021-05-31)

### HyPA
- Fix bug preventing commander from receiving faster attack speed

### Redenbacher-EX
- Create new mode with further enhanced stats

## v0.9.6 (2021-04-13)

- Add support for mods:
  - Legion
  - Second Wave
  - Section 17
  - Dozer
- Energy and time ammo weapons are handled differently from before
  - Ammo per shot and ammo capacity are divided by 1.5
  - Ammo demand is no longer multiplied by 1.5
  - Metal ammo weapon behavior remains how it previously was (ammo demand x1.5)

