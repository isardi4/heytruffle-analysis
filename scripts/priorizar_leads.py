"""Regla de prioridad compartida por el generador de entrega. Sin red ni LLM."""


def score_final(signals):
    """Regla oficial v3. Indicadores revisados, no conteos de menciones."""
    if signals["historical_only"]:
        level, base = "Revalidar antecedente antiguo", 15
    elif signals["explicit_phone_issue"]:
        level, base = "Alta: dificultad telefónica publicada", 80
    elif signals["shared_workload"] or (signals["phone_orders"] and (signals["demand_peak"] or signals["capacity_constraint"])):
        level, base = "Media: hipótesis operativa respaldada", 50
    else:
        level, base = "Exploratoria: encaje y operación telefónica", 30
    # Señales distintas, presencia binaria: 20 citas no equivalen a 20 problemas.
    parts = {"base": base, "canal_pedidos": 5 * signals["phone_orders"],
             "tareas_compartidas": 5 * signals["shared_workload"],
             "demanda": 5 * signals["demand_peak"],
             "atribucion_local": 3 * signals["location_specific"],
             "texto_de_ambas_fuentes_disponible": 3 * signals["source_text_available"],
             "publicacion_operativa_reciente": 3 * signals["recent_operational_publication"]}
    # Mantener bandas separadas: histórico 15–24, exploratorio 30–49,
    # hipótesis 50–69, dificultad explícita 80–99.
    bonus = min(19 if not signals["historical_only"] else 9, sum(v for k, v in parts.items() if k != "base"))
    repeated_locations = signals.get("verified_problem_locations", 0)
    if not signals["historical_only"] and signals["explicit_phone_issue"] and repeated_locations >= 2:
        bonus = min(19, bonus + min(15, 5 * (repeated_locations - 1)))
    return {"version": "prioridad-v3", "level": level, "score": base + bonus,
            "components": parts, "bonus_applied": bonus,
            "cross_location_bonus_available": repeated_locations >= 2}
