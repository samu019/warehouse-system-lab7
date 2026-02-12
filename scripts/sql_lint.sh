#!/bin/bash
echo "🔍 Analizando código SQL..."
cd ~/warehouse-system

# Verificar archivos SQL
for file in sql/migrations/*.sql; do
    echo "→ Analizando $file"
    sql-lint "$file" || echo "⚠️  Advertencias en $file"
done

echo "✅ Análisis completado"
