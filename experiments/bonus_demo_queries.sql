-- Reference queries for showing Lab 7 bonus tasks.
-- Every statement is commented out so opening this file cannot change data.
-- Run a query only after applying the matching reference migration to a
-- disposable database. Do not run these against the main course_catalog DB.

-- Bonus 1: after applying bonus_1_level_check_reference.py, PostgreSQL should
-- reject this value with a courses_level_check violation.
-- UPDATE courses SET level = 'expert' WHERE id = 'api-design';

-- Bonus 1: inspect the CHECK registered in PostgreSQL.
-- SELECT conname, pg_get_constraintdef(oid)
-- FROM pg_constraint
-- WHERE conname = 'courses_level_check';

-- Bonus 2: after applying bonus_2_rename_description_reference.py to the
-- disposable scratch database, the original text should be under summary.
-- SELECT id, summary FROM courses ORDER BY id LIMIT 3;

-- Bonus 2: after downgrade, the original description name should exist again.
-- SELECT id, description FROM courses ORDER BY id LIMIT 3;
