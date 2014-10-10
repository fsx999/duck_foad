# coding=utf-8
from django.db import connections, transaction


def dictfetchall(cursor):
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]


def open_cour(db_name):
    cursor = connections['foad'].cursor()
    db_name = 'c_%s' % db_name.strip()
    # maj forum
    cursor.execute("""ALTER TABLE %s_bb_categories ADD group_id INT(11) DEFAULT NULL""" % db_name)
    #maj introduction
    cursor.execute("""ALTER TABLE %s_tool_intro ADD group_id INT(11) DEFAULT NULL""" % db_name)
    #UPDATE INTRO HOME
    cursor.execute("""UPDATE %s_tool_intro SET tool_id = '0' WHERE tool_id= '-1'""" % db_name)
    #MAJ ANNONCE
    cursor.execute("""ALTER TABLE %s_announcement
            MODIFY temps DATETIME DEFAULT NULL,
            MODIFY ordre INT(11) DEFAULT NULL,
            ADD group_id INT(11) DEFAULT NULL,
            ADD auth_id INT(11) DEFAULT NULL
    """ % db_name)
    # UPDATE ORDER ANNONCE
    cursor.execute("""UPDATE %s_announcement SET %s_announcement.ordre = NULL""" % (db_name, db_name))
    # MAJ CALENDAR
    cursor.execute("""ALTER TABLE %s_calendar_event
            ADD group_id INT(11) DEFAULT NULL,
            ADD dayEnd DATE DEFAULT '0000-00-00',
            ADD hourEnd TIME DEFAULT '00:00:00',
            ADD auth_id INT(11) DEFAULT NULL
    """ % db_name)
    #UPDATE DAYEND CALENDAR
    cursor.execute("""UPDATE %s_calendar_event
            SET %s_calendar_event.dayEnd = %s_calendar_event.day,
            %s_calendar_event.hour = '00:00:00'
    """ % (db_name, db_name, db_name, db_name))
    # MAJ GROUP TEAM
    cursor.execute("""ALTER TABLE %s_group_team
            ADD self_registration INT(1) DEFAULT NULL,
            ADD private INT(1) DEFAULT NULL,
            ADD tool TEXT DEFAULT NULL,
            ADD alertMail INT(1) DEFAULT NULL,
            ADD ordre INT(11) DEFAULT NULL,
            ADD visibility ENUM('SHOW', 'HIDE') DEFAULT 'SHOW',
            MODIFY maxStudent INT(11) DEFAULT NULL
    """ % db_name)
    # MOVE GROUP PROPERTY SELF REGISTRATION TO GROUP TEAM
    cursor.execute("""UPDATE %s_group_team AS gr, %s_group_property AS pr
            SET gr.self_registration = pr.self_registration
            WHERE pr.self_registration = 1
    """ % (db_name, db_name))
    # MOVE GROUP PROPERTY PRIVATE TO GROUP TEAM
    cursor.execute("""UPDATE %s_group_team AS gr, %s_group_property AS pr
            SET gr.private = pr.private
            WHERE pr.private = 1
    """ % (db_name, db_name))
    # MOVE GROUP TEAM DESCRIPTION TO TOOL_INTRO
    cursor.execute("""INSERT INTO %s_tool_intro (tool_id, content, group_id)
            SELECT '9' AS tool_id, gr.description, gr.id
            FROM %s_group_team AS gr
            WHERE gr.description !=''
    """ % (db_name, db_name))
    #// EMPTY GROUP DESCRIPTION
    cursor.execute("""UPDATE %s_group_team
            SET %s_group_team.description = NULL
    """ % (db_name, db_name))
    #// MOVE GROUP TEAM TUTOR TO REAL GROUP TEAM
    cursor.execute("""INSERT INTO %s_group_rel_team_user (user, team, status)
            SELECT gr.tutor, gr.id, '1' AS status
            FROM %s_group_team AS gr
            WHERE gr.tutor !=''
    """ % (db_name, db_name))
    #// GROUP TEAM ACTIVATE TOOLS
    cursor.execute("""SELECT forum, document, wiki, chat FROM %s_group_property""" % db_name)
    group_tool = dictfetchall(cursor)
    group_too_list = []
    for tools in group_tool:
        for tool, activate in tools.items():
            if activate == 1 and tool == 'forum':
                group_too_list.append('CLCHT')
            if activate == 1 and tool == 'document':
                group_too_list.append('CLDOC')
            if activate == 1 and tool == 'wiki':
                group_too_list.append('CLFRM')
            if activate == 1 and tool == 'chat':
                group_too_list.append('CLWIKI')
        #for tool, activate in tools:
    grpt = ','.join(group_too_list)
    cursor.execute("""UPDATE %s_group_team SET tool = '%s'""" % (db_name, grpt))
    #// GROUP PROPERTY
    cursor.execute("""ALTER TABLE %s_group_property
            ADD tool TEXT DEFAULT NULL,
            ADD alertMail INT(1) DEFAULT NULL,
            ADD maxStudent INT(11) DEFAULT NULL,
            DROP forum,
            DROP document,
            DROP wiki,
            DROP chat
    """ % db_name)
    cursor.execute("""UPDATE %s_group_property
            SET tool = '%s'""" % (db_name, grpt))
    #// MAJ DESCRIPTION
    cursor.execute("""ALTER TABLE %s_course_description
            ADD group_id INT(11) DEFAULT NULL,
            ADD ordre INT(11) DEFAULT NULL
    """ % db_name)
    #// MAJ ASSIGNMENT
    cursor.execute("""ALTER TABLE %s_wrk_assignment
            ADD ordre INT(11) DEFAULT NULL,
            ADD group_id INT(11) DEFAULT NULL,
            ADD subject_doc_path VARCHAR(200) DEFAULT NULL,
            ADD auth_id INT(11) DEFAULT NULL,
            ADD default_lock enum('enabled','disabled') NOT NULL default 'disabled',
            ADD default_grade enum('enabled','disabled') NOT NULL default 'enabled',
            ADD can_delete enum('enabled','disabled') NOT NULL default 'disabled',
            ADD email_option enum('enabled','disabled') NOT NULL default 'disabled',
            ADD max_submission INT(11) NOT NULL DEFAULT 1,
            ADD in_agenda INT(11) DEFAULT NULL
    """ % db_name)
    #// MAJ SUBMISSION
    cursor.execute("""ALTER TABLE `%s_wrk_submission`
            ADD locked enum('enabled','disabled') NOT NULL default 'disabled',
            ADD email_option enum('enabled','disabled') NOT NULL default 'disabled'
    """ % db_name)
