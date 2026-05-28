% Hechos (151 Pokémon de Kanto)


pokemon(bulbasaur, planta, veneno).
pokemon(ivysaur, planta, veneno).
pokemon(venusaur, planta, veneno).
pokemon(charmander, fuego, nil).
pokemon(charmeleon, fuego, nil).
pokemon(charizard, fuego, volador).
pokemon(squirtle, agua, nil).
pokemon(wartortle, agua, nil).
pokemon(blastoise, agua, nil).
pokemon(caterpie, bicho, nil).
pokemon(metapod, bicho, nil).
pokemon(butterfree, bicho, volador).
pokemon(weedle, bicho, veneno).
pokemon(kakuna, bicho, veneno).
pokemon(beedrill, bicho, veneno).
pokemon(pidgey, normal, volador).
pokemon(pidgeotto, normal, volador).
pokemon(pidgeot, normal, volador).
pokemon(rattata, normal, nil). %<- GOD
pokemon(raticate, normal, nil).
pokemon(spearow, normal, volador).
pokemon(fearow, normal, volador).
pokemon(ekans, veneno, nil).
pokemon(arbok, veneno, nil).
pokemon(pikachu, electrico, nil).
pokemon(raichu, electrico, nil).
pokemon(sandshrew, tierra, nil).
pokemon(sandslash, tierra, nil).
pokemon(nidoran_hembra, veneno, nil).
pokemon(nidorina, veneno, nil).
pokemon(nidoqueen, veneno, tierra).
pokemon(nidoran_macho, veneno, nil).
pokemon(nidorino, veneno, nil).
pokemon(nidoking, veneno, tierra).
pokemon(clefairy, hada, nil).
pokemon(clefable, hada, nil).
pokemon(vulpix, fuego, nil).
pokemon(ninetales, fuego, nil).
pokemon(jigglypuff, normal, hada).
pokemon(wigglytuff, normal, hada).
pokemon(zubat, veneno, volador).
pokemon(golbat, veneno, volador).
pokemon(oddish, planta, veneno).
pokemon(gloom, planta, veneno).
pokemon(vileplume, planta, veneno).
pokemon(paras, bicho, planta).
pokemon(parasect, bicho, planta).
pokemon(venonat, bicho, veneno).
pokemon(venomoth, bicho, veneno).
pokemon(diglett, tierra, nil).
pokemon(dugtrio, tierra, nil).
pokemon(meowth, normal, nil).
pokemon(persian, normal, nil).
pokemon(psyduck, agua, nil).
pokemon(golduck, agua, nil).
pokemon(mankey, lucha, nil).
pokemon(primeape, lucha, nil).
pokemon(growlithe, fuego, nil).
pokemon(arcanine, fuego, nil).
pokemon(poliwag, agua, nil).
pokemon(poliwhirl, agua, nil).
pokemon(poliwrath, agua, lucha).
pokemon(abra, psiquico, nil).
pokemon(kadabra, psiquico, nil).
pokemon(alakazam, psiquico, nil).
pokemon(machop, lucha, nil).
pokemon(machoke, lucha, nil).
pokemon(machamp, lucha, nil).
pokemon(bellsprout, planta, veneno).
pokemon(weepinbell, planta, veneno).
pokemon(victreebel, planta, veneno).
pokemon(tentacool, agua, veneno).
pokemon(tentacruel, agua, veneno).
pokemon(geodude, roca, tierra).
pokemon(graveler, roca, tierra).
pokemon(golem, roca, tierra).
pokemon(ponyta, fuego, nil).
pokemon(rapidash, fuego, nil).
pokemon(slowpoke, agua, psiquico).
pokemon(slowbro, agua, psiquico).
pokemon(grimer, veneno, nil).
pokemon(muk, veneno, nil).
pokemon(shellder, agua, nil).
pokemon(cloyster, agua, hielo).
pokemon(gastly, fantasma, veneno).
pokemon(haunter, fantasma, veneno).
pokemon(gengar, fantasma, veneno).
pokemon(onix, roca, tierra).
pokemon(drowzee, psiquico, nil).
pokemon(hypno, psiquico, nil).
pokemon(krabby, agua, nil).
pokemon(kingler, agua, nil).
pokemon(voltorb, electrico, nil).
pokemon(electrode, electrico, nil).
pokemon(exeggcute, planta, psiquico).
pokemon(exeggutor, planta, psiquico).
pokemon(cubone, tierra, nil).
pokemon(marowak, tierra, nil).
pokemon(hitmonlee, lucha, nil).
pokemon(hitmonchan, lucha, nil).
pokemon(lickitung, normal, nil).
pokemon(koffing, veneno, nil).
pokemon(weezing, veneno, nil).
pokemon(rhyhorn, tierra, roca).
pokemon(rhydon, tierra, roca).
pokemon(chansey, normal, nil).
pokemon(tangela, planta, nil).
pokemon(kangaskhan, normal, nil).
pokemon(horsea, agua, nil).
pokemon(seadra, agua, nil).
pokemon(goldeen, agua, nil).
pokemon(seaking, agua, nil).
pokemon(staryu, agua, nil).
pokemon(starmie, agua, psiquico).
pokemon(mr_mime, psiquico, hada).
pokemon(scyther, bicho, volador).
pokemon(jynx, hielo, psiquico).
pokemon(electabuzz, electrico, nil).
pokemon(magmar, fuego, nil).
pokemon(pinsir, bicho, nil).
pokemon(tauros, normal, nil).
pokemon(magikarp, agua, nil).
pokemon(gyarados, agua, volador).
pokemon(lapras, agua, hielo).
pokemon(ditto, normal, nil).
pokemon(eevee, normal, nil).
pokemon(vaporeon, agua, nil).
pokemon(jolteon, electrico, nil).
pokemon(flareon, fuego, nil).
pokemon(porygon, normal, nil).
pokemon(omanyte, roca, agua).
pokemon(omastar, roca, agua).
pokemon(kabuto, roca, agua).
pokemon(kabutops, roca, agua).
pokemon(aerodactyl, roca, volador).
pokemon(snorlax, normal, nil).
pokemon(articuno, hielo, volador).
pokemon(zapdos, electrico, volador).
pokemon(moltres, fuego, volador).
pokemon(dratini, dragon, nil).
pokemon(dragonair, dragon, nil).
pokemon(dragonite, dragon, volador).
pokemon(mewtwo, psiquico, nil).
pokemon(mew, psiquico, nil).


% Relaciones de efectividad entre tipos de pokemon

efectivo(acero, hada).
efectivo(acero, hielo).
efectivo(acero, roca).
efectivo(agua, fuego).
efectivo(agua, tierra).
efectivo(agua, roca).
efectivo(bicho, planta).
efectivo(bicho, psiquico).
efectivo(bicho, siniestro).
efectivo(dragon, dragon).
efectivo(electrico, agua).
efectivo(electrico, volador).
efectivo(fantasma, fantasma).
efectivo(fantasma, psiquico).
efectivo(fuego, acero).
efectivo(fuego, bicho).
efectivo(fuego, hielo).
efectivo(fuego, planta).
efectivo(hada, dragon).
efectivo(hada, lucha).
efectivo(hada, siniestro).
efectivo(hielo, planta).
efectivo(hielo, dragon).
efectivo(hielo, tierra).
efectivo(hielo, volador).
efectivo(lucha, acero).
efectivo(lucha, hielo).
efectivo(lucha, normal).
efectivo(lucha, roca).
efectivo(lucha, siniestro).
efectivo(planta, agua).
efectivo(planta, roca).
efectivo(planta, tierra).
efectivo(psiquico, lucha).
efectivo(psiquico, veneno).
efectivo(roca, bicho).
efectivo(roca, fuego).
efectivo(roca, hielo).
efectivo(roca, volador).
efectivo(siniestro, fantasma).
efectivo(siniestro, psiquico).
efectivo(tierra, acero).
efectivo(tierra, electrico).
efectivo(tierra, roca).
efectivo(tierra, fuego).
efectivo(tierra, veneno).
efectivo(veneno, planta).
efectivo(veneno, hada).
efectivo(volador, bicho).
efectivo(volador, planta).
efectivo(volador, lucha).


% Relaciones de no efectividad entre tipos de pokemon
ineficaz(acero, acero).
ineficaz(acero, agua).
ineficaz(acero, electrico).
ineficaz(acero, fuego).
ineficaz(agua, agua).
ineficaz(agua, dragon).
ineficaz(agua, planta).
ineficaz(bicho, acero).
ineficaz(bicho, fantasma).
ineficaz(bicho, fuego).
ineficaz(bicho, hada).
ineficaz(bicho, lucha).
ineficaz(bicho, veneno).
ineficaz(bicho, volador).
ineficaz(dragon, acero).
ineficaz(dragon, hada).
ineficaz(electrico, dragon).
ineficaz(electrico, electrico).
ineficaz(electrico, planta).
ineficaz(fantasma, normal).
ineficaz(fantasma, lucha).
ineficaz(fuego, agua).
ineficaz(fuego, dragon).
ineficaz(fuego, fuego).
ineficaz(fuego, roca).
ineficaz(hada, acero).
ineficaz(hada, fuego).
ineficaz(hada, veneno).
ineficaz(hielo, acero).
ineficaz(hielo, agua).
ineficaz(hielo, fuego).
ineficaz(hielo, hielo).
ineficaz(lucha, bicho).
ineficaz(lucha, hada).
ineficaz(lucha, psiquico).
ineficaz(lucha, veneno).
ineficaz(lucha, volador).
ineficaz(normal, acero).
ineficaz(normal, fantasma).
ineficaz(normal, roca).
ineficaz(planta, acero).
ineficaz(planta, bicho).
ineficaz(planta, dragon).
ineficaz(planta, fuego).
ineficaz(planta, planta).
ineficaz(planta, veneno).
ineficaz(planta, volador).
ineficaz(psiquico, acero).
ineficaz(psiquico, psiquico).
ineficaz(psiquico, siniestro).
ineficaz(roca, acero).
ineficaz(roca, lucha).
ineficaz(roca, tierra).
ineficaz(siniestro, hada).
ineficaz(siniestro, lucha).
ineficaz(siniestro, siniestro).
ineficaz(tierra, bicho).
ineficaz(tierra, planta).
ineficaz(tierra, volador).
ineficaz(veneno, acero).
ineficaz(veneno, fantasma).
ineficaz(veneno, roca).
ineficaz(veneno, tierra).
ineficaz(veneno, veneno).
ineficaz(volador, acero).
ineficaz(volador, electrico).
ineficaz(volador, roca).



% Regla 1:
% Un Pokémon A vencerá a un Pokémon B si, y solo si,
% al menos uno de sus tipos es efectivo contra uno de los tipos de B,
% y ningún tipo de A es ineficaz contra alguno de los tipos de B.

%CODIGO 1%

tipo(POKEMON, TIPO) :-
	pokemon(POKEMON, TIPO, _),
	TIPO \= nil.

tipo(POKEMON, TIPO) :-
	pokemon(POKEMON, _, TIPO),
	TIPO \= nil.

vence_pokemon(PROPIO, RIVAL) :-
	tipo(PROPIO, TIPO_PROPIO),
	tipo(RIVAL, TIPO_RIVAL),
	efectivo(TIPO_PROPIO, TIPO_RIVAL),
	\+ (tipo(PROPIO, OTRO_TIPO_PROPIO), tipo(RIVAL, OTRO_TIPO_RIVAL), ineficaz(OTRO_TIPO_PROPIO, OTRO_TIPO_RIVAL)).

% Un oponente es uno de los contrincantes del combate pokemon
% El equipo de "Candela" está compuesto por "Flareon", "Magmar" y "Moltres"
% [a, b, c] es una lista de instancias
oponente(candela, [flareon, magmar, moltres]).
oponente(blanche, [vaporeon, articuno, lapras]).
oponente(spark, [jolteon, electabuzz, zapdos]).
oponente(gary, [venusaur, blastoise, charizard]).

% Regla 2:
% Para cada Pokémon de mi oponente,
% al menos uno de mis Pokémon debe vencerlo.

% CODIGO 2

vence_equipo(PROPIOS, RIVAL) :-
	oponente(RIVAL, EQUIPO_RIVAL),
	gana_a_todos(PROPIOS, EQUIPO_RIVAL).

gana_a_todos(_, []).

gana_a_todos(PROPIOS, [RIVAL_POKEMON|RESTO]) :-
	member(PROPIO, PROPIOS),
	vence_pokemon(PROPIO, RIVAL_POKEMON),
	gana_a_todos(PROPIOS, RESTO).

mostrar_resultado(PROPIOS, RIVAL) :-
	(   vence_equipo(PROPIOS, RIVAL)
	->  write('Jugador gana')
	;   write('Jugador pierde')
	),
	nl.