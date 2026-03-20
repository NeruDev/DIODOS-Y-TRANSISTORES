# Changelog

Todos los cambios notables en este repositorio serán documentados aquí.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

---

## [Unreleased]

### Changed
- Reestructuración completa del repositorio según especificación modular
- Módulos educativos movidos a `topics/`
- Renombrado de carpetas a kebab-case
- Consolidación de directivas IA en `AGENTS.md`
- Simplificación del formato de `manifest.json`
- `00-META/` → `00-meta/`
- `media/generated/` → `assets/` en cada módulo
- `_directives.md` → `directives.md` en cada módulo

### Added
- Sistema de auditorías en `audits/`
- Sandbox centralizado en `sandbox/`
- Archivos `.editorconfig` y `CHANGELOG.md`
- Directivas de migración de contenido `Notas/` a `theory/`
- Carpeta `00-meta/templates/` para referencias de futuros repos
- `00-meta/repo-map.md` - Mapa estructural del repositorio

### Removed
- `00-META/ia-contract.md` (contenido consolidado en AGENTS.md)
- Duplicación excesiva entre archivos de directivas IA
- Archivos temporales en raíz (`run_test.py`)

### Migrated
- `Plantilla de Arquitectura Modular Universal.md` → `00-meta/templates/architecture-template.md`
- `generate-claude-md-prompt.md` → `00-meta/templates/context-generation-prompts.md`
- `Temario.md` → `00-meta/temario.md`
- `AUDITORIA_ESTADO_REPO.md` → `audits/reports/2026-03-estado-inicial.md`

---

## [1.0.0] - 2026-02-07

### Added
- Estructura inicial del repositorio
- 5 módulos educativos: DIO, BJT, FET, AMP, PRO
- Sistema de manifest.json por módulo
- Scripts de generación de gráficas en `00-META/tools/`
- Glosario de términos técnicos
- Índice wiki navegable
