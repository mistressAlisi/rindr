CREATE OR REPLACE VIEW "ticket_meantimes" AS SELECT (responded-opened) AS mean_response,COUNT(1) AS ticket_count,(responded-opened) AS id from ticket_ticket GROUP BY mean_response ORDER BY ticket_count DESC;

CREATE OR REPLACE VIEW ticket_with_week_view AS  SELECT id,created,affirmer,notes,type_id,contributors,fix,reference,opened,responded,updated,creator_id,archived,difficulty,system,team,extract(WEEK from opened) as week,  ticket_ticket.responded - ticket_ticket.opened AS mean_response, extract(YEAR from ticket_ticket.opened) as year from ticket_ticket;

CREATE OR REPLACE FUNCTION _final_mode(anyarray)
  RETURNS anyelement AS
  $BODY$
      SELECT a
          FROM unnest($1) a
	      GROUP BY 1
	          ORDER BY COUNT(1) DESC, 1
		      LIMIT 1;
		      $BODY$
		      LANGUAGE sql IMMUTABLE;


CREATE AGGREGATE _mode(anyelement) (
  SFUNC=array_append, --Function to call for each row. Just builds the array
    STYPE=anyarray,
      FINALFUNC=_final_mode, --Function to call after everything has been added to array
        INITCOND='{}' --Initialize an empty array when starting
	);

CREATE OR REPLACE VIEW ticket_mode_response_per_week_view AS SELECT _mode(mean_response) AS mode, week, year, _mode(mean_response) as id, count(1) as count  FROM ticket_with_week_view GROUP BY  week, year;

