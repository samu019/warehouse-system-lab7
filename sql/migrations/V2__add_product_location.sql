-- ----------------------------------------------------------------------
-- Migración V2: Agregar ubicación física a productos
-- Laboratorio 8 - Requisito 4
-- ----------------------------------------------------------------------

-- 1. Agregar columna location (permitimos NULL inicialmente)
ALTER TABLE products ADD COLUMN location VARCHAR(50);

-- 2. Actualizar registros existentes con ubicaciones por categoría
UPDATE products SET location = 'A1-01' WHERE category = 'Electrónica' AND location IS NULL;
UPDATE products SET location = 'B2-05' WHERE category = 'Periféricos' AND location IS NULL;
UPDATE products SET location = 'C3-12' WHERE category = 'Redes' AND location IS NULL;

-- 3. Crear índice para búsquedas por ubicación
CREATE INDEX idx_products_location ON products(location);

-- 4. Ahora sí, hacer NOT NULL obligatorio
ALTER TABLE products ALTER COLUMN location SET NOT NULL;

-- 5. Documentar el cambio
COMMENT ON COLUMN products.location IS 'Ubicación física en el almacén (formato: estante-posición)';

-- 6. Verificar migración (mensaje en log)
DO $$
BEGIN
    RAISE NOTICE 'Migración V2 aplicada correctamente: columna location agregada a products';
END $$;
