from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Job, Base, Ability

engine = create_engine('sqlite:///ff14jobs.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# PALADIN
job1 = Job(name="Paladin",
           img="https://bit.ly/2MbzYcA",
           role="Tank",
           author="diego ruiz",
           description="For centuries, the elite of the Sultansworn have "
           "served as personal bodyguards to the royal family of Ul'dah. "
           "Known as paladins, these men and women marry exquisite swordplay "
           "with stalwart shieldwork to create a style of combat "
           "uncompromising in its defense. Clad in brilliant silver armor, "
           "they charge fearlessly into battle, ever ready to lay down their "
           "lives for their liege. To be a paladin is to protect, and those "
           "who choose to walk this path will become the iron foundation"
           "upon which the party's defense is built.")
session.add(job1)
session.commit()

ability1 = Ability(name="Fast Blade",
                   description="Delivers an attack with a potency of 200",
                   level=1,
                   Cast="Weaponskill",
                   author="diego ruiz",
                   job=job1)
session.add(ability1)
session.commit()


ability2 = Ability(name="Fight or Flight",
                   description="Increases physical damage dealt by 25%",
                   level=2, Cast="Ability",
                   author="diego ruiz",
                   job=job1)
session.add(ability2)
session.commit()

ability3 = Ability(name="Riot Blade",
                   description="Delivers an attack with a potency of 100",
                   level=4, Cast="Weaponskill",
                   author="diego ruiz",
                   job=job1)
session.add(ability3)
session.commit()

ability4 = Ability(name="Total Eclipse",
                   description="Delivers an attack with a potency "
                   "of 120 to all nearby enemies",
                   level=6,
                   Cast="Weaponskill",
                   author="diego ruiz",
                   job=job1)
session.add(ability4)
session.commit()

ability5 = Ability(name="Shield Bash",
                   description="Delivers an attack with a potency of 110. "
                   "Additional Effect: Stun. Duration: 6s",
                   author="diego ruiz",
                   level=10, Cast="Weaponskill", job=job1)
session.add(ability5)
session.commit()

# DARK KNIGHT
job2 = Job(name="Dark Knight",
           img="https://bit.ly/2q9chci",
           role="Tank",
           author="diego ruiz",
           description="The pious Ishgardian clergy guide the flock, and the "
           "devout knights protect the weak. Yet even the holiest of men "
           "succumb to the darkest of temptations. None dare to administer "
           "justice to these sacrosanct elite residing outside the reach of "
           "the law. Who, then, defends the feeble from the transgressions of "
           "those meant to guide and protect them. A valiant few take up arms "
           "to defend the downtrodden, and not even the holy priests and "
           "knights can escape their judgment. Pariahs in their own land, "
           "they are known by many as dark knights. These sentinels bear no "
           "shields declaring their allegiance. Instead, their greatswords "
           "act as beacons to guide the meek through darkness.")
session.add(job2)
session.commit()

ability1 = Ability(name="Living Shadow",
                   description="Conjure a simulacrum of your darkside to "
                   "fight alongside you.",
                   author="diego ruiz",
                   level=80, Cast="Ability", job=job2)
session.add(ability1)
session.commit()


ability2 = Ability(name="Dark Missionary",
                   description="Reduces magic damage taken by self and "
                   "nearby party members by 10%.",
                   author="diego ruiz",
                   level=76, Cast="Ability", job=job2)
session.add(ability2)
session.commit()

ability3 = Ability(name="Edge of Shadow",
                   description="Deals unaspected damage with "
                   "a potency of 500.",
                   level=74,
                   author="diego ruiz",
                   Cast="Ability",
                   job=job2)
session.add(ability3)
session.commit()

ability4 = Ability(name="Flood of Shadow",
                   description="Deals unaspected damage with a potency of "
                   "300 to all enemies in a straight line before you.",
                   level=74,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job2)
session.add(ability4)
session.commit()

ability5 = Ability(name="Stalwart Soul",
                   description="Deals unaspected damage with a potency of "
                   "100 to all nearby enemies.",
                   level=72,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job2)
session.add(ability5)
session.commit()

# WARRIOR
job3 = Job(name="Warrior",
           img="https://bit.ly/328RB2g",
           role="Tank",
           author="diego ruiz",
           description="On the northernmost edge of Abalathia's Spine "
           "exists a mountain tribe renowned for producing fearsome "
           "mercenaries. Wielding greataxes and known as warriors, these "
           "men and women learn to harness their inner-beasts and translate "
           "that power to unbridled savagery on the battlefield. In former "
           "times which saw war waged ceaselessly in Eorzea, the warriors "
           "featured prominently on the front lines of battle. With the "
           "arrival of peacetime, however, their art has descended into "
           "the shadows of obscurity, where it remains to this day.")
session.add(job3)
session.commit()

ability1 = Ability(name="Chaotic Cyclone",
                   description="Delivers a critical direct hit with a "
                   "potency of 400 to all nearby enemies.",
                   level=72,
                   Cast="Weaponskill",
                   author="diego ruiz",
                   job=job3)
session.add(ability1)
session.commit()

ability2 = Ability(name="Nascent Flash",
                   description="Grants Nascent Flash to self and Nascent "
                   "Glint to target party member.",
                   level=76,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job3)
session.add(ability2)
session.commit()

ability3 = Ability(name="Nascent Flash",
                   description="Delivers a critical direct hit with a "
                   "potency of 920",
                   level=80,
                   Cast="Weaponskill",
                   author="diego ruiz",
                   job=job3)
session.add(ability3)
session.commit()


# GUNBREAKER
job4 = Job(name="Gunbreaker",
           img="https://bit.ly/2nFTJiR",
           role="Tank",
           author="diego ruiz",
           description="The Hrothgar of northern Ilsabard have passed the "
           "art of the gunblade from one generation to the next. The "
           "weapon itself combines a sword with a firing mechanism, "
           "emitting a range of magical effects by utilizing aetherically "
           "imbued cartridges. Originally employed by Queen Gunnhildr's "
           "personal guard, they were once known as Gunnhildrs Blades "
           "and differ greatly from the similarly named weapons used "
           "in the Garlean Empire.")
session.add(job4)
session.commit()

ability1 = Ability(name="Abdomen Tear",
                   description="Delivers an attack with a potency of 280.",
                   level=70,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job4)
session.add(ability1)
session.commit()

ability2 = Ability(name="Eye Gouge",
                   description="Delivers an attack with a potency of 300.",
                   level=70,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job4)
session.add(ability2)
session.commit()

ability3 = Ability(name="Fated Circle",
                   description="Delivers an attack with a potency of 320 "
                   "to all nearby enemies.",
                   level=72,
                   Cast="Weaponskill",
                   author="diego ruiz",
                   job=job4)
session.add(ability3)
session.commit()

ability4 = Ability(name="Bloodfest",
                   description="Draws aetheric energy from target,"
                   "adding 2 Cartridges to your Powder Gauge.",
                   level=76,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job4)
session.add(ability4)
session.commit()

ability5 = Ability(name="Blasting Zone",
                   description="Delivers an attack with a potency of 800.",
                   level=80,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job4)
session.add(ability5)
session.commit()


# WHITE MAGE
job5 = Job(name="White Mage",
           img="https://bit.ly/2MwF0iI",
           role="Healer",
           author="diego ruiz",
           description="White magic, the arcane art of succor, was "
           "conceived eras past that the world might know comfort. Alas, "
           "man began perverting its powers for selfgain, and by his "
           "wickedness brought about the Sixth Umbral catastrophe. "
           "Although the art subsequently became forbidden, it is now "
           "in the midst of a revival at the hands of the Padjal, chosen "
           "of the elementals. Those who would walk the path of the white "
           "mage are healers without peer, possessed of the power to "
           "deliver comrades from the direst of affliction seven "
           "the icy grip of death itself.")
session.add(job5)
session.commit()

ability1 = Ability(name="Dia",
                   description="Deals unaspected damage with "
                   "a potency of 120.",
                   level=72,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job5)
session.add(ability1)
session.commit()

ability2 = Ability(name="Glare",
                   description="Deals unaspected damage with a "
                   "potency of 300.",
                   level=72,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job5)
session.add(ability2)
session.commit()

ability3 = Ability(name="Afflatus Misery",
                   description="Deals unaspected damage to target and "
                   "all enemies nearby it with a potency of 900 for "
                   "the first enemy.",
                   level=74,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job5)
session.add(ability3)
session.commit()

ability4 = Ability(name="Afflatus Rapture",
                   description="Restores own HP and the HP of all "
                   "nearby party members.",
                   level=76,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job5)
session.add(ability4)
session.commit()

ability5 = Ability(name="Temperance",
                   description="Increases healing magic potency by 20%, "
                   "while reducing damage taken by self and all party "
                   "members within a radius of 30 yalms by 10%.",
                   level=80,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job5)
session.add(ability5)
session.commit()


# SCHOLAR
job6 = Job(name="Scholar",
           img="https://bit.ly/2IMPQA9",
           role="Healer",
           author="diego ruiz",
           description="In an age long past, when mankind flourished "
           "under the radiance of arcane mastery, the island of Vylbrand "
           "was home to a city-state called Nym. Though the history of "
           "that age tells of countless wars waged with earth-shattering "
           "incantations, it was the brilliant strategic maneuvering of "
           "Nym's scholars that allowed their mundane army of mariners "
           "to throw back would-be conquerers time and again. These "
           "learned men and women defended the freedom of their tiny "
           "nation with their unique command over spell-weaving "
           "faeries, utilizing the creatures' magicks to heal the "
           "wounded and bolster the strength of their allies.")
session.add(job6)
session.commit()

ability1 = Ability(name="Biolysis",
                   description="Deals unaspected damage over time.",
                   level=72,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job6)
session.add(ability1)
session.commit()

ability2 = Ability(name="Broil III",
                   description="Deals unaspected damage with a "
                   "potency of 280.",
                   level=72,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job6)
session.add(ability2)
session.commit()

ability3 = Ability(name="Recitation",
                   description="Allows the execution of Adloquium, Succor, "
                   "Indomitability, or Excogitation without consuming "
                   "resources while also ensuring critical HP is restored.",
                   level=74,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job6)
session.add(ability3)
session.commit()

ability4 = Ability(name="Fey Blessing",
                   description="Orders faerie to execute Fey Blessing.",
                   level=76,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job6)
session.add(ability4)
session.commit()

ability5 = Ability(name="Summon Seraph",
                   description="Summons Seraph to fight at your side. "
                   "While summoned, automatically casts Seraphic "
                   "Veil on party members who suffer damage.",
                   level=80,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job6)
session.add(ability5)
session.commit()

# ASTRO
job7 = Job(name="Astro",
           img="https://bit.ly/2pcMsaS",
           role="Healer",
           author="diego ruiz",
           description="Ever has man coveted knowledge, and none more so "
           "than that of his fate. Thus did he labor to master the skill "
           "of foresight but initial efforts bore little fruit. That "
           "is, until he looked to the stars above, which foretell the "
           "coming seasons, and learned to read the heavens. Though "
           "this gift is known today as astrology, the people of "
           "Sharlayan saw fit to not only read the stars, but to "
           "write their movements as well. By attuning their aetherial "
           "energies to that of constellations, they learned to wield "
           "magicks with heretofore unseen properties. Thus was "
           "astromancy born a new form of magick which grants its "
           "users power over fate. Employing a star globe and divining "
           "deck in their miraculous deeds, fortune always smiles "
           "upon these masters of arcana.")
session.add(job7)
session.commit()

ability1 = Ability(name="Combust III",
                   description="Deals unaspected damage over time.",
                   level=72,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job7)
session.add(ability1)
session.commit()

ability2 = Ability(name="Malefic IV",
                   description="Deals unaspected damage with a "
                   "potency of 240.",
                   level=72,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job7)
session.add(ability2)
session.commit()

ability3 = Ability(name="Celestial Intersection",
                   description="Restores own or target party member's HP",
                   level=74,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job7)
session.add(ability3)
session.commit()

ability4 = Ability(name="Horoscope",
                   description="Reads your fortune and those of "
                   "nearby party members, granting them Horoscope.",
                   level=76,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job7)
session.add(ability4)
session.commit()

ability5 = Ability(name="Neutral Sect",
                   description="Aspected Helios and Aspected Benefic "
                   "receive the effects of both Diurnal Sect "
                   "and Nocturnal Sect.",
                   level=80,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job7)
session.add(ability5)
session.commit()

# BLACK MAGE
job8 = Job(name="Black Mage",
           img="https://bit.ly/33sU2Nj", role="Dps",
           author="diego ruiz",
           description="In days long past, there existed an occult and "
           "arcane art known as black magic a potent magic of pure "
           "destructive force born forth by a sorceress of unparalleled "
           "power. Those who learned to wield this instrument of ruin "
           "came to be called black mages, out of both fear and respect "
           "for their gift. Yet great power served to corrupt the "
           "judgment of mortal man, and so he unknowingly set out upon "
           "the path of ruin. Adventurers who take the black will "
           "become agents of devastation, capable of annihilating those "
           "who oppose them through little more than the force "
           "of their will.")
session.add(job8)
session.commit()

ability1 = Ability(name="Despair",
                   description="Deals fire damage with a potency of 380.",
                   level=72,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job8)
session.add(ability1)
session.commit()

ability2 = Ability(name="Umbral Soul",
                   description="Grants Umbral Ice and 1 Umbral Heart.",
                   level=76,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job8)
session.add(ability2)
session.commit()

ability3 = Ability(name="Xenoglossy",
                   description="Deals unaspected damage "
                   "with a potency of 750.",
                   level=80,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job8)
session.add(ability3)
session.commit()

# SUMMONER
job9 = Job(name="Summoner",
           img="https://bit.ly/2B66fLR",
           role="Dps",
           author="diego ruiz",
           description="The beast tribes of Eorzea worship and summon "
           "forth beings known as primals, among which are Ifrit, "
           "Garuda, and Titan. Yet what is a god to one man is a "
           "demon to another, for the city-states of Eorzea see these "
           "beings as a grave threat to their collective survival. In "
           "times immemorial, there lived mages who had not only the "
           "power to summon the primals, but also the means to "
           "transmute the primals' essences, thus binding them to "
           "their will. Known simply as summoners, the existence of "
           "these men and women and their arcane art have been "
           "all but lost to the ages.")
session.add(job9)
session.commit()

ability1 = Ability(name="Firebird Trance",
                   description="Summons Demi-Phoenix to fight by your "
                   "side, which executes Everlasting Flight as it "
                   "manifests. Each time you cast a spell on an enemy, "
                   "Demi-Phoenix will execute Scarlet Flame "
                   "on the same target.",
                   level=72,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job9)
session.add(ability1)
session.commit()

ability2 = Ability(name="Fountain of Fire",
                   description="Deals fire damage with a potency of 250.",
                   level=72,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job9)
session.add(ability2)
session.commit()

ability3 = Ability(name="Brand of Purgatory",
                   description="Deals fire damage to target and all "
                   "enemies nearby it with a potency of 350 for "
                   "the first enemy.",
                   level=72,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job9)
session.add(ability3)
session.commit()

ability4 = Ability(name="Enkindle Phoenix",
                   description="Gradually restores own HP "
                   "and the HP of all nearby party members.",
                   level=80,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job9)
session.add(ability4)
session.commit()

ability5 = Ability(name="Everlasting Flight",
                   description="Gradually restores own HP and the "
                   "HP of all nearby party members.",
                   level=80,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job9)
session.add(ability5)
session.commit()


# RED MAGE
job10 = Job(name="Red Mage",
            img="https://bit.ly/2ILJBwq",
            role="Dps",
            author="diego ruiz",
            description="On the eastern edge of Abalathia's Spine "
            "lies the mountainous region of Gyr Abania. It is in "
            "these elevated lands that people took shelter, when a "
            "burning star guided them away from the Sixth Umbral "
            "Calamity's treacherous floodwaters. The survivors "
            "gathered from near and far, and amongst them were "
            "refugees of the sorcerous cities of Mhach and Amdapor.")
session.add(job10)
session.commit()

ability1 = Ability(name="Engagement",
                   description="Delivers an attack with a potency of 150.",
                   level=72,
                   Cast="Ability",
                   author="diego ruiz",
                   job=job10)
session.add(ability1)
session.commit()

ability2 = Ability(name="Reprise",
                   description="Delivers an attack with a potency of 100.",
                   level=76,
                   Cast="Weaponskill",
                   author="diego ruiz",
                   job=job10)
session.add(ability2)
session.commit()

ability3 = Ability(name="Scorch",
                   description="Deals unaspected damage with "
                   "a potency of 700.",
                   level=80,
                   Cast="Spell",
                   author="diego ruiz",
                   job=job10)
session.add(ability3)
session.commit()

print "all classes added"
